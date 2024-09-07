#  MH-ET Assistance Tracker


## Content

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Configuration](#configuration)
   1. [MH-ET LIVE Scanner](#mh-et-live-scanner)
   2. [Raspberry Pi](#raspberry-pi)
   3. [Google Drive](#google-drive)
4. [Execution](#execution)


## Introduction
This repository contains a project that allows you to create an attendance list using barcodes. The code was developed in Python, as it is expected to run on a Raspberry Pi. 

The details of the configuration and use of the hardware, as well as its documentation, are presented here as well. 

This is a beta version, which may only work on a local machine. But it is expected that in the future it can be linked to a storage server (cloud or local) that allows automatic synchronization of the files managed by this program.

## Requirements
+ Git
+ Minicom
+ Python 3+
+ python3-pip
+ PyDrive 2+
+ DateTime
+ openpyxl
+ python-dateutil
+ pyserial

## Configuration
### MH-ET LIVE Scanner 
This scanner has two modes of operation:
* Keyboard:
  - In this mode, what was scanned will be detected by the computer as keyboard input.
* Serial port:
  - In this mode, what was scanned will enter the computer's serial port.

Documentation for these modes of operation and other details can be found in the [user manual](/docu/Scanner-v3_manual.pdf). You can also consult the [configuration manual](/docu/Scanner_v3p0_QR_code_module_specification.pdf) if required.

Since we want to automate the scanning process, serial mode has been chosen. Now, in order to use this device in this way, the following steps are required:

![Scanner connection](/img/mh-et_conn.png "MH-ET Scanner connector")

1.   Connect the jumpers as shown in 1.
2.   Check if the device manager can see that there is a new TTY port device in the kernel messages.

     ```bash
     dmesg | grep tty
     ```
     
     If you can't find it, change the USB port, or install the CH340 driver,

3.   Connect the scanner to a computer or device as shown in 2.
4.   To test if the device works, run the following program at the command line, replacing * with your new found drive:

     ```bash
     sudo minicom -D /dev/tty* -b 9600
     ```
     Scan the QR code to detect if it works normally. To exit the terminal, press Ctrl-a x

### Raspberry Pi
To download the files from this repository to the RPi run the following command on the command line:
```bash
git clone https://gitlab.com/liewhnic/pl-scanner.git
```
### Google Drive

This utility is not enabled yet. However, if you want to use Google Drive services, you must follow the steps stipulated in the following [repository](https://github.com/aluna1997/Python_and_PyDrive2)

Likewise, in this [video](https://www.youtube.com/watch?v=ZI4XjwbpEwU) you will find a step-by-step setup guide and code for using Google cloud services.

## Execution
For code execution, go to the src folder and run the following command:
```bash
python3 main.py
```
