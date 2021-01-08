#!/usr/bin/python3

import os
import sys
import datetime
import requests
import json

tor = False

# Enables or disable tor depending on the arguments

try:
    if sys.argv[1] == "tor" or sys.argv[1] == "Tor" or sys.argv[1] == "TOR":
        tor = True
    elif sys.argv[1] != "tor" and sys.argv[1] != "Tor" and sys.argv[1] != "TOR":
        print("Invalid argument. Did you mean 'tor'?")
        sys.exit()
except IndexError:  # In case there's no parameter recieved
    tor = False

# Ask for VPN

if tor == False:
    answer = input("Are you using VPN?? [Y/N] ")
    if answer == "Y" or answer == "y":
        pass
    else:
        sys.exit()

runtime_path = os.getcwd()
time = str(datetime.datetime.now())

#---------- check if directories created

if os.path.exists("files"):
    pass
else: 
    os.mkdir("files")
    print("Dir created, please move your files in there and restart the script")
    sys.exit()

# ---------- Defining proxys and headers ---------------------------------------

tor_proxy = {
        'http' : "socks5://127.0.0.1:9050",
        'https' : "socks5://127.0.0.1:9050"
        }

headers = {

        'user-agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
        'accept-language' : "en-US,en;q=0.5"
        }

# ----------- functions ---------------------------------------------------------

def getFiles():     # Returns a list with the filenames in "files" directory
    os.chdir("files")
    return os.listdir() 
    os.chdir(runtime_path)

# -------------------------------------------------------------------------------

def getBestServer():
    # https://apiv2.gofile.io/getServer
    # example --> {"status":"ok","data":{"server":"srv-file6"}}
    
    if tor: 
        request = requests.get("https://apiv2.gofile.io/getServer", headers=headers, proxies=tor_proxy) # Tor request

    else: # Normal request
        request = requests.get("https://apiv2.gofile.io/getServer", headers=headers)

    recieved_json = json.loads(json.dumps(request.json()))  # Loading recieved json
    data = recieved_json["data"]
    return data["server"]   # Returns best available server
# --------------------------------------------------------------------------------

def uploadFiles(file_list, best_server):
    # https://srv-file6.gofile.io/uploadFile
    # example --> {'status': 'ok', 'data': {'code': 'XnjNq3', 'adminCode': '95WyBxdomNVmjvnmcq7p', 'file': {'name': 'file', 'mimetype': 'text/plain', 'size': 0}}}
    
    recieved_json = None
    
    print("\n" + "Best server --> " + best_server + "\n")

    for file_name in file_list: # Iterating files in directory
       
        os.chdir(runtime_path)
        os.chdir("files/")

        print("[*] Reading '" + file_name + "'...")
        file_content = open(file_name, "rb").read() # Reading file content
        print("[!] Done" + "\n")

        print("[*] Sending '" + file_name + "'...") # Performing request

        if tor: # Tor request
            print("[!] Using tor to perform the request [!]" + "\n")
            request = requests.post("https://" + best_server + ".gofile.io/uploadFile", proxies=tor_proxy, headers=headers, data={"description":file_name}, files={"file":(file_name,file_content)})

        else: # Normal request
            request = requests.post("https://" + best_server + ".gofile.io/uploadFile", headers=headers, data={"description":file_name}, files={"file":(file_name,file_content)})

        print("[*] Done" + "\n")
        recieved_json = json.loads(json.dumps(request.json()))  # Loading json  
        request_headers = request.headers   # Getting request headers
        prepareFileOutput(recieved_json, file_list, best_server, request_headers)    # write all the output on a file

# ----------------------------------------------------------------------------------

def prepareFileOutput(recieved_json, file_list, server, request_headers):
    
    os.chdir(runtime_path)
    output = open("output_" + time + ".txt", "a")
   
    status = recieved_json["status"]
    data = recieved_json["data"]
    file_info = data["file"]

    file_url = "https://gofile.io/d/" + data["code"]
    admin_code = data["adminCode" ]
    file_name = file_info["name"]
    file_size = file_info["size"]
    file_type = file_info["mimetype"]
    
    output.write("--------- " + file_name  + " ------------ [" + str(datetime.datetime.now()) + "] \n" )
    output.write("Filename --> " +  file_name + "\n")
    output.write("File size --> " + str(file_size)+ " bytes" + "\n")
    output.write("File type --> " + file_type + "\n")
    output.write("File url --> " + file_url + "\n")
    output.write("Used server --> " + server + "\n")
    output.write("Admin code --> " + admin_code + " (Don't share this!)" + "\n")
    output.write(" " + "\n")
    output.write("Request headers --> " + str(request_headers) + "\n")

    if tor:
        output.write(" ")
        output.write("---- [UPLOADED USING TOR] ----" + "\n")

    output.write("-------------------------------" + "\n")
    output.write(" " + "\n")
    output.close()


#--------------------- Main ----------------------------------

try:
    file_list = getFiles()
    best_server = getBestServer()
    uploadFiles(file_list, best_server)

except FileNotFoundError:
    print("FileNotFoundError - Please, move your files into 'files' directory")
    sys.exit()

except requests.exceptions.ConnectionError:
    print("ConnectionError - Please, check your internet connection, your VPN or tor (tor must run on 127.0.0.1:9050)")
    sys.exit()

except ConnectionRefusedError:
    print("ConnectionRefusedError - Please, check your internet connection, your proxy or your VPN")

except requests.exceptions.HTTPError:
    print("HTTPError - Probably API has changed")
    sys.exit()

except requests.exceptions.ProxyError:
    print("ProxyError - Is tor running on 127.0.0.1:9050 ?")

except requests.exceptions.SSLError:
    print("SSLError - An SSL error ocurred")
    sys.exit()

except requests.exceptions.ConnectTimeout:
    print("ConnectTimeoutError - Request timed out while trying to connect to server")
    sys.exit()

except requests.exceptions.ReadTimeout:
    print("ReadTimeoutError - Server didn't send any data in the alloted amount of time")
    sys.exit()

except requests.exceptions.InvalidURL:
    print("InvalidURLError - API URL seems to be invalid")
    sys.exit()

except requests.exceptions.InvalidHeader:
    print("InvalidHeaderError - Header seems to be invalid")
    sys.exit()

except json.decoder.JSONDecodeError:
    print("JSONDecodeError - Failed while decoding json response")
    sys.exit()

except KeyboardInterrupt:
    sys.exit()


