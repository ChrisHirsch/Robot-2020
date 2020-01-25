# Import the base classes to use anywhere in team3200
from .robot import MyRobot as Robot
from team3200.robotMap import RobotMap as RobotMap

# import submodules
from . import subsystems
from . import commands

# create instance of robotMap for use everywhere
robotMap = RobotMap()

__all__ = ["Robot", "RobotMap", "subsystems", "commands", "robotMap"]
