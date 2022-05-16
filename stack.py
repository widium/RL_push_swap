import numpy as np
from collections import namedtuple
import random


class Stack():

  def __init__(self, size):

      if size > 0 :
        self.stack = np.arange(size)
        self.top = self.stack[-1]
      else :
        self.stack = np.array([])
        self.top = None
