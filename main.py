import RPi.GPIO as GPIO
import time
from hx711 import HX711
import numpy as np
import smbus
import math


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
    GPIO.output(5, GPIO.LOW)
    start = time.time()

    while GPIO.input(6) == GPIO.HIGH:
        now = time.time()
        if now - start > 0.2:
            GPIO.output(5, GPIO.HIGH)
            return True

    stop = time.time()

    time_diff = stop-start
    dist = (340 * time_diff)/2.0 #340 assumed as speed of sound, gives dist in meters

    if dist > 0.1:
        GPIO.output(5, GPIO.HIGH)
        return True

    GPIO.output(5, GPIO.HIGH)
    return False



def poll_parcel_sensor(sensor_handle):

     measurments = sensor_handle.get_raw_data(num_measures=3)
     avg_measurment = np.mean(measurments)

     scaling_factor = 1.0
     offset = 0.0

     weight = scaling_factor * avg_measurment + offset

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

    accel_vec = np.array([accel_xout_scaled, accel_yout_scaled, accel_zout_scaled]).reshape((3,1))/9.81

    return np.linalg.norm(accel_vec) > 1.5

def vicinity_put_parcel_status():
    pass

def vicinity_put_security_status():
    pass

if __name__ == "main":

    GPIO.setmode(GPIO.BOARD)

    #door sensor init
    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(6, GPIO.IN)
    GPIO.output(5, GPIO.HIGH)

    #parcel sensor init
    hx711 = HX711(
        dout_pin=7,
        pd_sck_pin=8,
        channel='A',
        gain=64
    )

    hx711.reset()

    #Security sensor init
    power_mgmt_1 = 0x6b
    power_mgmt_2 = 0x6c

    bus = smbus.SMBus(1)
    address = 0x68

    # Aktivieren, um das Modul ansprechen zu koennen
    bus.write_byte_data(address, power_mgmt_1, 0)


    while True:

        door_sensor_status = poll_door_sensor()
        parcel_sensor_status = poll_parcel_sensor()
        sec_sensor_status = poll_security_sensor()