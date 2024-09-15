# dht22 temperature and humidity sensor demo code

import time
import adafruit_dht as dht
import board

# dht22 OUT pin is connected to GPIO pin 4
dht22 = dht.DHT22(board.D4)

while True:
    try:
        # get temperature, humidity through dht22 object
        temp_c, humidity = dht22.temperature, dht22.humidity
        print(f"Temp:{temp_c}, Humidity:{humidity}")
    except RuntimeError as err:
        print(err.args[0])

    # wait for two seconds
    time.sleep(2)
