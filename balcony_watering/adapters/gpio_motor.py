from gpiozero import PWMLED
from domain.ports import MotorControllerPort


MOTOR_PWM_PIN = 19


class GpioMotorController(MotorControllerPort):
    def __init__(self):
        self.motor = PWMLED(MOTOR_PWM_PIN)

    def set_speed(self, speed: float):
        self.motor.value = speed 

    def get_speed(self) -> float:
        return self.motor.value
    
    def stop(self):
        self.motor.value = 0