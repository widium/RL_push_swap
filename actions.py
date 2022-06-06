
import numpy as np

from utils import is_sorted

def delta(A_size, size):
  return (A_size - size)


class Action():
    
    def __init__(self, A, B):
        self.A = A
        self.B = B
        
        self.push_b = 0 # "push_b"
        self.push_a = 1 # "push_a"
        self.rotate_b = 2 # "rotate_b"
        self.rotate_a = 3 # "rotate_a"
        self.inverse_rotate_b = 4 # "inverse_rotate_b"
        self.inverse_rotate_a = 5 # "inverse_rotate_a"
        self.swap_b = 6 # "swap_b"
        self.swap_a = 7 # "swap_a"
        self.rotate = 8 # "rotate"
        self.reverse = 9 # "reverse"
        self.swap = 10 # "swap"
  
            
    def possible_actions(self):
        action = list()
        # Si la Stack A est sorted et B vide
        if np.count_nonzero(~np.isnan(self.B.stack)) == 0 and np.all(self.A.stack[:-1] <= self.A.stack[1:]):
            return (action);
  
        if (np.count_nonzero(~np.isnan(self.B.stack)) > 1):
            action.extend([self.push_b,
                           self.rotate_b,
                           self.inverse_rotate_b,
                           self.swap_b])
          
        if (np.count_nonzero(~np.isnan(self.A.stack)) > 1):
              action.extend([self.push_a,
                           self.rotate_a,
                           self.inverse_rotate_a,
                           self.swap_a])
        
        
        if (np.count_nonzero(~np.isnan(self.A.stack)) > 1 and np.count_nonzero(~np.isnan(self.B.stack)) > 1) :
            action.extend([self.rotate,
                           self.reverse,
                           self.swap])
        
        return action
      
    def balanced(self, size):
      
      # =============== A ==================== #
      # SI il y a trop de Nan
      if delta(self.A.stack.size, size) > 0:
        
        
        divergence = delta(self.A.stack.size, size)
        for i in range(divergence):
            if (np.isnan(self.A.stack[i])):
              self.A.stack = np.delete(self.A.stack, i)
  
      # Si il y a pas assez de Nan
      elif delta(self.A.stack.size, size) < 0:
        
        divergence = abs(delta(self.A.stack.size, size))
        for i in range(divergence):
            self.A.stack = np.insert(self.A.stack, i, np.nan)

      # =============== B ==================== #
      # SI il y a trop de Nan
      if delta(self.B.stack.size, size) > 0:
        divergence = delta(self.B.stack.size, size)
        for i in range(divergence):
            if (np.isnan(self.B.stack[i])):
              self.B.stack = np.delete(self.B.stack, i)
              
      # Si il y a pas assez de Nan  
      elif delta(self.B.stack.size, size) < 0:
        
        divergence = abs(delta(self.B.stack.size, size))
        for i in range(divergence):
            self.B.stack = np.insert(self.B.stack, i, np.nan)
      
      # if self.A.stack.size == size and self.B.stack.size == size :
          # print("balanced ok")
  
      
    
