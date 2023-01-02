from sense_emu import SenseHat
from typing import Union
from fastapi import FastAPI

app = FastAPI()
sense = SenseHat()


@app.get("/get_data")
def get_data():
    pressure = sense.get_pressure()
    humidity = sense.get_humidity()
    temperature = sense.get_temperature()
    orientation = sense.get_orientation_degrees()
    # if len(sense.stick.get_events()):
    #     for event in sense.stick.get_events():
    #         timestamp = event.timestamp
    #         direction = event.direction
    #         action = event.action
    # else:
    #     timestamp = 0
    #     direction = None
    #     action = None
    return [
        {
            "temperature": {
                "value": temperature,
                "unit": "C"
            },
            "pressure": {
                "value": pressure,
                "unit": "hPa"
            },
            "humidity": {
                "value": humidity,
                "unit": "%"
            },
            "roll": {
                "value": orientation['roll'],
                "unit": "deg"
            },
            "pitch": {
                "value": orientation['pitch'],
                "unit": "deg"
            },
            "yaw": {
                "value": orientation['yaw'],
                "unit": "deg"
            }
            # "joystick": {
            #     "timestamp": timestamp,
            #     "direction": direction,
            #     "action": action
            # }
        }
    ]


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

