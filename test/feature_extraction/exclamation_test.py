# -*- coding: utf-8 -*-
"""
Created on Sunday 10.10.2021 15:00

@author hkohnen, huhlenbrock
"""

import unittest
from script.feature_extraction.exclamation_count import ExclamationCount

class ExclamationTest(unittest.TestCase):
    
    def setUp(self):
        self.INPUT_COLUMN = "input"
        self.exclamation_count = ExclamationCount(self.INPUT_COLUMN)
    
    def test_input_columns(self):
        self.assertEqual(self.exclamation_count._input_columns, [self.INPUT_COLUMN])
    
    def test_exclamation_count_sentence(self): 
        EXPECTED_COUNT = [5]
        input_text = 'This is a test tweet!!!!!'
        
        self.assertEqual(self.exclamation_count._get_values(input_text), EXPECTED_COUNT)
            
        
if __name__ == '__main__':
    unittest.main()
        

    
        

