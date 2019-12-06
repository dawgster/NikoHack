import RPi.GPIO as GPIO

def poll_door_sensor():
    return GPIO.input(5) == GPIO.HIGH

def poll_parcel_sensor():
    return GPIO.input(6) == GPIO.HIGH

def poll_security_sensor():
    return False

def vicinity_put_parcel_status():
    pass

def vicinity_put_security_status():
    pass

if __name__ == "main":

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(5, GPIO.IN)
    GPIO.setup(6, GPIO.IN)
    GPIO.setup(7, GPIO.IN)

    while True:

        door_sensor_status = poll_door_sensor()
        parcel_sensor_status = poll_parcel_sensor()
        sec_sensor_status = poll_security_sensor()