class Moove():

  def __init__(self, A, B, size):
      self.initial_size = size
      self.action = Action(A, B)

  
  def push_b(self, A, B):
        
        # Si A est vide 
        if np.count_nonzero(~np.isnan(A.stack)) == 0:
          return (-5)
        
        if is_sorted(A) and np.full(B, np.nan):
          return (-8)
        
        # ne pas push des nan
        if not np.isnan(A.top):
          B.stack = np.append(B.stack, A.top)
          B.top = A.top
          
          # maj A (supprimer la valeur push, ajouter un nan)
          A.stack = np.delete(A.stack, -1)
          A.stack = np.insert(A.stack, 0, np.nan)
          
          #maj B (supprimer un le nan du debut)
          if np.isnan(B.stack[0]):
            B.stack = np.delete(B.stack, 0) 

        # re-Assigner un nouveux top (si A est vide ou si il ya un elements)
        if np.count_nonzero(~np.isnan(A.stack)) == 0:
          A.top = None
        else:
          A.top = A.stack[-1]
          
        # self.action.balanced(self.initial_size)
        return (-1)
    
  def push_a(self, A, B):
      # Si B est vide 
      if np.count_nonzero(~np.isnan(B.stack)) == 0:
        return (-5)
      
      # ne pas push des nan
      if not np.isnan(B.top):
        A.stack = np.append(A.stack, B.top)
        A.top = B.top
        
        # maj B (supprimer la valeur push, ajouter un nan)
        B.stack = np.delete(B.stack, -1)
        B.stack = np.insert(B.stack, 0, np.nan)
        
        #maj A (supprimer un le nan du debut)
        if np.isnan(A.stack[0]):
          A.stack = np.delete(A.stack, 0) 
        

       # re-Assigner un nouveux top (si B est vide ou si il ya un elements)
      if np.count_nonzero(~np.isnan(B.stack)) == 0:
        B.top = None
      else:
        B.top = B.stack[-1]
        
      # self.action.balanced(self.initial_size)
      return (-1)
  
  def rotate_a(self, A):
    
    # Si A est vide ou n'a qu'un element 
    if np.count_nonzero(~np.isnan(A.stack)) == 0 or np.count_nonzero(~np.isnan(A.stack)) == 1:
      return (-5)
    
    
    nbr = np.isnan(A.stack).sum()
    bot = A.stack[nbr]
    A.stack = np.append(A.stack, bot)
    A.stack = np.delete(A.stack, nbr)
    A.top = A.stack[-1]
    
    self.action.balanced(self.initial_size)
    return (-1)

  def rotate_b(self, B):
    
    # Si B est vide ou n'a qu'un element 
    if np.count_nonzero(~np.isnan(B.stack)) == 0 or np.count_nonzero(~np.isnan(B.stack)) == 1:
      return (-5)
    
    nbr = np.isnan(B.stack).sum()
    bot = B.stack[nbr]
    B.stack = np.append(B.stack, bot)
    B.stack = np.delete(B.stack, nbr)
    B.top = B.stack[-1]
    
    self.action.balanced(self.initial_size)
    return (-1)

  def rotate(self, A, B):
    
    re = 0
    re += self.rotate_a(A)
    re += self.rotate_b(B)
    return re
    

  def inverse_rotate_a(self, A):

    # Si A est vide ou n'a qu'un element 
    if np.count_nonzero(~np.isnan(A.stack)) == 0 or np.count_nonzero(~np.isnan(A.stack)) == 1:
      return (-5)
    
    nbr = np.isnan(A.stack).sum()
    A.stack = np.insert(A.stack, nbr, A.top)
    A.stack = np.delete(A.stack, -1)
    A.top = A.stack[-1]
    
    self.action.balanced(self.initial_size)
    return (-1)
  
  def inverse_rotate_b(self, B):

    # Si B est vide ou n'a qu'un element 
    if np.count_nonzero(~np.isnan(B.stack)) == 0 or np.count_nonzero(~np.isnan(B.stack)) == 1:
      return (-5)

    nbr = np.isnan(B.stack).sum()
    B.stack = np.insert(B.stack, nbr, B.top)
    B.stack = np.delete(B.stack, -1)
    B.top = B.stack[-1]
    
    self.action.balanced(self.initial_size)
    return (-1)

  def reverse(self, A, B):
    
    re = 0
    re += self.inverse_rotate_a(A)
    re += self.inverse_rotate_b(B)
    return re
  
  def swap_a(self, A):
    
      # Si A est vide ou n'a qu'un element 
      if np.isnan(A.stack[-1]) or np.isnan(A.stack[-2]):
        return (-5)

      A.stack[[-1, -2]] =  A.stack[[-2, -1]]
      A.top = A.stack[-1]
      
      # self.action.balanced(self.initial_size)
      return (-1)

  def swap_b(self, B):
    
      # Si B est vide ou n'a qu'un element 
      if np.isnan(B.stack[-1]) or np.isnan(B.stack[-2]):
        return (-5)

      B.stack[[-1, -2]] =  B.stack[[-2, -1]]
      B.top = B.stack[-1]
      
      # self.action.balanced(self.initial_size)
      return (-1)
      
  def swap(self, A, B):
    
    re = 0
    re += self.swap_a(A)
    re += self.swap_b(B)
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