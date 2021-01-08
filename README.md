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

>Md5 --> `71DDDA754E8EAD3A534322FC39AD6500`

>Sha1 --> `87F0185273933F424293902B57857C527DD1AEB3`

>Sha256 --> `382DF43A20C7CA0537BD40BB47431159196045DEF836534743B6A6911D26DBBE`

>Sha512 --> `F068F433CA3DFA1D3E2A5C440ECFB13F9F703B156F41B8BA23D3991E01C2DAA1A912F745ECA64564356919888EA6B4C38FF0476C2812DFC7FF188300EEB3BE22`

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
