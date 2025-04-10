from gpiozero import MCP3008
from domain.ports import SensorReaderPort


SENSOR_CHANNEL = 0


class HumiditySensorReader(SensorReaderPort):
    def __init__(self):
        self.sensor = MCP3008(SENSOR_CHANNEL)

    def read(self) -> float:
        return self.sensor.value