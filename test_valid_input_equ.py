from tkinter.constants import X
import unittest
from backend import valid_input_equ
import numpy as np

class TestValidInputEqu(unittest.TestCase):
    
    def test_empty_input(self):
        x = np.arange(1, 10, 0.01)
        self.assertFalse(valid_input_equ("",x))

    def test_symbol_input(self):
        x = np.arange(1, 10, 0.01)
        self.assertFalse(valid_input_equ("-",x))
    
    def test_wrong_letter_input(self):
        x = np.arange(1, 10, 0.01)
        self.assertFalse(valid_input_equ("z",x))
    
    def test_number_input(self):
        x = np.arange(1, 10, 0.01)
        self.assertTrue(valid_input_equ("1",x))
    
    def test_valid_equ(self):
        x = np.arange(1, 10, 0.01)
        self.assertTrue(valid_input_equ("1/(x**2+1)",x))
    
    def test_invalid_equ(self):
        x = np.arange(1, 10, 0.01)
        self.assertFalse(valid_input_equ("x****9",x))
    
if __name__=="__main__":
    TestValidInputEqu()