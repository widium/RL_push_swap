import numpy as np
from numpy import nan

from tabulate import tabulate
import random
from itertools import zip_longest
from collections import namedtuple
from stack import Stack
from actions import Moove, Action, List_actions
from utils_class import EpsilonGreedy, ReplayMemory
from DQN import DQNAgent  
from constant import *


class Env:
    
    
    def __init__(self, size):
        self.A = Stack(size, 0)
        self.B = Stack(size, 1)
        self.size = size
        self.state_t = np.vstack((self.A.stack, self.B.stack))
        
        self.moover = Moove(self.A, self.B, size)
        self.actions = Action(self.A, self.B)
        self.liste = List_actions()
        self.current_action = 1;
        # self.agent = Agent(EpsilonGreedy(MIN_EPSILON, MAX_EPSILON, DECAY), 11)
        self.strategy = EpsilonGreedy(MIN_EPSILON, START_EPSILON, DECAY)
        
        self.current_reward = 0
        self.step = 0
        
        self.replaymemory = ReplayMemory(CAPACITY)
    
    def reset(self, size):
        self.A = Stack(size, 0)
        self.B = Stack(size, 1)
        self.state_t = np.vstack((self.A.stack, self.B.stack))
        
    def state(self):
        if self.B.stack.size == 0 and np.all(self.A.stack[:-1] <= self.A.stack[1:]):
            return 'done'
        return np.vstack((self.A.stack, self.B.stack))
        
    def actions_available(self):
        return self.actions.possible_actions()
    
    def reward(self):
        if self.B.stack.size == 0 and np.all(self.A.stack[:-1] <= self.A.stack[1:]):
            self.current_reward += 100
        reward_tmp = self.current_reward
        self.current_reward = 0
        return (reward_tmp)
    
    def take_actions(self):
        
        self.liste.add(self.current_action)
        self.current_reward += self.liste.compare()
        
        if self.current_action == 0:
            self.current_reward += self.moover.push_b(self.A, self.B)
            
        elif self.current_action == 1:
            self.current_reward += self.moover.push_a(self.A, self.B)
            
        elif self.current_action == 2:
            self.current_reward += self.moover.rotate_b(self.B)
            
        elif self.current_action == 3:
            self.current_reward += self.moover.rotate_a(self.A)
            
        elif self.current_action == 4:
            self.current_reward += self.moover.inverse_rotate_b(self.B)
            
        elif self.current_action == 5:
            self.current_reward += self.moover.inverse_rotate_a(self.A)
            
        elif self.current_action == 6:
           self.current_reward += self.moover.swap_b(self.B)
            
        elif self.current_action == 7:
            self.current_reward += self.moover.swap_a(self.A)
            
        elif self.current_action == 8:
           self.current_reward += self.moover.rotate(self.A, self.B)
            
        elif self.current_action == 9:
            self.current_reward += self.moover.reverse(self.A, self.B)
            
        elif self.current_action == 10:
            self.current_reward += self.moover.swap(self.A, self.B)
       
    def choose_action(self, policy_model):
        exploration_rate = self.strategy.get_exploration_rate(self.step)
        
        self.step += 1
        
        if (exploration_rate > random.random()):
            #exploration
            self.current_action = np.random.choice(self.actions.possible_actions())
            self.take_actions()
            return self.current_action
        else :
            self.current_action = np.argmax(policy_model.predict(self.state))
            self.take_actions()
            return self.current_action
    
    

    def action_space(self):
      return np.array([0,
                       1,
                       2,
                       3,
                       4,
                       5,
                       6,
                       7,
                       8,
                       9,
                       10])
    
    def create_experience(self, state_t, action, state_t1, reward):
        Experience = namedtuple(
                'Experience', ('state', 'action', 'next_state', 'reward'))
        return Experience(state_t, action, state_t1, reward)