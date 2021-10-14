#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple feature that checks whether the tweet contains a photo/video or not

Created on Sun Oct 10 14:17:41 2021

@author: huhlenbrock
"""

import numpy as np
from code.feature_extraction.feature_extractor import FeatureExtractor

# class for extrcating feature if tweet contains photo/video
class PhotoVideo(FeatureExtractor):
    
    # constructor
    def __init__(self, input_column):
        super().__init__([input_column], "{0}_photoVideo".format(input_column))
    
    # don't need to fit, so don't overwrite _set_variables()
    
    # compute how many photos/videos are there
    def _get_values(self, input_one, input_two):
        result = np.array(input_one[0].len() + input_two.len())
        result = result.reshape(-1,1)
        return result


