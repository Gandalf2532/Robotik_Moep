from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction, Axis, Color
from pybricks.tools import wait

HUB = PrimeHub()

HUB.imu.reset_heading(0)

TOPLEFT = Motor(Port.A)
TOPRIGHT = Motor(Port.E)
def PlatteBewegen(direction):
    TOPLEFT.run_angle(1000, direction * 475, wait=False)
    TOPRIGHT.run_angle(1000, direction * -475)
    
PlatteBewegen(1)
wait(1000)
PlatteBewegen(-1)