from dronekit import connect

connection_string="/dev/serial/by-id/usb-ArduPilot_Pixhawk4-BL_370043000651383138373938-if00"

iha=connect(connection_string,wait_ready=True,timeout=100,baud=115200)

print(iha.location.global_relative_frame.alt)
