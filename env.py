import numpy as np
from numpy import nan

from tabulate import tabulate
import random
from itertools import zip_longest 
from collections import namedtuple
from stack import Stack
from actions import Moove, Action
from utils_class import EpsilonGreedy, ReplayMemory, Agent



EPISODE = 2500
DECAY = 0.998
MAX_EPSILON = 0.9
MIN_EPSILON = 0.15
ACTION_REWARD = -1
FINISH_REWARD = 100
LEARNING_RATE = 0.1
DISCOUNT = 0.95
STACK_SIZE = 10
BATCH_SIZE = 64
MIN_REPLAY_MEMORY_SIZE = 100
GAMMA = 0.99




class Env:
    
    def __init__(self, size):
        self.A = Stack(size)
        self.B = Stack(0)
        self.moover = Moove(self.A, self.B)
        self.actions = Action(self.A, self.B)
        self.current_action = 0;
        # self.agent = Agent(EpsilonGreedy(MIN_EPSILON, MAX_EPSILON, DECAY), 11)
        self.strategy = EpsilonGreedy(MIN_EPSILON, MAX_EPSILON, DECAY)
        self.agent = DQNAgent(size)
        self.cum_reward = self.moover.reward
        self.step = 0
    
        
    def state(self):
        return (self.A.stack, self.B.stack)
    
    def reset(self, size):
        self.A = Stack(size)
        self.B = Stack(0)
        
    def actions_available(self):
        return self.actions.possible_actions()
    
    def reward(self):
        if self.B.stack.size == 0 and np.all(self.A.stack[:-1] <= self.A.stack[1:]):
             self.cum_reward += 100
        return (self.cum_reward)
        
    def choose_action(self):
        exploration_rate = self.strategy.get_exploration_rate(self.step)
        
        self.step += 1
        
        if (exploration_rate > random.random()):
            #exploration
            self.current_action = np.random.choice(self.actions.possible_actions())
            return self.current_action
        else :
            return self.actions.possible_actions()
        
    def take_actions(self):
        if self.current_action == 0:
            self.moover.push_b()
        if self.current_action == 1:
            self.moover.push_a()
        if self.current_action == 2:
            self.moover.rotate_b()
        if self.current_action == 3:
            self.moover.rotate_a()
        if self.current_action == 4:
            self.moover.inverse_rotate_b()
        if self.current_action == 5:
            self.moover.inverse_rotate_a()
        if self.current_action == 6:
            self.moover.swap_b()
        if self.current_action == 7:
            self.moover.swap_a()
        if self.current_action == 8:
            self.moover.rotate()
        if self.current_action == 9:
            self.moover.reverse()
        if self.current_action == 10:
            self.moover.swap()
        
    
    def print_stack(self):
        print("-------------------")
        for a, b in zip_longest(reversed(self.A.stack), reversed(self.B.stack), fillvalue='xxx'):
          
          print(f"{a}\t{b}")
        print("-------------------")