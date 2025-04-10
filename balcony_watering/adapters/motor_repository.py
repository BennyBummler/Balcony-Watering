import os

from domain.ports import MotorStateRepositoryPort
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS


ORGANIZATION=os.environ.get("INFLUX_ORG")  
BUCKET=os.environ.get("INFLUX_BUCKET")    


class InfluxMotorStateRepository(MotorStateRepositoryPort):
    def __init__(self, client: InfluxDBClient):
        self.client = client

    def save(self, motor_state: float):
        write_api = self.client.write_api(write_options=SYNCHRONOUS)
        point = Point("clima")
        point.tag("type", "water_pump")
        point.tag("model", "R385")
        point.field("motor_speed", motor_state)
        print(f"save motor speed {point}")
        write_api.write(bucket=BUCKET, org=ORGANIZATION, record=point)