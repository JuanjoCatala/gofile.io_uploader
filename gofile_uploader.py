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

argumentParser = argparse.ArgumentParser(description="Upload files to anonfile.io!")
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
	"https" : "socks5::127.0.0.1:9050"
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
	request = request.get(url, headers=fakeHeaders, proxies=proxy)
	return rarseJSON(request)

def performPOSTRequest(url: str, filename: str, fileContent: bytes) -> dict:
	request = requests.get(url, headers=fakeHeaders, files={"file":(filename, fileContent)})
	return parseJSON(request)

def performPOSTRequestWithProxy(url: str, proxy: dict, filename: str, fileContent: bytes) -> dict:
	request = request.get(url, headers=fakeHeaders, proxies=proxy, files={"file":(filename, fileContent)})
	return parseJSON(request)


def readFile(filename: str, path: str) -> bytes:
	os.chdir(path)
	fileContent: bytes = None

	with open(filename, "rb") as f:
		fileContent = f.read()

	os.chdir(runtimePath)
	return fileContent

def getFileMD5(filename: str, path: str) -> str:
	os.chdir(path)
	fileContent: bytes = readFile(filename, path)
	return hashlib.md5(fileContent).hexdigest()
	os.chdir(runtimePath)

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
		print("[*] Sending " + filename + " to " + "https://" + bestServer + ".gofile.io/uploadFile" + "...")
		return performPOSTRequestWithProxy("https://" + bestServer + ".gofile.io/uploadFile", torProxy, filename, fileContent)
	else:
		print("[*] Sending " + filename + " to " + "https://" + bestServer + ".gofile.io/uploadFile" + "...")
		return performPOSTRequest("https://" + bestServer + ".gofile.io/uploadFile", filename, fileContent)


def createUploadLog(requestJSON: dict):
	
	statusCode: str = requestJSON["status"]
	fileUrl: str = "https://gofile.io/d/" + requestJSON["data"]["code"]
	adminCode: str = requestJSON["data"]["adminCode"]
	filename: str = requestJSON["data"]["fileName"]
	md5: str = requestJSON["data"]["md5"]

	MD5TestResult: bool = [ getFileMD5(filename, "upload") is md5 ] 
	uploadedWithTor: bool = torSelected	

	logFilename: str = "upload" + systemTime + ".txt"
	logFile: _io.TextIOWrapper = open(logFilename, a)	

	f.write("---------------- " + filename + " ---------------- " + systemTime)
	f.write("statusCode -->" + statusCode)
	f.write("filename --> " + filename)
	f.write("file url --> " + fileUrl)
	f.write("adminCode --> " + adminCode + " [Be careful with this]")
	f.write("md5 --> " + md5)
	f.write(" ")
	f.write("[!] MD5 CHECK RESULT [!] --> " + MD5TestResult)	
	f.write("[!] Uploaded with tor? --> " + uploadedWithTor)
	f.write("--------------------------------------------")


def main():
	checkFolders()
	fileList: list = getFilesInUploadFolder()

	for file in fileList:

		fileContent: bytes = readFile(file, "uploads")		
		requestJSON: dict = uploadFile(file, fileContent)

		createUploadLog(requestJSON)


# -------------- MAIN BEGINS HERE -------------------

if __name__ == "__main__":	# just to not execute in case this file is imported
	main()
