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


def is_sorted(A : np.ndarray):
    for i in range(A.size -1):
         if A[i+1] > A[i]:
               return False
    return True 

def is_finish(A : np.ndarray, B : np.ndarray):
    if is_sorted(A) and np.count_nonzero(B) == 0:
        return True
    else :    
        return False
    
def is_empty(A : np.ndarray):
    if (np.count_nonzero(A) == 0):
        return True
    else :
        return False
    
def top_is_empty(A : np.ndarray):
    if A[0] == 0:
        return True
    else :
        return False
    
def less_than_two_element(A : np.ndarray):
    if (np.count_nonzero(A) < 2):
        return True
    else :
        return False
    
def index_of_bot(A : np.ndarray):
    return -(np.count_nonzero(A == 0))

def get_bot(A : np.ndarray):
    index_bot = index_of_bot(A)
    return (A[index_bot - 1])


        