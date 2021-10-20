#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests the "number of hashtags" feature

Created on Sun Oct 10 15:11:20 2021

@author: ml
"""

import unittest
#import pandas as pd
from script.feature_extraction.number_hashtags import NumberHashtags

class HashtagFeatureTest(unittest.TestCase):
    
    def setUp(self):
        self.INPUT_COLUMN = "input"
        self.hashtag_feature = NumberHashtags(self.INPUT_COLUMN)
        #self.df = pd.DataFrame()
        #self.df[self.INPUT_COLUMN] = ['["cool", "lol"]']
    
    def test_length_input_column(self):
        self.assertEqual(self.hashtag_feature._input_columns, [self.INPUT_COLUMN])

    def test_hashtags_count(self):
        expected = 2
        input_col = ['["cool", "lol"]']
        
        #hashtags_count = len(self.df[self.INPUT_COLUMN])
        hashtags_count = self.hashtag_feature._get_number(input_col)
        
        self.assertEqual(expected, hashtags_count)
    
    


if __name__ == '__main__':
    unittest.main()

