# USoC_Debug_Bridge

This repo is holding the USoC Debug Bridge.

## Setup Bridge

### Requirements:

* debian / ubuntu libs
    ```
    sudo apt install libSDL2-2.0 pyelftools
    ```

* store entire repo to ex: `/opt/usoc_debug_bridge`
* add to ~/.bashrc
    ```
    # debug bridge
    export PATH=/opt/usoc_debug_bridge/bin:$PATH
    export PYTHONPATH=/opt/usoc_debug_bridge/python:$PYTHONPATH
    export LD_LIBRARY_PATH=/opt/usoc_debug_bridge/lib:$LD_LIBRARY_PATH
    export PULP_CONFIGS_PATH=/opt/usoc_debug_bridge/python
    ```

### FAQ

Q: library not found when running `plpbridge`

A: maybe add the library path to `/etc/ld.so.conf.d/plp_bridge.conf`



## Test

```
plpbridge --chip=usoc_v1 --cable=ftdi read --addr=0x1a110000
```

Should give the following result:

```
Found ftdi device i:0x15BA:0x2B:0
Connecting to ftdi device i:0x15BA:0x2B:0
1a110000: 00 00 00 00
```
---

## Serial Monitor

When using the debug USB JTAG, there is also a CDC device that can be found per ID like:

 `/dev/serial/by-id/usb-15ba_Olimex_OpenOCD_JTAG_ARM-USB-OCD-H_OL23F79F-if01-port0`

 With that we can prepare a config for minicom 

`~/.minirc.dfl`

```
pu port             /dev/serial/by-id/usb-15ba_Olimex_OpenOCD_JTAG_ARM-USB-OCD-H_OL23F79F-if01-port0
pu baudrate         1000000
pu rtscts           No
pu linewrap         Yes
pu addcarreturn     Yes
```

install minicom if not already done
```
sudo apt install minicom
```

then start minicom in a terminal:

```
minicom 
```

then after pressing reset it will look like

 ```
***********************************************************
*                                                         *
* USoC Bootloader                                         *
*                                                         *
* Version :749-9f9bc839ba0632901979138e92d41492f808329e   *
* Build   :Fri, 06 Nov 2020 07:46:17 +0100                *
*                                                         *
***********************************************************

OTP 0x0 0x0
LCS EFUSE 0x0
LCS 0x0
Load image from MRAM
Kernel 0x1d020000
addr   0x1d100010
size   0x9378
Start boot process
Found usoc kernel

 ```
