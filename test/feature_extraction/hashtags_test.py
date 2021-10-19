#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests the "number of hashtags" feature

Created on Sun Oct 10 15:11:20 2021

@author: ml
"""

import unittest

from script.feature_extraction.number_hashtags import NumberHashtags

class HashtagFeatureTest(unittest.TestCase):
    
    def setUp(self):
        self.INPUT_COLUMN = "input"
        self.hashtag_feature = NumberHashtags(self.INPUT_COLUMN)
        self.df[self.INPUT_COLUMN] = ['["cool", "lol"]']
    
    def test_length_input_column(self):
        self.assertEqual(self.hashtag_feature._input_column, len([self.INPUT_COLUMN]))


if __name__ == '__main__':
    unittest.main()

