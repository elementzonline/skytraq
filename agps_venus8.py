from skytraq.venus8 import Venus8
import serial.tools.list_ports


def device_port():
    """Find UART Controller Port"""
    ports = serial.tools.list_ports.comports()
    device_ports = []

    for port, desc, hwid in sorted(ports):
        # print("{}: {} [{}]".format(port, desc, hwid))
        if "USB to UART" in desc:
            device_ports.append(port)

    print(device_ports)
    return device_ports


device_port = device_port()[0]
serial_speed = 115200

# Connect to Port
gps = Venus8(device_port, serial_speed, debug=True)

print("> soft version", gps.getSoftwareVersion(0))

waas_enabled = gps.getWaasStatus()
print("> waas: ", waas_enabled)
nav_mode = gps.getNavigationMode()
print("> navigation mode: ", nav_mode)

# ensure waas is enabled
if not waas_enabled:
    print("Enable WAAS")
    gps.setWaasStatus(True, True)
    print("> waas: ", gps.getWaasStatus())

# ensure we are in pedestrian mode
if nav_mode != "pedestrian":
    print("Enable pedestrian mode")
    gps.setNavigationMode(True, True)
    print("> navigation mode: ", gps.getNavigationMode())

# Disable NMEA Output
gps.enable_nmea_output(enable=False)

print("===================================")
print("======   agps warm start    =======")
print("===================================")

# Send AGPS Warm Start Command
gps.send_restart(restart_type=Venus8.AGPS_WARM_START_MODE)

print("===================================")
print("====   update ephemeris info  =====")
print("===================================")

# Download Ephemeris and Write to Venus8
gps.updateEphemeris()

# Enable NMEA Output
gps.enable_nmea_output(enable=True)

print("============   done   =============")
