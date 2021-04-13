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

>- Upload your files to [gofile.io](https://gofile.io) easily. (This script is supposed to work on windows, but it hasn't been tested)
>- New release (0.0.1), less and cleaner code. More functions will be added

## Capabilities

>- Posibility of uploading files using tor
>- Uploads are logged in the runtime folder
>- User-agent spoofed
>- MD5 check between local and cloud files

## Checksums

gofileUploader.py hashes

>Md5 --> `9b06d7b3ab107c1df18758fed3705b6b`

>Sha1 --> `bad4451e2d9aaee0858b00caf263e1391f48cab6`

>Sha256 --> `e2ad5e7bf6e8b95d43d95bec7f189a0aadbbc0e167194f7b0e66fcc34dcec36a`

>Sha512 --> `47b20040108a0038018421735855e9369c586c9c81751d1f342402050bf3a30757ddea7f5843a1dff7397bcb8038ca6a53a6c18dd8da453a845b5bd8339356b1`

## Setup

***Install requirements***

`$ pip3 install -r requirements.txt`

Then move your files into "uploads/" directory.

## Examples

***For basic info:***

`$ python3 gofile_uploader.py` (Upload your files using YOUR ACTUAL IP)

`$ python3 gofile_uploader.py -t` (Upload your files using TOR. You must have tor running on 127.0.0.1:9050)

![alt text](example.jpg)

## Features to add

- Include native tor binaries
- Add custom proxy capability
