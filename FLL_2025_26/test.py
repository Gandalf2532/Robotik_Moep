from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction, Axis, Color
from pybricks.tools import wait

HUB = PrimeHub()

HUB.imu.reset_heading(0)
BEWEGUNGSMOTOREN = DriveBase(Motor(Port.D, Direction.COUNTERCLOCKWISE), Motor(Port.C), 56, 130)
#130 anpassen, falls falsch. Dann aber allen mitteilen
BEWEGUNGSMOTOREN.use_gyro(True)
winkel = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 200, 270, 360,]

for i in winkel:
    BEWEGUNGSMOTOREN.turn(i)
    wait(500)
    BEWEGUNGSMOTOREN.turn(-i)