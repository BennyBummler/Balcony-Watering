import os

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

from domain.ports import SensorRepositoryPort


BUCKET = os.environ.get("INFLUX_BUCKET")    
ORGANIZATION = os.environ.get("INFLUX_ORG")  


class InfluxSensorRepository(SensorRepositoryPort):
    def __init__(self, client: InfluxDBClient):
        self.client = client

    def save(self, sensor_value):
        write_api = self.client.write_api(write_options=SYNCHRONOUS)
        point = Point("clima")
        point.tag("type", "humidity_sensor")
        point.tag("location", "2")
        point.field("humidity", sensor_value)
        print(f"save sensor value {point}")
        write_api.write(bucket=BUCKET, org=ORGANIZATION, record=point)