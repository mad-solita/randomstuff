import unittest
from tools.piston_extension_formula import piston_sequence

class TestPistonExtensionFormula(unittest.TestCase):
    
    def test_positive(self):
        piston_sequence(50)
        piston_sequence(500)
        piston_sequence(1001)
        
    def test_negative(self):
        with self.assertRaises(ValueError):
            piston_sequence(-5)