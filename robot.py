import math
from magicbot import AutonomousStateMachine, tunable, MagicRobot
from phoenix5 import TalonSRX
from wpilib import XboxController, run
from phoenix5._ctre import TalonSRXControlMode  # Import the specific control mode
from components.kiwi import KiwiDrive


class Robot(MagicRobot):
    def createObjects(self):
        # Define motor controllers (adjust IDs to match your setup)
        self.left_motor = TalonSRX(0)
        self.right_motor = TalonSRX(1)
        self.back_motor = TalonSRX(2)

        # Initialize KiwiDrive with motors
        self.kiwi_drive = KiwiDrive(self.left_motor, self.right_motor, self.back_motor)

        # Initialize Xbox controller on port 0
        self.controller = XboxController(0)

    def teleopPeriodic(self):
        # Read controller inputs for the Kiwi drive
        x_speed = self.controller.getLeftX()
        y_speed = -self.controller.getLeftY()  # Invert Y if needed
        z_rotation = self.controller.getRightX()

        # Drive the robot based on controller inputs
        self.kiwi_drive.drive_cartesian(x_speed, y_speed, z_rotation)

    def autonomousPeriodic(self):
        # Code for autonomous mode, if applicable
        pass

    def disabledInit(self):
        # Stop the motors when the robot is disabled
        self.kiwi_drive.stop()


if __name__ == "__main__":
    run(Robot)
