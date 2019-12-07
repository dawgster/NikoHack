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
        'Content-Type' : 'application/json',
        'infrastructure-id': 'VAS',
        'adapter-id': 'HackathonSampleService'
    }

    data = "{value:'" + str(h) + "," + str(s) + "," + str(v) + "'}"

    r = requests.put(url=url, data=data, headers=headers)
