#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 18:05:28 2021

Simple feature that counts the number of hashtags used in a tweet.

@author: huhlenbrock, hkohnen
"""
import numpy as np
from script.feature_extraction.feature_extractor import FeatureExtractor

# class for extracting the number of hashtags
class NumberHashtags(FeatureExtractor):
    
    def __init__(self, input_column):
        super().__init__([input_column], "{0}_nrHashtags".format(input_column))
        
    # count hashtags  
    def _get_values(self, inputs):
<<<<<<< HEAD

        result = np.array(inputs[0].str.count('#'))
        result = result.reshape(-1,1)
=======
        
        result = np.array(inputs[0].str.count('#'))
        result = result.reshape(-1, 1)
>>>>>>> 4cbc7c1c9fda8a1f463f2c9ef635aec4b9012944
        return result
