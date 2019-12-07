#!/usr/bin/env python3

import requests
from dotenv import load_dotenv
import os

load_dotenv()


def set_bulb_color(h, s, v):
    ip = os.getenv("raspi_ip")
    object_id_bulb = os.getenv("object_id_bulb")

    if ip is None:
        raise RuntimeError("Undefined environment variable `raspi_ip`")

    if object_id_bulb is None:
        raise RuntimeError("Undefined environment variable `object_id_bulb`")

    url = 'http://' + ip + ":9997/agent/remote/objects/" + object_id_bulb + "/properties/Bulb2_Color"

    headers = {
        'Content-Type': 'application/json',
        'infrastructure-id': 'VAS',
        'adapter-id': 'HackathonSampleService'
    }

    data = "{value:'" + str(h) + "," + str(s) + "," + str(v) + "'}"

    r = requests.put(url=url, data=data, headers=headers)


def flash_bulb_color():
    """
    Flashes the current color. Set the color with `set_bulb_color`.
    """
    ip = os.getenv("raspi_ip")
    object_id_bulb = os.getenv("object_id_bulb")

    if ip is None:
        raise RuntimeError("Undefined environment variable `raspi_ip`")

    if object_id_bulb is None:
        raise RuntimeError("Undefined environment variable `object_id_bulb`")

    url = 'http://' + ip + ":9997/agent/remote/objects/" + object_id_bulb + "/properties/Bulb2_Alert"

    headers = {
        'Content-Type': 'application/json',
        'infrastructure-id': 'VAS',
        'adapter-id': 'HackathonSampleService'
    }

    data = "{value:'LSELECT'}"

    r = requests.put(url=url, data=data, headers=headers)

def bulb_set_disabled_status():
    set_bulb_color(0.6*255, 0, 0)

def bulb_set_parcel_status():
    set_bulb_color(0.6*255, 100, 50)
    flash_bulb_color()

def bulb_set_security_status():
    set_bulb_color(0, 100, 10)
    flash_bulb_color()
