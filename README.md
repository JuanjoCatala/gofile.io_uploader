# gofile.io_uploader
Upload your files to [gofile.io](https://gofile.io) easily with this Python script!. 

## Table of contents
* [General info](#general-info)
* [Checksums](#checksums)
* [Capabilities](#capabilities)
* [Setup](#setup)
* [Examples](#Examples)
* [Features to add](#Features-to-add)


## General info
>Upload your files to [gofile.io](https://gofile.io) easily. (This script is supposed to work on windows, but it hasn't been tested)

## Capabilities

>- Posibility of uploading files using tor
>- User-agent spoofed

## Checksums
gofile_uploader.py hashes

>Md5 --> `1BE9C124AAB94271819CC19FDB6D3181`

>Sha1 --> `5989EEEFBAB7297B980B11EB901B15609D997089`

>Sha256 --> `EA1D8106C1FEA50B58347B4FA191A9D35ED90DCD6C6568BBA1E19A8C8B3BFA23`

>Sha512 --> `3C2347D72C269BDAFEDAF53A964CC25D25ECE186D436ECACEA9C93F438339894FC2747BB57B278D572A5E4C48914FDD28D17F4C7BE1999445FDBC05F9E2DA7F8`

## Setup

***Install requirements***

`$ pip3 install -r requirements.txt`

Then move your files into "files/" directory.

## Examples

***For basic info:***

`$ python3 gofile_uploader.py` (Upload your files using YOUR ACTUAL IP)

`$ python3 gofile_uploader.py tor` (Upload your files using TOR. You must have tor running on 127.0.0.1:9050)

![alt text](example.png)

## Features to add

- Upload many files in only one link
- Include tor binaries
