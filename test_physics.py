import unittest
import physics
import math


class TestPhysics(unittest.TestCase):
    def test_calculate_buoyancy(self):
        self.assertEqual(physics.calculate_buoyancy(1, 1), 9.81)
        self.assertEqual(physics.calculate_buoyancy(0, 1), ValueError)
        self.assertEqual(physics.calculate_buoyancy(1, 0), ValueError)
        self.assertEqual(physics.calculate_buoyancy(-1, 1), ValueError)
        self.assertEqual(physics.calculate_buoyancy(1, -1), ValueError)

    def test_will_it_float(self):
        self.assertEqual(physics.will_it_float(10, 1), True)
        self.assertEqual(physics.will_it_float(1, 1001), False)
        self.assertEqual(physics.will_it_float(1, 1000), None)
        self.assertEqual(physics.will_it_float(0, 1), ValueError)
        self.assertEqual(physics.will_it_float(1, 0), ValueError)
        self.assertEqual(physics.will_it_float(-1, 1), ValueError)
        self.assertEqual(physics.will_it_float(1, -1), ValueError)

    def test_calculatepressure(self):
        self.assertEqual(physics.calculate_pressure(10), 98100)
        self.assertEqual(physics.calculate_pressure(-1), ValueError)

    def test_calculate_acceleration(self):
        self.assertEqual(physics.calculate_acceleration(10, 2), 5)
        self.assertEqual(physics.calculate_acceleration(1, -1), ValueError)
        self.assertEqual(physics.calculate_acceleration(1, 0), ValueError)

    def test_calculate_angular_acceleration(self):
        self.assertEqual(physics.calculate_angular_acceleration(6, 3), 2)
        self.assertEqual(physics.calculate_angular_acceleration(1, -1), ValueError)
        self.assertEqual(physics.calculate_angular_acceleration(1, 0), ValueError)

    def test_calculate_moment_of_Inertia(self):
        self.assertEqual(physics.calculate_moment_of_inertia(2, 2), 8)
        self.assertEqual(physics.calculate_moment_of_inertia(-1, 1), ValueError)
        self.assertEqual(physics.calculate_moment_of_inertia(0, 1), ValueError)
        self.assertEqual(physics.calculate_moment_of_inertia(1, -1), ValueError)

    def test_calculate_auv_acceleration(self):
        self.assertEqual(
            physics.calculate_auv_acceleration(100, math.pi, 100, 0.1, 0.5),
            [-2.0000000000000004, 2.0000000000000004],
        )
        self.assertEqual(
            physics.calculate_auv_acceleration(100, math.pi),
            [-2.0000000000000004, 2.0000000000000004],
        )

    def test_calculate_auv_angular_acceleration(self):
        self.assertEqual(physics.calculate_auv_angular_acceleration(1, math.pi / 2), 2)

    def test_calculate_auv2_acceleration(self):
        self.assertEqual(
            physics.calculate_auv2_acceleration(
                [1, 2, 3, 4],
                0,
            )
        )


if __name__ == "__main__":
    unittest.main()
