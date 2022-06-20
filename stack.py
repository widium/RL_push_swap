# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    stack.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ebennace <ebennace@student.42lausanne.c    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/06/08 08:04:04 by ebennace          #+#    #+#              #
#    Updated: 2022/06/20 09:22:54 by ebennace         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import numpy as np
import random


class Stack():

  def __init__(self, size, empty=False):
    self.range = np.arange(1, 1001, 1)

    if empty == False :

      self.stack = np.random.choice(self.range, size, replace=False)
      self.stack = self.stack.astype('float32')
      self.top = self.stack[0]
      
      
    elif empty == True :
      
      self.stack = np.full(size, 0, dtype=np.float32)
      self.top = self.stack[0]
    
    # reshape in 2D
    self.stack = self.stack.reshape((self.stack.shape[0], 1))
