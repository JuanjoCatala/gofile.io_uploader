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

>Md5 --> `120ce3b98d7894f761e77a4731605b7e`

>Sha1 --> `c0737e53db3eb58f414cba91851c9b3f5f873aaa`

>Sha256 --> `17706ee89714ee8369b9f62e5eb4a5da744f3a688c52b84e3b049b870534f900`

>Sha512 --> `b47127144cc778c4cc3ef2b66c5f007f8de822397f695e1e3f3899413e677845f9832682f779a3e26965524ecd558f80c2e7794b082eb4f4f10c5ed7559ac739`

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
