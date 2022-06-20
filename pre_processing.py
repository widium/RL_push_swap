# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pre_processing.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ebennace <ebennace@student.42lausanne.c    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/06/08 06:41:55 by ebennace          #+#    #+#              #
#    Updated: 2022/06/13 08:56:22 by ebennace         ###   ########.fr        #
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

def denormalize_vector(output):
    
    vector = np.array([[0,
                        1,
                        2,
                        3,
                        4,
                        5,
                        6,
                        7,
                        8,
                        9,
                        10]], dtype=np.float32)
    
    vector = vector.reshape((vector.shape[1], vector.shape[0]))
    
    print("Vector Shape : ", vector.shape)
    print("Vector : ", vector)
    print("Output Shape : ", output.shape)
    print("Output : ", output)

    scaler = MinMaxScaler(feature_range=(0, 1))
    vector_scaled = scaler.fit_transform(vector)

    output = output.reshape((output.shape[1], output.shape[0]))
    output = scaler.inverse_transform(output)

    return (output)
    