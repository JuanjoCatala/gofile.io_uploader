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

>Md5 --> `6f2ef43d6a4e509552ebbbd8e3cd606d`

>Sha1 --> `1306da5fe03c9ef0368d7af41133565559857379`

>Sha256 --> `4044d4d90bf2ae2e6d1d130c63f7bca7026bbef2ea78d9411932b9636bdce87a`

>Sha512 --> `ec9a1bca55cadee28854e2eefc1245540a8fcc1a6e68e55c99df47422c8c31f6e0b8a0d34715c2a4fb6c0742cdff101eb57ebaa6d2b5c9a1d2c0a88f5baca682`

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
