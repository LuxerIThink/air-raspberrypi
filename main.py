from sense_emu import SenseHat
from typing import Union
from fastapi import FastAPI

app = FastAPI()
sense = SenseHat()
timestamp = 0
direction = None
action = None


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


@app.put("/put_led")
def put_led(request: list):
    for data in request:
        sense.set_pixel(data["x"], data["y"], data["r"], data["g"], data["b"])
    return {"Status": "Success"}


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
