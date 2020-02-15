import motorHelper


class Shooter:
    # Note - The way we will want to do this will be to give this component motor description dictionaries from robotmap and then creating the motors with motorhelper. After that, we simply call wpilib' differential drive
    shooter_motorsList: dict

    def setup(self):
        self.motors = {}
        self.speed = 0
        for motorDescKey in self.shooter_motorsList:
            currentMotor = self.shooter_motorsList[motorDescKey]
            print("{}".format(currentMotor))
            self.motors[motorDescKey] = motorHelper.createMotor(currentMotor)

        self.shooterMotor = self.motors['shooterMotor']
    
    def setSpeed(self, speed):
        self.speed = speed

    def intake(self):
        self.speed = -1
    
    def shoot(self):
        self.speed = 1
        print("shooting")

    def stop(self):
        self.speed = 0
        print("stopping")

    def execute(self):
        self.shooterMotor.set(self.speed)
        print("shooter execute")
