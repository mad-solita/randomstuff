import unittest
from tools import circumference_of_circle

class TestCircumferenceOfCircle(unittest.TestCase):
    
    def test_positive(self):
        circumference_of_circle.circumference_of_circle(3)
    
    def test_negative(self):
        circumference_of_circle.circumference_of_circle(-3)