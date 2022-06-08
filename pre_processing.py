# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pre_processing.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ebennace <ebennace@student.42lausanne.c    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/06/08 06:41:55 by ebennace          #+#    #+#              #
#    Updated: 2022/06/08 10:08:15 by ebennace         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import numpy as np
from sklearn.preprocessing import MinMaxScaler

class Normalize:
    def __init__(self):
        self.Min_Max = MinMaxScaler(feature_range=(0, 1))
    
    def transform(self, A):
        A = self.Min_Max.fit_transform(A)
        return (A)
    
    def inverse_transform(self, A):
        A = self.Min_Max.inverse_transform(A)
        return (A)
         
    
def pre_processing_state(state):
    tensor = state.reshape((1, state.shape[0], state.shape[1]))
    return tensor
