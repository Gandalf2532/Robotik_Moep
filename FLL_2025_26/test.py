from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction, Axis, Color
from pybricks.tools import wait

HUB = PrimeHub()

BEWEGUNGSMOTOREN = DriveBase(Motor(Port.C), Motor(Port.D, Direction.COUNTERCLOCKWISE), 55, 100) #55mm Reifendurchmesser, 100mm achesnbreite

#Tests, wie genau Pybricks arbeitet und ob ein eigener GyroTurn gebraucht wird. Am Ende sollte der Bot da stehen, wo er gestartet ist.

#Anscheinend sind GyroStraight und GyroTurn schon integriert. Wer weiß, wie gut die sind 🤷‍♂️

BEWEGUNGSMOTOREN.straight(200)
BEWEGUNGSMOTOREN.turn(90)
BEWEGUNGSMOTOREN.turn(-90)
BEWEGUNGSMOTOREN.straight(-200)

BEWEGUNGSMOTOREN.straight(2000)
BEWEGUNGSMOTOREN.turn(180)
BEWEGUNGSMOTOREN.turn(-180)
BEWEGUNGSMOTOREN.straight(-2000)