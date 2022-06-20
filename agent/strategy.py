# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    strategy.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ebennace <ebennace@student.42lausanne.c    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/06/20 11:20:49 by ebennace          #+#    #+#              #
#    Updated: 2022/06/20 11:31:42 by ebennace         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils.constant import *
import numpy as np

class EpsilonGreedy:
    def __init__(self, min, max, decay):
        self.min = min
        self.max = max
        self.decay = decay
        self.epsilon = max
    
    def get_exploration_rate(self, current_step):
        self.epsilon = (self.min + (self.max - self.min)* (np.exp(-self.decay * current_step)))
        return self.epsilon