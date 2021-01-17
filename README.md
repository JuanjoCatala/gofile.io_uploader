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

>Md5 --> `a094412a0c0f49b38a2436e7116896a2`

>Sha1 --> `b737cbd950a0c50b320ecbf14a11e1b52190860d`

>Sha256 --> `a00a4e298a06a6b5ea4e04158195748ff57ad14e80d63a6be13d2f722fb29e13`

>Sha512 --> `77c4faeabde6adccb1e125b12aaee5d0fb5bb46ab690418f631d57d7a06c77e0d414925c90641774bbb713b00347f0d4f48c25008d3713f03c6ee25819f153aa`

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
