from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction

hub = PrimeHub()

Bewegungsmotoren = DriveBase(Motor(Port.C), Motor(Port.D, Direction.COUNTERCLOCKWISE), 55, 100) #Reifendurchmesser und achsenlänge abmessen

Bewegungsmotoren.straight(200)
Motor()

