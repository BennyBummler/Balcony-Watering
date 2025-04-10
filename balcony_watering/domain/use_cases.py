from time import sleep

from domain import ports 


def read_and_save_humidity(sensor: ports.SensorReaderPort, sensor_repository: ports.SensorRepositoryPort):
    while True:
        value = sensor.read()
        sensor_repository.save(value)
        sleep(60)


def set_and_save_motor_speed(motor: ports.MotorControllerPort, motor_repository: ports.MotorStateRepositoryPort):
    while True:
        value = float(input("Add motorspeed from 0-1:\t"))
        motor.set_speed(value)
        motor_repository.save(value)