
import numpy as np

class Action():
    
    def __init__(self, A, B):
        
        self.push_a = "push_a"
        self.push_b = "push_b"
        self.rotate_a = "rotate_a"
        self.rotate_b = "rotate_b"
        self.rotate = "rotate"
        self.inverse_rotate_a = "inverse_rotate_a"
        self.inverse_rotate_b = "inverse_rotate_b"
        self.reverse = "reverse"
        self.swap_a = "swap_a"
        self.swap_b = "swap_b"
        self.swap = "swap"
        self.A = A
        self.B = B
    
        
        # self.actions_space = len(self.action)
        
    def  A_is_full(self):
        if self.A.stack.size != 0 and self.B.stack.size == 0:
            return (1)
        else :
            return (0)
        
    def  B_is_full(self):
            if self.B.stack.size != 0 and self.A.stack.size == 0:
                return (1)
            else :
                return (0)
            
    def possible_actions(self):
        action = list()
        # Si la Stack A est sorted et B vide
        if self.B.stack.size == 0 and np.all(self.A.stack[:-1] <= self.A.stack[1:]):
            pass
        
        # Si A et plein et que B et vide 
        elif (A_is_full() == 1):
            action.extend([self.push_b,
                           self.rotate_b,
                           self.inverse_rotate_b,
                           self.swap_b])

        # Si B et plein et que A et vide
        elif (B_is_full() == 1):
            action.extend([self.push_a,
                           self.rotate_a,
                           self.inverse_rotate_a,
                           self.swap_a])

        
        elif self.A.stack.size == 1:
            action.append([self.push_a])

        elif self.B.stack.size == 1:
            action.append([self.push_b])
            
        else :
            action.extend([self.push_a, 
                           self.push_b, 
                           self.rotate_a, 
                           self.rotate_b,
                           self.rotate,
                           self.inverse_rotate_a,
                           self.inverse_rotate_b,
                           self.reverse,
                           self.swap_a,
                           self.swap_b,
                           self.swap])
        
        return action

    
    
    
class Moove():

  def __init__(self, A, B):
      self.A = A
      self.B = B

  
  def push_a(self):
        # Si A est vide 
        if not self.A.stack.size:
          return
        self.B.stack = np.append(self.B.stack, self.A.top)
        self.A.stack = np.delete(self.A.stack, -1)
        self.B.top = self.A.top

        # Si A est vide maintenant
        if not self.A.stack.size:
          self.A.top = None
        else:
          self.A.top = self.A.stack[-1]
    
  def push_b(self):
      # Si B est vide 
      if not self.B.stack.size:
        return
      # Si A est vide
      if not self.A.stack.size :
        self.A.stack = np.append(self.A.stack, self.B.top)
        self.B.stack = np.delete(self.B.stack, -1)
        self.A.top = self.B.top

      # Si B est vide maintenant
      if not self.B.stack.size:
        self.B.top = None
      else:
        self.B.top = self.B.stack[-1]
  
  def rotate_a(self):
    
    # Si A est vide ou n'a qu'un element 
    if not self.A.stack.size or self.A.stack.size == 1:
      return

    self.A.stack = np.roll(self.A.stack, 1)
    self.A.top = self.A.stack[-1]

  def rotate_b(self):
    
    # Si B est vide ou n'a qu'un element 
    if not self.B.stack.size or self.B.stack.size == 1:
      return
    
    self.B.stack = np.roll(self.B.stack, 1)
    self.B.top = self.B.stack[-1]

  def rotate(self):
    
    self.rotate_a()
    self.rotate_b()

  def inverse_rotate_a(self):

    # Si A est vide ou n'a qu'un element 
    if not self.A.stack.size or self.A.stack.size == 1:
      return
    
    self.A.stack = np.roll(self.A.stack, -1)
    self.A.top = self.A.stack[-1]
  
  def inverse_rotate_b(self):

    # Si B est vide ou n'a qu'un element 
    if not self.B.stack.size or self.B.stack.size == 1:
      return

    self.B.stack = np.roll(self.B.stack, -1)
    self.B.top = self.B.stack[-1]

  def reverse(self):
    
    self.inverse_rotate_a()
    self.inverse_rotate_b()
  
  def swap_a(self):
      # Si A est vide ou n'a qu'un element 
      if not self.A.stack.size or self.A.stack.size == 1:
        return

      self.A.stack[[-1, -2]] =  self.A.stack[[-2, -1]]
      self.A.top = self.A.stack[-1]

  def swap_b(self):
    
      # Si B est vide ou n'a qu'un element 
      if not self.B.stack.size or self.B.stack.size == 1:
        return
    
      self.B.stack[[-1, -2]] =  self.B.stack[[-2, -1]]
      self.B.top = self.B.stack[-1]
      
  def swap(self):
    
    self.swap_a()
    self.swap_b()