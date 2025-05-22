# USoC_Debug_Bridge

This repo is holding the USoC Debug Bridge.

## Setup Bridge

### Requirements:

* GIT version control is installed.
    ```
    sudo apt-get install git 
    ```

* Python 3 is installed.
    ```
    sudo apt-get install python3-pip
    ```

* libSDL2 is installed.
    ```
    sudo apt-get install libSDL2-2.0
    ```

### Install Bridge

Insatll the python-pyelftools.
```
sudo pip3 install pyelftools
```

Clone repository.
```
git clone git@gitlab.sensry.net:ganymed/usoc_debug_bridge.git
```

Switch to directory *usoc_debug_bridge/* and make build script executable.
```
cd usoc_debug_bridge
chmod +x build_sourceme.sh
```

Generate sourceme by running:
```
./build_sourceme.sh
```

To use the bridge source the sourceme script.
```
source sourceme.sh
```

See also https://github.com/pulp-platform/pulp-debug-bridge.

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
