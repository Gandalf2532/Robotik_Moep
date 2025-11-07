from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction, Axis, Color
from pybricks.tools import wait

HUB = PrimeHub()

HUB.imu.reset_heading(0)
BEWEGUNGSMOTOREN = DriveBase(Motor(Port.D, Direction.COUNTERCLOCKWISE), Motor(Port.C), 56, 150)
#130 anpassen, falls falsch. Dann aber allen mitteilen
BEWEGUNGSMOTOREN.use_gyro(True)
BEWEGUNGSMOTOREN.settings(straight_speed=800)

BEWEGUNGSMOTOREN.straight(280)
BEWEGUNGSMOTOREN.turn(90)
BEWEGUNGSMOTOREN.straight(500)
BEWEGUNGSMOTOREN.straight(-500)
BEWEGUNGSMOTOREN.turn(-90)
BEWEGUNGSMOTOREN.straight(-280)
