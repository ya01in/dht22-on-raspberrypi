#!/home/li/Workspace/dht22/dht/bin/python3
# a recorder program that can continuously collect temperature and humidity
# info, and save it into a csv file.

import csv
import time
import datetime
import adafruit_dht as dht
import board
import logging
from typing import List

# dht22 is connected to GPIO 4
dht22 = dht.DHT22(board.D4)


def get_info() -> tuple[str]:
    # Get temperature info from dht22 with retry.
    # Currently is set to retry 10 times, then it will exit the program
    # save the environment for debugging
    logging.info("Getting env info")
    count = 1
    while count:
        if count > 11:
            logging.error("Fail to get env message over 10 time, abort program")
            logging.error("Please check circuit")
            exit(1)

        try:
            temp_c, humidity = dht22.temperature, dht22.humidity
            logging.info(f"Temp:{temp_c}, Humidity:{humidity}")
            count = 0 if (temp_c is not None and humidity is not None) else count + 1
        except RuntimeError as err:
            logging.warning(f"Fail to get env info, error message:{err.args[0]}")
            count += 1
    return temp_c, humidity


def write2csv(file_name: str, data: List[str]) -> None:
    with open(file_name, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)
    logging.info("Data recorded")


def main() -> None:
    # initialize the csv file with header if it just been created
    with open(FILENAME, mode="a", newline="") as file:
        if file.tell() == 0:
            logging.info("File is empty, init with header")
            writer = csv.writer(file)
            writer.writerow(["time", "temp", "humidity"])

    logging.info("Start recorder")
    while True:
        temp, hum = get_info()
        current_time = datetime.datetime.now().timestamp()
        data = [current_time, temp, hum]
        write2csv(FILENAME, data)
        logging.info(f"Logged data:{data}")
        time.sleep(INTERVAL)


if __name__ == "__main__":
    FORMAT = "%(asctime)s %(levelname)s: %(message)s"
    logging.basicConfig(level=logging.INFO, format=FORMAT)
    FILENAME = "env_record.csv"
    INTERVAL = 30
    main()

