import numpy as np
from collections import namedtuple
import random


class Stack():

  def __init__(self, size, empty):

      if empty == 0 :
        self.stack = np.random.choice(range(100), size, replace=False)
        self.top = self.stack[-1]
      else :
        self.stack = np.full(size, np.nan)
        self.top = None
