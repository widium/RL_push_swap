# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    utils.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ebennace <ebennace@student.42lausanne.c    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/06/08 05:38:49 by ebennace          #+#    #+#              #
#    Updated: 2022/06/20 09:28:45 by ebennace         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from utils.constant import *


def is_sorted(A : np.ndarray):
    for i in range(A.size -1):
         if A[i+1] < A[i]:
               return False
    return True 

def is_finish(A : np.ndarray, B : np.ndarray):
    if is_sorted(A) and is_empty(B):
        return True
    else :    
        return False
    
def is_empty(A : np.ndarray):
    if np.all(A == NULL_VALUE):
        return True
    else :
        return False
    
def top_is_empty(A : np.ndarray):
    if A[0] == NULL_VALUE:
        return True
    else :
        return False
    
def bot_is_empty(A : np.ndarray):
    if A[-1] == NULL_VALUE:
        return True
    else :
        return False
    
def less_than_two_element(A : np.ndarray):
    if (np.count_nonzero(A != NULL_VALUE) < 2):
        return True
    else :
        return False
    
def index_of_bot(A : np.ndarray):
        return -(np.count_nonzero(A == NULL_VALUE))

def get_bot(A : np.ndarray):
    index_bot = index_of_bot(A)
    return (A[index_bot - 1])

def add_value_to_bot(index : int, A : np.ndarray, top : float):
    #if stack is full
    if (index == 0):
      A = np.append(A, top)
    else :
      A = np.insert(A, index, top)
    return A