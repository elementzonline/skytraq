Skytraq
=======

Skytraq Venus 8 GPS binary protocol implentation

# Purpose

This is the repository that gives sample codes for testing S1216F8 Skytrack GPS/GNSS module. 
This GPS device outputs NMEA messages which can be read in the PC using a USB to serial port converter. It
also has the ability to store gps logs (date, position and speed) to its
internal memory.
Skytraq uses a proprietary binary protocol to communicate with the module.
This protocol is specified in two application notes:
- [Binary Messages of Venus 6 GPS](http://dlnmh9ip6v2uc.cloudfront.net/datasheets/Sensors/GPS/AN0003_v1.4.19.pdf)
- [Data Logging Extension for Venus 6 GPS](http://dlnmh9ip6v2uc.cloudfront.net/datasheets/Sensors/GPS/Venus/638/doc/AN0008_v1.4.11-datalogging.pdf)

# Status

## Working features:
- read/write navigation mode
- read/write waas status
- read software version / crc
- configure serial port speed
- probe serial port speed
- write ephemeris data (agps) to device
- enable/disable NMEA output
- restart system ( hot start, warm start, gps warmstart)

## TODO
- read/write output format
- read/write position output rate
- reset to factory default

# Usage

- to update ephemeris data use agps.py (UNTESTED)

# Reference to other similar projects

- https://github.com/r0ro/skytraq - the core code is derived from this repo which was for Venus6 type chip.
