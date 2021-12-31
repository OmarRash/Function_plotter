import unittest
from backend import valid_input_num

class TestValidInputNum(unittest.TestCase):
    def test_empty_input(self):
        self.assertFalse(valid_input_num("",""))

    def test_symbol_input(self):
        self.assertFalse(valid_input_num("- ","+ "))
    
    def test_letter_input(self):
        self.assertFalse(valid_input_num("z","1"))
    
    def test_max_smaller_than_min(self):
        self.assertFalse(valid_input_num("10","1"))
    
    def test_negative_values (self):
        self.assertTrue(valid_input_num("-10","-1"))
    
    def test_normal_values(self):
        self.assertTrue(valid_input_num("5","20"))
    
if __name__=="__main__":
    TestValidInputNum()

    
       
        