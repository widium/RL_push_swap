
import numpy as np

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
      if delta(self.A.stack.size, size) > 0:
        
        divergence = delta(self.A.stack.size, size)
        for i in range(divergence):
            # print("rm nan in A")
            if (np.isnan(self.A.stack[i])):
              self.A.stack = np.delete(self.A.stack, i)
  
        
      elif delta(self.A.stack.size, size) < 0:
        
        divergence = abs(delta(self.A.stack.size, size))
        for i in range(divergence):
            # print("add nan in A")
            self.A.stack = np.insert(self.A.stack, i, np.nan)

      # ===============B==================== #
      if delta(self.B.stack.size, size) > 0:
        # print(f"B = {self.B.stack.size} , Size = {size} --> supprimer des nan B")
        divergence = delta(self.B.stack.size, size)
        for i in range(divergence):
            # print("rm nan in B")
            if (np.isnan(self.B.stack[i])):
              self.B.stack = np.delete(self.B.stack, i)
        
      elif delta(self.B.stack.size, size) < 0:
        
        divergence = abs(delta(self.B.stack.size, size))
        for i in range(divergence):
            # print("add nan in B")
            self.B.stack = np.insert(self.B.stack, i, np.nan)
      
      # if self.A.stack.size == size and self.B.stack.size == size :
          # print("balanced ok")
        

def delta(A_size, size):
  return (A_size - size)


  
  # if A.stack.size > size:
  #   print("A possede trop de nan")
  # if B.stack.size > size :
  #   print("B possede trop de nan")
  # if A.stack.size > B.stack.size :
  #   print("il manque des nan dans B")
  # if B.stack.size > A.stack.size :
  #   print("il manque des nan dans A")
  
      
    
class Moove():

  def __init__(self, A, B, size):
      self.reward = 0;
      self.A = A
      self.B = B
      self.initial_size = size

  
  def push_b(self):
        # Si A est vide 
        if not self.A.stack.size:
          return
        # ne pas push des nan
        if not np.isnan(self.A.top):
          self.B.stack = np.append(self.B.stack, self.A.top)
          self.A.stack = np.delete(self.A.stack, -1)
          self.B.top = self.A.top

        # Si A est vide maintenant
        if not self.A.stack.size:
          self.A.top = None
        else:
          self.A.top = self.A.stack[-1]
        self.reward -= 1
        # balanced(self.A, self.B, self.initial_size)
    
  def push_a(self):
      # Si B est vide 
      if not self.B.stack.size:
        return
      # ne pas push des nan
      if not np.isnan(self.B.top):
        self.A.stack = np.append(self.A.stack, self.B.top)
        self.B.stack = np.delete(self.B.stack, -1)
        self.A.top = self.B.top

      # Si B est vide maintenant
      if not self.B.stack.size:
        self.B.top = None
      else:
        self.B.top = self.B.stack[-1]
      self.reward -= 1
  
  def rotate_a(self):
    
    # Si A est vide ou n'a qu'un element 
    if not self.A.stack.size or self.A.stack.size == 1:
      return

    self.A.stack = np.roll(self.A.stack, 1)
    self.A.top = self.A.stack[-1]
    self.reward -= 1

  def rotate_b(self):
    
    # Si B est vide ou n'a qu'un element 
    if not self.B.stack.size or self.B.stack.size == 1:
      return
    
    self.B.stack = np.roll(self.B.stack, 1)
    self.B.top = self.B.stack[-1]
    self.reward -= 1

  def rotate(self):
    
    self.rotate_a()
    self.rotate_b()

  def inverse_rotate_a(self):

    # Si A est vide ou n'a qu'un element 
    if not self.A.stack.size or self.A.stack.size == 1:
      return
    
    self.A.stack = np.roll(self.A.stack, -1)
    self.A.top = self.A.stack[-1]
    self.reward -= 1
  
  def inverse_rotate_b(self):

    # Si B est vide ou n'a qu'un element 
    if not self.B.stack.size or self.B.stack.size == 1:
      return

    self.B.stack = np.roll(self.B.stack, -1)
    self.B.top = self.B.stack[-1]
    self.reward -= 1

  def reverse(self):
    
    self.inverse_rotate_a()
    self.inverse_rotate_b()
  
  def swap_a(self):
      # Si A est vide ou n'a qu'un element 
      if not self.A.stack.size or self.A.stack.size == 1:
        return

      self.A.stack[[-1, -2]] =  self.A.stack[[-2, -1]]
      self.A.top = self.A.stack[-1]
      self.reward -= 1

  def swap_b(self):
    
      # Si B est vide ou n'a qu'un element 
      if not self.B.stack.size or self.B.stack.size == 1:
        return
    
      self.B.stack[[-1, -2]] =  self.B.stack[[-2, -1]]
      self.B.top = self.B.stack[-1]
      self.reward -= 1
      
  def swap(self):
    
    self.swap_a()
    self.swap_b()