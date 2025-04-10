import threading
from gpiozero import PWMLED, MCP3008

import os, time
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS


INFLUX_HOST = os.environ.get("http://raspberrypi:8086")
INFLUX_TOKEN = os.environ.get("INFLUX_TOKEN")
INFLUX_ORG = os.environ.get("INFLUX_ORG")
INFLUX_BUCKET = os.environ.get("INFLUX_BUCKET")



def read_and_save_humidity(sensor: MCP3008, influx_db_client: InfluxDBClient) -> float:
    while True:
        humidity =sensor.value
        write_api = influx_db_client.write_api(write_options=SYNCHRONOUS)
            
        point = Point("clima")
        point.tag("location", "2")
        point.field("humidity", humidity)
        write_api.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=point)
        print(f"save humidity {point}")
        time.sleep(60)


def set_and_save_motor_speed(motor: PWMLED, influx_db_client: InfluxDBClient):
    while True:
        value = float(input("Add motorspeed from 0-1:\t"))
        motor.value = value

        write_api = influx_db_client.write_api(write_options=SYNCHRONOUS)
        point = Point("clima")
        point.tag("type", "water_pump")
        point.tag("model", "R385")
        point.field("motor_speed", value)
        print(f"save motor speed {point}")
        write_api.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=point)


def main(sensor: MCP3008, motor: PWMLED, client: InfluxDBClient):
    sensor_thread = threading.Thread(target=read_and_save_humidity, args=[sensor, client], daemon=True)
    motor_thread = threading.Thread(target=set_and_save_motor_speed, args=[motor, client])
    sensor_thread.start()
    motor_thread.start()
    

if __name__=="__main__":   
    sensor = MCP3008(0)
    motor = PWMLED(19)
    client = InfluxDBClient(url=INFLUX_HOST, token=INFLUX_TOKEN, org=INFLUX_ORG)
    try:
        main(sensor, motor, client)
    finally:
        motor.value=0