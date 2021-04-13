import os
import sys
import requests
import json
import argparse
import datetime
import hashlib

# ----- API URLs -----
# https://api.gofile.io/getServer
# https://{server}.gofile.io/uploadFile
# 
# https://api.gofile.io/deleteUpload?c=XXXXAbc&token=XXXX
# https://api.gofile.io/getAccountInfo?token=XXXXXX
# https://api.gofile.io/getUploadsList?token=XXXXXXX


# ---- setting up the arguments ------

argumentParser = argparse.ArgumentParser(description="Upload files to anonfile.io! | Ver. 0.0.1")
argumentParser.add_argument("-p", "--proxy", type=str, required=False, help="Upload files through a custom proxy")


mutuallyExclusiveGroup = argumentParser.add_mutually_exclusive_group(required=False)
mutuallyExclusiveGroup.add_argument("-t", "--tor", help="Upload files trough tor proxy (127.0.0.1:9050)", action="store_true", required=False)

arguments = argumentParser.parse_args()


# -------- Defining variables --------

runtimePath: str = os.getcwd()
torSelected: bool = arguments.tor
systemTime: str = str(datetime.datetime.now())


torProxy: dict = {
	"http" : "socks5://127.0.0.1:9050",
	"https" : "socks5://127.0.0.1:9050"
	}

fakeHeaders: dict = {
	"user-agent" : "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36",
	"accept-language" : "en-US,en;q=0.5"
	
	}


def checkFolders():
	if not os.path.exists("uploads"):
		os.mkdir("uploads")	
		raise Exception("Folder 'upload' does not exists. Please restart the script and put your files in there")	

def getFilesInUploadFolder() -> list:
	os.chdir("uploads")
	files: dict = os.listdir()
	os.chdir(runtimePath)
	return files

def parseJSON(requestJson: requests) -> dict:
	return json.loads(json.dumps(requestJson.json()))

def performGETRequest(url: str) -> dict:
	request = requests.get(url, headers=fakeHeaders)
	return parseJSON(request)

def performGETRequestWithProxy(url: str, proxy: dict) -> dict:
	request = requests.get(url, headers=fakeHeaders, proxies=proxy)
	return rarseJSON(request)

def performPOSTRequest(url: str, filename: str, fileContent: bytes) -> dict:
	request = requests.post(url, headers=fakeHeaders, files={"file":(filename, fileContent)})
	return parseJSON(request)

def performPOSTRequestWithProxy(url: str, proxy: dict, filename: str, fileContent: bytes) -> dict:
	request = requests.post(url, headers=fakeHeaders, proxies=proxy, files={"file":(filename, fileContent)})
	return parseJSON(request)


def readFile(filename: str) -> bytes:
	os.chdir("uploads")
	with open(filename, "rb") as f:
		os.chdir(runtimePath)
		return f.read()

def getFileMD5(filename: str) -> str:
	fileContent: bytes = readFile(filename)
	MD5Hash: str = hashlib.md5(fileContent).hexdigest()
	os.chdir(runtimePath)
	return MD5Hash

def getBestServer() -> str:
	# {"status":"ok","data":{"server":"srv-store1"}}	

	if torSelected:
		return performGETRequestWithProxy("https://api.gofile.io/getServer", torProxy)["data"]["server"]
	else:
		return performGETRequest("https://api.gofile.io/getServer")["data"]["server"]


def uploadFile(filename: str, fileContent: str) -> dict:
	# {"status":"ok","data":{"code":"123Abc","adminCode":"Cd9yjCk62syKNEPfAeQg","fileName":"file.txt","md5":"2a4a7522de4ba17a8c6cd920c89f8386"}}	

	bestServer: str = getBestServer()	

	if torSelected:
		print(f"\n[*] Sending {filename} to https://{bestServer}.gofile.io/uploadFile")
		return performPOSTRequestWithProxy("https://" + bestServer + ".gofile.io/uploadFile", torProxy, filename, fileContent)
	else:
		print(f"\n[*] Sending {filename} to https://{bestServer}.gofile.io/uploadFile")
		return performPOSTRequest("https://" + bestServer + ".gofile.io/uploadFile", filename, fileContent)


def replaceIlegalChars(filename: str):
	ilegalChars: tuple = (" ", "\\", "/", ":", ",", "<", ">")
	
	cleanName: str = None
	for char in filename:
		if char in ilegalChars:
			cleanName = filename.replace(char, "-")
	return cleanName
		

def createUploadLog(requestJSON: dict):
	
	statusCode: str = requestJSON["status"]
	fileUrl: str = "https://gofile.io/d/" + requestJSON["data"]["code"]
	adminCode: str = requestJSON["data"]["adminCode"]
	filename: str = requestJSON["data"]["fileName"]
	uploadMD5: str = requestJSON["data"]["md5"]
	

	MD5TestResult: bool = getFileMD5(filename) == uploadMD5 
	uploadedWithTor: bool = torSelected	

	logFilename: str = replaceIlegalChars(f"upload.{systemTime}.txt")
	logFile: _io.TextIOWrapper = open(logFilename, "a")	

	logFile.write("---------------- " + filename + " ---------------- " + systemTime + "\n")
	logFile.write("statusCode -->" + statusCode + "\n")
	logFile.write("filename --> " + filename + "\n")
	logFile.write("file url --> " + fileUrl + "\n")
	logFile.write("adminCode --> " + adminCode + " [Be careful with this] \n")
	logFile.write("md5 --> " + uploadMD5 + "\n")

	logFile.write("\n")

	logFile.write("[!] MD5 CHECK RESULT [!] --> " + str(MD5TestResult) + "\n")	
	logFile.write("[!] Uploaded with tor? [!] --> " + str(uploadedWithTor) + "\n")
	logFile.write("\n")

	logFile.close()

	

def printLogFile():

	logName = replaceIlegalChars(f"upload.{systemTime}.txt")
	print(f"\n[*] Log file saved as '{runtimePath}/{logName}' \n")
		
	with open(logName, "rt") as logFile:
		print(logFile.read())

def main():
	checkFolders()
	fileList: list = getFilesInUploadFolder()

	for file in fileList:

		fileContent: bytes = readFile(file)		
		requestJSON: dict = uploadFile(file, fileContent)
		
		os.chdir(runtimePath)
		createUploadLog(requestJSON)

	printLogFile()

# -------------- MAIN BEGINS HERE -------------------

if __name__ == "__main__":	# just to not execute in case this file is imported
	main()
