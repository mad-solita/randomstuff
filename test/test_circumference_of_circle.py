import unittest
from tools.circumference_of_circle import circumference_of_circle

class TestCircumferenceOfCircle(unittest.TestCase):
    
    def test_positive(self):
        circumference_of_circle(3)
    
    def test_negative(self):
        with self.assertRaises(ValueError):
            circumference_of_circle(-3)