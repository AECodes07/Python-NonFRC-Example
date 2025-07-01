# Phoenix 6 outside FRC using Python

Very simple getting started example for using Phoenix 6 in Python.

## Requirements

1. Make sure you meet the [Phoenix 6 System Requirements](https://v6.docs.ctr-electronics.com/en/stable/docs/installation/requirements.html)
2. Install `requirements.txt` with `pip install -r requirements.txt`.
2. If using a CANivore on Linux, [install canivore-usb](https://v6.docs.ctr-electronics.com/en/stable/docs/canivore/canivore-setup.html#linux-non-frc)

If running on linux with a generic USB to CAN SocketCAN adapter, run the `./generic_socketcan_start.sh` script.

If you're using CANivore on Windows, no additional steps are needed to interface with the CANivore.
Ensure Tuner's "CANivore USB" toggle is off when running hardware-attached on Windows.

### FRC-Lock
If a device has seen an FRC Robot Controller (RoboRIO or similar), it will "[FRC-Lock](https://v6.docs.ctr-electronics.com/en/stable/docs/api-reference/api-usage/enabling-actuators.html#frc-lock)".
Unlock it for non-FRC use by performing a Factory Default in Tuner.

## Running Robot Code

The Python package of Phoenix 6 by-default runs simulation if the system supports it.
In order to run with hardware, set the `CTR_TARGET` environment variable to "Hardware".

A table of what to run is provided below:

|Target|Windows|Linux|MacOS|
|---|---|---|---|
|Simulation|`python robot.py`|`python robot.py`|`python robot.py`|
|Hardware|`$env:CTR_TARGET="Hardware"; python robot.py`|`CTR_TARGET=Hardware python robot.py`|Not supported|
