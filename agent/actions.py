# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    actions.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ebennace <ebennace@student.42lausanne.c    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/06/08 05:38:58 by ebennace          #+#    #+#              #
#    Updated: 2022/06/21 09:28:27 by ebennace         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import numpy as np

from utils.utils import is_sorted, is_finish, is_empty, get_bot
from utils.utils import top_is_empty, less_than_two_element, index_of_bot, bot_is_empty
from utils.utils import add_value_to_bot
from utils.constant import *


def possible_actions(A , B):
  
    push_b = 0 # "push_b"
    push_a = 1 # "push_a"
    rotate_b = 2 # "rotate_b"
    rotate_a = 3 # "rotate_a"
    inverse_rotate_b = 4 # "inverse_rotate_b"
    inverse_rotate_a = 5 # "inverse_rotate_a"
    swap_b = 6 # "swap_b"
    swap_a = 7 # "swap_a"
    rotate = 8 # "rotate"
    reverse = 9 # "reverse"
    swap = 10 # "swap"
    
    action = list()
      
    # SI B a plus d'un elements
    if (np.count_nonzero(B.stack == NULL_VALUE) > 1):
        action.extend([rotate_b,
                       inverse_rotate_b,
                       swap_b])
        
    # Si A a plus d'un elements
    if (np.count_nonzero(A.stack == NULL_VALUE) > 1):
          action.extend([rotate_a,
                         inverse_rotate_a,
                         swap_a])
    
    # Si A a qu'un seul elements ou plus
    if (np.count_nonzero(A.stack == NULL_VALUE) > 0):
        action.extend([push_b])
    
    # Si B a qu'un seul elements ou plus
    if (np.count_nonzero(B.stack == NULL_VALUE) > 0):
        action.extend([push_a])
    
    # si A et B on plus d'un element
    if (np.count_nonzero(A.stack == NULL_VALUE) > 1 and np.count_nonzero(B.stack == NULL_VALUE) > 1) :
        action.extend([rotate,
                       reverse,
                       swap])
    
    return action
      
    
