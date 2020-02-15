import motorHelper


class Intake:
    # Note - The way we will want to do this will be to give this component motor description dictionaries from robotmap and then creating the motors with motorhelper. After that, we simply call wpilib' differential drive
    intake_motorsList: dict

    def setup(self):
        self.motors = {}
        self.speed = 0
        for motorDescKey in self.intake_motorsList:
            currentMotor = self.intake_motorsList[motorDescKey]
            print("{}".format(currentMotor))
            self.motors[motorDescKey] = motorHelper.createMotor(currentMotor)

        self.shooterMotor = self.motors['shooterMotor']
    
    def setSpeed(self, speed):
        self.speed = speed

    def execute(self):
        self.shooterMotor.set(self.speed)