import os
import threading

from influxdb_client import InfluxDBClient

from dotenv import load_dotenv
load_dotenv()

from adapters.humidity_sensor import HumiditySensorReader
from adapters.gpio_motor import GpioMotorController
from adapters.sensor_repository import InfluxSensorRepository
from adapters.motor_repository import InfluxMotorStateRepository
from domain.use_cases import read_and_save_humidity, set_and_save_motor_speed


INFLUX_HOST = os.environ.get("INFLUX_HOST")
INFLUX_TOKEN = os.environ.get("INFLUX_TOKEN")
INFLUX_ORG = os.environ.get("INFLUX_ORG")


def main(sensor: HumiditySensorReader, sensor_repo: InfluxSensorRepository, motor: GpioMotorController, motor_repo: InfluxMotorStateRepository):    
    sensor_thread = threading.Thread(target=read_and_save_humidity, args=[sensor, sensor_repo], daemon=True)
    motor_thread = threading.Thread(target=set_and_save_motor_speed, args=[motor, motor_repo])
    sensor_thread.start()
    motor_thread.start()


if __name__=="__main__":
    sensor = HumiditySensorReader()
    motor = GpioMotorController()
    client = InfluxDBClient(url=INFLUX_HOST, token=INFLUX_TOKEN, org=INFLUX_ORG)

    sensor_repo = InfluxSensorRepository(client)
    motor_repo = InfluxMotorStateRepository(client)

    try:
        main(sensor, sensor_repo, motor, motor_repo)
    finally:
        motor.stop()