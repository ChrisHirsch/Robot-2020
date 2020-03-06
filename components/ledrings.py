from wpilib import DigitalInput as dio
from magicbot import StateMachine, state, tunable
from components.breakSensors import BreakSensors, Sensors


class LedRings(StateMachine):
    """Statemachine to do LEDs"""
    compatString = ["doof"]

    breakSensors: BreakSensors
    xboxMap: XboxMap

    # Tunables
    pulseSpeed = tunable(1)

    def __init__(self):

        # Get our sensors

       
        # Make it so #1
        self.engage()

    def on_enable(self):
        """
        Called when the bot is enabled. This will register our states with the proper code
        """
        self.breakSensors.registerSensorEvent(
            self, 
            "pulseRingsUp", 
            Sensors.kShootingSensor, 
            True, 
            "shootInitShooting", 
            "shootRunShooter")


    def pulseRingsUp(self):
        """
        Sets the pulse direction so the rings go "up" and will probably be used when intaking balls and firing
        """
        self.logger.debug("Pulsing rings UP")
        self.pulseDirection = "Up"
        self.next_state('pulseRings')
    
    def pulseRingsDown(self):
        """
        Sets the pulse direction so the rings go "down" and will probably be used when we are sending balls
        back out throught he loader (barf mode)
        """
        self.logger.debug("Pulsing rings DOWN")
        self.pulseDirection = "Down"
        self.next_state('pulseRings')

    def stopPulse(self):
        """
        Stop pulsing the LED rings
        """
        self.next_state('idle')

    @state
    def pulseRings(self, state_tm):
        print("Pulsing Rings %s" % self.pulseDirection)

    @state(first = True)
    def idle(self):
        pass

    def execute(self):
        
        # Make it so #1
        self.engage()
