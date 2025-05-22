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
