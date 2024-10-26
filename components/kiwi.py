import math
from phoenix5 import TalonSRX
from phoenix5._ctre import TalonSRXControlMode  # Import the specific control mode
from components.vector import Vector2d


class KiwiDrive:
    def __init__(
        self, left_motor: TalonSRX, right_motor: TalonSRX, back_motor: TalonSRX
    ):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.back_motor = back_motor

        # Angles for the wheel vectors
        self.left_vec = Vector2d(math.cos(math.radians(60)), math.sin(math.radians(60)))
        self.right_vec = Vector2d(
            math.cos(math.radians(120)), math.sin(math.radians(120))
        )
        self.back_vec = Vector2d(
            math.cos(math.radians(270)), math.sin(math.radians(270))
        )

    def drive_cartesian(self, x_speed: float, y_speed: float, z_rotation: float):
        # Calculate directional vector based on input speeds
        input_vector = Vector2d(x_speed, y_speed)

        # Project input vector onto each motor vector and add rotation
        wheel_speeds = [
            input_vector.scalarProject(self.left_vec) + z_rotation,
            input_vector.scalarProject(self.right_vec) + z_rotation,
            input_vector.scalarProject(self.back_vec) + z_rotation,
        ]

        # Normalize speeds if any exceed 1
        max_magnitude = max(abs(speed) for speed in wheel_speeds)
        if max_magnitude > 1.0:
            wheel_speeds = [speed / max_magnitude for speed in wheel_speeds]

        # Set motor speeds with PercentOutput control mode
        self.left_motor.set(TalonSRXControlMode.PercentOutput, wheel_speeds[0])
        self.right_motor.set(TalonSRXControlMode.PercentOutput, wheel_speeds[1])
        self.back_motor.set(TalonSRXControlMode.PercentOutput, wheel_speeds[2])

    def stop(self):
        # Stop the motors by setting their output to zero in PercentOutput mode
        self.left_motor.set(TalonSRXControlMode.PercentOutput, 0)
        self.right_motor.set(TalonSRXControlMode.PercentOutput, 0)
        self.back_motor.set(TalonSRXControlMode.PercentOutput, 0)
