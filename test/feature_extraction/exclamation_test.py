# -*- coding: utf-8 -*-
"""
Created on Sunday 10.10.2021 15:00

@author hkohnen, huhlenbrock
"""

import unittest
import pandas as pd
from code.feature_extraction.exclamation_count import ExclamationCount

class ExclamationTest(unittest.TestCase):
    
    def setUp(self):
        self.INPUT_COLUMN = "input"
        self.exclamation_count = ExclamationCount(self.INPUT_COLUMN)
        self.df = pd.DataFrame()
        self.df[self.INPUT_COLUMN] = ['["This", "!", "is", "!", "a", "!", "test", "!", "tweet", "!"]']
    
    def test_input_columns(self):
        self.assertEqual(self.exclamation_count._input_columns, [self.INPUT_COLUMN])
    
    def test_exclamation_count_sentence(self): 
        self.exclamation_count.fit(self.df)
        EXPECTED_COUNT = [5]
        
        ex_count = self.exclamation_count._return
        
        self.assertEqual(ex_count, EXPECTED_COUNT)
        

    
        

