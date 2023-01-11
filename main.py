from sense_emu import SenseHat
from typing import Union
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json

app = FastAPI()
sense = SenseHat()
timestamp = 0
direction = None
action = None


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/get_data")
async def get_data():
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


@app.put("/put_led")
async def put_led(request: Request):
    try:
        json_data = await request.json()
    except json.decoder.JSONDecodeError:
        raise HTTPException(status_code=404, detail="Item not found")

    for data in json_data:
        sense.set_pixel(data["x"], data["y"], data["r"], data["g"], data["b"])

    return JSONResponse(content="{}")


# def main():
#     global timestamp, direction, action
#
#     while True:
#         for event in sense.stick.get_events():
#             timestamp = event.timestamp
#             direction = event.direction
#             action = event.action
#             print("The joystick was {} {}".format(event.action, event.direction))
#
# if __name__ == '__main__':
#     main()
