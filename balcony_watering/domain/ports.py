# domain/ports.py
from abc import ABC, abstractmethod

class MotorControllerPort(ABC):
    @abstractmethod
    def set_speed(self, speed: float):
        pass

    @abstractmethod
    def get_speed(self) -> float:
        pass

    @abstractmethod
    def stop(self):
        pass


class MotorStateRepositoryPort(ABC):
    @abstractmethod
    def save(self, motor_state):
        pass

class SensorReaderPort(ABC):
    @abstractmethod
    def read(self) -> float:
        pass

class SensorRepositoryPort(ABC):
    @abstractmethod
    def save(self, sensor_value):
        pass