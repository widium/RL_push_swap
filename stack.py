# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    stack.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ebennace <ebennace@student.42lausanne.c    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/06/08 08:04:04 by ebennace          #+#    #+#              #
#    Updated: 2022/06/08 09:14:36 by ebennace         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import numpy as np
import random


class Stack():

  def __init__(self, size, empty=False):
      
      
      # self.A = self.scaler.transform(self.A.stack)

      if empty == False :

        self.stack = np.random.choice(range(100), size, replace=False)
        self.stack = self.stack.astype('float32')
        self.top = self.stack[-1]
        
        
      elif empty == True :
        
        self.stack = np.full(size, np.nan, dtype=np.float32)
        self.top = None
      
      # reshape in 2D
      self.stack = self.stack.reshape((self.stack.shape[0], 1))
