#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Feature that counts the exclamation points in a tweet.

Created on Sun Oct 10 13:55:28 2021

@author: hkohnen, huhlenbrock
"""

import numpy as np
from script.feature_extraction.feature_extractor import FeatureExtractor

# class for extracting number of exclamation marks in a tweet as a feature
class ExclamationCount(FeatureExtractor):
    
    # constructor
    def __init__(self, input_column):
        super().__init__([input_column], "{0}_number_of_exclamation_marks".format(input_column))
    
    # don't need to fit, so don't overwrite _set_variables()
    
    # compute the number of occuring exclamation marks based on the inputs
    def _get_values(self, inputs):
        
        result = np.array(inputs[0].str.count('!'))
        result = result.reshape(-1,1)
        return result
