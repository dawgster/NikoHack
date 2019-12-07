import RPi.GPIO as GPIO
import time
from hx711 import HX711
import numpy as np
import smbus
import math

from bulb import set_bulb_color, bulb_set_disabled_status, bulb_set_parcel_status, bulb_set_security_status

sec_sensor_status = False

def read_byte(reg):
    return bus.read_byte_data(address, reg)


def read_word(reg):
    h = bus.read_byte_data(address, reg)
    l = bus.read_byte_data(address, reg + 1)
    value = (h << 8) + l
    return value


def read_word_2c(reg):
    val = read_word(reg)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val


def dist(a, b):
    return math.sqrt((a * a) + (b * b))


def get_y_rotation(x, y, z):
    radians = math.atan2(x, dist(y, z))
    return -math.degrees(radians)


def get_x_rotation(x, y, z):
    radians = math.atan2(y, dist(x, z))
    return math.degrees(radians)


def poll_door_sensor():
    GPIO.output(6, GPIO.LOW)
    time.sleep(0.00001)

    start = time.time()
    stop = time.time()

    while GPIO.input(12) == 0:
        start = time.time()


    while GPIO.input(12) == 1:
        stop = time.time()

    time_diff = stop-start
    dist = (34300 * time_diff)/2.0 #340 assumed as speed of sound, gives dist in meters
    #print(dist)
    if dist > 30:
        GPIO.output(6, GPIO.HIGH)
        return True

    GPIO.output(6, GPIO.HIGH)
    return False



def poll_parcel_sensor(sensor_handle):

     print("reading weight")
     measurments = sensor_handle.get_raw_data_mean(5)
     avg_measurment = measurments

     scaling_factor = 1.0
     offset = 0.0

     weight = scaling_factor * avg_measurment + offset

     print(weight)

     if weight > 0.5:
         return True

     return False

def poll_security_sensor():

    accel_xout = read_word_2c(0x3b)
    accel_yout = read_word_2c(0x3d)
    accel_zout = read_word_2c(0x3f)

    accel_xout_scaled = accel_xout / 16384.0
    accel_yout_scaled = accel_yout / 16384.0
    accel_zout_scaled = accel_zout / 16384.0

    accel_vec = np.array([accel_xout_scaled, accel_yout_scaled, accel_zout_scaled]).reshape((3,1))
    norm = np.linalg.norm(accel_vec)
    print(norm)
    return norm > 1.1 or norm < 0.75

def vicinity_put_parcel_status(status):

    bulb_set_parcel_status() if status else bulb_set_disabled_status()

def vicinity_put_security_status(status):

    bulb_set_security_status() if status else bulb_set_disabled_status()

def wait_for_authorization_state():
    global sec_sensor_status
    door_sensor_status = poll_door_sensor()
    sec_sensor_status = poll_security_sensor() if  not sec_sensor_status else True

    print("wait for authorized_state")

    if door_sensor_status or sec_sensor_status:
        vicinity_put_security_status(True)

    if not sec_sensor_status:
        vicinity_put_parcel_status(False)

    if GPIO.input(24) == 1:
        print("autorized")
        return "authorized_state"

    return "wait_for_authorization_state"


def authorized_state():

    global sec_sensor_status
    door_sensor_status = poll_door_sensor()
    sec_sensor_status = poll_security_sensor() if not sec_sensor_status else True
    print("authorized_state")
    GPIO.output(16, GPIO.LOW)
    if sec_sensor_status:
        vicinity_put_security_status(True)

    if not sec_sensor_status:
        vicinity_put_parcel_status(False)

    if door_sensor_status == True:
        return "wait_for_package_state"

    return "authorized_state"


def wait_for_package_state():

    global sec_sensor_status
    door_sensor_status = poll_door_sensor()
    sec_sensor_status = poll_security_sensor() if not sec_sensor_status else True

    print("wait_for_package_state")

    GPIO.output(16, GPIO.HIGH)
    print(GPIO.input(16))
    if sec_sensor_status:
        vicinity_put_security_status(True)

    if not sec_sensor_status:
        vicinity_put_parcel_status(False)

    if door_sensor_status == False:
        time.sleep(0.5)
        return "occupied_state"

    return "wait_for_package_state"

def occupied_state():

    global sec_sensor_status
    #door_sensor_status = poll_door_sensor()
    sec_sensor_status = poll_security_sensor() if not sec_sensor_status else True

    GPIO.output(16, GPIO.LOW)

    print("occupied state")

    if sec_sensor_status:
        print("Security breach")

    if sec_sensor_status:
        vicinity_put_security_status(True)

    if not sec_sensor_status:
        vicinity_put_parcel_status(True)

    return "occupied_state"



state_machine = {"wait_for_authorization_state": wait_for_authorization_state,
                 "authorized_state": authorized_state,
                 "wait_for_package_state": wait_for_package_state,
                 "occupied_state": occupied_state}

if __name__ == "__main__":

    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()

    #door sensor init
    GPIO.setup(6, GPIO.OUT)
    GPIO.setup(12, GPIO.IN)
    GPIO.output(6, GPIO.HIGH)

    #RFID
    GPIO.setup(24, GPIO.IN)

    #Kühlschrank Light
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(16, GPIO.LOW)
    #GPIO.output(16, GPIO.HIGH)

    print("initializing")
    #parcel sensor init
    #hx711 = HX711(
    #    dout_pin=22,
    #    pd_sck_pin=23
    #)
    print("resetting")
    #hx711.reset()
    print("hx711 initialized")
    #Security sensor init
    power_mgmt_1 = 0x6b
    power_mgmt_2 = 0x6c

    bus = smbus.SMBus(1)
    address = 0x68

    # Aktivieren, um das Modul ansprechen zu koennen
    bus.write_byte_data(address, power_mgmt_1, 0)
    bulb_set_disabled_status()
    state = "wait_for_authorization_state"
    while True:

        state_function = state_machine[state]
        state = state_function()


