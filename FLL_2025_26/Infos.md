BEWEGUNGSMOTOREN = DriveBase(Motor(Port.D, Direction.COUNTERCLOCKWISE), Motor(Port.C), 56, 130)
BEWEGUNGSMOTOREN.use_gyro(True)


Das muss so, weil unsere Motoren "falsch* bzw. anders als die Programmierer geplant haben, angebaut sind