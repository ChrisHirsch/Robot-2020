import motorHelper


class Shooter:
    # Note - The way we will want to do this will be to give this component motor description dictionaries from robotmap and then creating the motors with motorhelper. After that, we simply call wpilib' differential drive
    shooter_motorsList: dict

    def setup(self):
        self.motors = {}
        self.speed = 0
        for motorDescKey in self.driveTrain_motorsList:
            currentMotor = self.driveTrain_motorsList[motorDescKey]
            print("{}".format(currentMotor))
            self.motors[motorDescKey] = motorHelper.createMotor(currentMotor)

        self.shooterMotor = self.motors['shooterMotor']
    
    def setSpeed(self, speed):
        self.speed = speed

    def execute(self):
        self.shooterMotor.set(self.speed)