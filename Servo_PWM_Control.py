import sys
sys.path.append("/home/apsync/dronekit-python/")
print(sys.path)

import time 
from dronekit import connect, VehicleMode, mavutil


connection_string = '0.0.0.0:9000'

def set_servo(vehicle, servo_number, pwm_value):
	pwm_value_int = int(pwm_value)
	msg = vehicle.message_factory.command_long_encode(
		0, 0, 
		mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
		0,
		servo_number,
		pwm_value_int,
		0,0,0,0,0
		)
	vehicle.send_mavlink(msg)
 
print("Connecting to plane on %s" % (connection_string,))
vehicle = connect(connection_string)

print(" GPS: %s" % vehicle.gps_0)
print(" Battery: %s" % vehicle.battery)
print(" Last Heartbeat: %s" % vehicle.last_heartbeat)
print(" Is Armable?: %s" % vehicle.is_armable)
print(" System status: %s" % vehicle.system_status.state)
print(" Mode: %s" % vehicle.mode.name)

for x in range(1, 60):
	set_servo(vehicle, 1, 1100)
	time.sleep(1)
	set_servo(vehicle, 1, 1500)
	time.sleep(1)
	set_servo(vehicle, 1, 1100)

vehicle.close()    
print("Completed")