class Moove():

  def __init__(self, A, B, size):
      self.initial_size = size

  
  def push_b(self, A, B):
        
        #si A est trier et que B est vide
        if is_finish(A.stack, B.stack):
          return (BAD_FINISH_REWARD)
        
        # Si A est vide 
        if is_empty(A.stack):
          return (EMPTY_REWARD)

        # ne pas push des nan
        if not top_is_empty(A.stack):
          B.stack = np.insert(B.stack, 0, A.top)
          B.top = A.top
          
          # maj A (supprimer la valeur push, ajouter un nan)
          A.stack = np.delete(A.stack, 0)
          A.stack = np.append(A.stack, NULL_VALUE)
          
          #maj B (supprimer un le 0 du debut)
          if bot_is_empty(B.stack):
            B.stack = np.delete(B.stack, -1)

        # re-Assigner un nouveux top (si A est vide ou si il ya un elements)
        if is_empty(A.stack):
          A.top = None
        else:
          A.top = A.stack[0]
          
        return (ACTION_REWARD)
    
  def push_a(self, A, B):
      
      #si A est trier et que B est vide
      if is_finish(A.stack, B.stack):
        return (BAD_FINISH_REWARD)
      
      # Si B est vide
      if is_empty(B.stack):
        return (EMPTY_REWARD)

      # ne pas push des nan
      if not top_is_empty(B.stack):
        A.stack = np.insert(A.stack, 0, B.top)
        A.top = B.top
          
        # maj B (supprimer la valeur push, ajouter un nan a la fin)
        B.stack = np.delete(B.stack, 0)
        B.stack = np.append(B.stack, NULL_VALUE)
          
        #maj A (supprimer un le 0 du debut)
        if bot_is_empty(A.stack):
          A.stack = np.delete(A.stack, -1) 
        
       # re-Assigner un nouveux top (si B est vide ou si il ya un elements)
      if is_empty(B.stack):
        B.top = None
      else:
        B.top = B.stack[0]
  
      return (ACTION_REWARD)
  
  def rotate_a(self, A, B):
    
    #si A est trier et que B est vide
    if is_finish(A.stack, B.stack):
      return (BAD_FINISH_REWARD)
    
    # Si A est vide ou n'a qu'un element 
    if less_than_two_element(A.stack):
      return (EMPTY_REWARD)
    
    # index du bot
    index = index_of_bot(A.stack)
    A.stack = add_value_to_bot(index, A.stack, A.top)
    A.stack = np.delete(A.stack, 0)
    A.top = A.stack[0]

    return (ACTION_REWARD)

  def rotate_b(self, A, B):
    
    #si A est trier et que B est vide
    if is_finish(A.stack, B.stack):
      return (BAD_FINISH_REWARD)
    
    # Si B est vide ou n'a qu'un element 
    if less_than_two_element(B.stack):
      return (EMPTY_REWARD)
    
    # index du bot
    index = index_of_bot(B.stack)
    B.stack= add_value_to_bot(index, B.stack, B.top)
    B.stack = np.delete(B.stack, 0)
    B.top = B.stack[0]
    
    return (ACTION_REWARD)

  def rotate(self, A, B):
    
    re = 0
    re += self.rotate_a(A, B)
    re += self.rotate_b(A, B)
    return re
    

  def inverse_rotate_a(self, A, B):

    #si A est trier et que B est vide
    if is_finish(A.stack, B.stack):
      return (BAD_FINISH_REWARD)
    
    # Si A est vide ou n'a qu'un element 
    if less_than_two_element(A.stack):
      return (EMPTY_REWARD)
    
    # index du bot
    index_bot = index_of_bot(A.stack)
    bot = get_bot(A.stack)
    
    # bot on top && delete old bot
    A.stack = np.insert(A.stack, 0, bot)
    A.stack = np.delete(A.stack, index_bot -1)
    A.top = A.stack[0]
    
    return (ACTION_REWARD)
  
  def inverse_rotate_b(self, A, B):

    #si A est trier et que B est vide
    if is_finish(A.stack, B.stack):
      return (BAD_FINISH_REWARD)
    
    # Si B est vide ou n'a qu'un element 
    if less_than_two_element(B.stack):
      return (EMPTY_REWARD)

    # index du bot
    index_bot = index_of_bot(B.stack)
    bot = get_bot(B.stack)
    # bot on top && delete old bot
    B.stack = np.insert(B.stack, 0, bot)
    B.stack = np.delete(B.stack, index_bot -1)
    B.top = B.stack[0]
    
    return (ACTION_REWARD)

  def reverse(self, A, B):
    
    re = 0
    re += self.inverse_rotate_a(A, B)
    re += self.inverse_rotate_b(A, B)
    return re
  
  def swap_a(self, A, B):

      #si A est trier et que B est vide
      if is_finish(A.stack, B.stack):
        return (BAD_FINISH_REWARD)
      
      # Si A est vide ou n'a qu'un element 
      if less_than_two_element(A.stack):
        return (EMPTY_REWARD)

      A.stack[[0, 1]] =  A.stack[[1, 0]]
      A.top = A.stack[0]
      
      return (ACTION_REWARD)

  def swap_b(self, A, B):
    
      #si A est trier et que B est vide
      if is_finish(A.stack, B.stack):
        return (BAD_FINISH_REWARD)

      # Si B est vide ou n'a qu'un element 
      if less_than_two_element(B.stack):
        return (EMPTY_REWARD)
      
      
      B.stack[[0, 1]] =  B.stack[[1, 0]]
      B.top = B.stack[0]
      
      return (ACTION_REWARD)
      
  def swap(self, A, B):
    
    re = 0
    re += self.swap_a(A, B)
    re += self.swap_b(A, B)
    return re
  
  
class List_actions:
    
    def __init__(self):
        self.list_of_action = list()
        # self.top = self.list_of_action[-1]
        
    def __str__(self):
        return f"{self.list_of_action}"
    
    def add(self, current_action):
        self.list_of_action.append(current_action)
    
    def compare(self):
        if not self.list_of_action or len(self.list_of_action) == 1:
            return 0;
        
        if self.list_of_action[-1] == 0 and self.list_of_action[-2] == 1:
            return -5
        if self.list_of_action[-1] == 1 and self.list_of_action[-2] == 0:
            return -5
        if self.list_of_action[-1] == 3 and self.list_of_action[-2] == 5:
            return -5
        if self.list_of_action[-1] == 5 and self.list_of_action[-2] == 3:
            return -5
        if self.list_of_action[-1] == 2 and self.list_of_action[-2] == 4:
            return -5
        if self.list_of_action[-1] == 4 and self.list_of_action[-2] == 2:
            return -5
        
        else :
            return 0