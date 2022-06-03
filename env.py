import numpy as np
from numpy import nan

from tabulate import tabulate
import random
from itertools import zip_longest
from collections import namedtuple
from stack import Stack
from actions import Moove, Action, List_actions
from utils_class import EpsilonGreedy, ReplayMemory, Agent, Experience
from DQN import DQNAgent  



STACK_SIZE = 10

EPISODE = 2
CAPACITY = 100_000
BATCH_SIZE = 64
MIN_REPLAY_MEMORY_SIZE = 100

DECAY = 0.001
START_EPSILON = 1
MIN_EPSILON = 0.15
TARGET_UPDATE = 10

ACTION_REWARD = -1
INVERSE_ACTION_REWARD = -5
FINISH_REWARD = 100

LEARNING_RATE = 0.1
DISCOUNT = 0.95
GAMMA = 0.99


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
        self.agent = DQNAgent(size)
        
        self.current_reward = 0
        self.step = 0
        
        self.exp = Experience()
        self.experience = None
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
       
    def choose_action(self):
        exploration_rate = self.strategy.get_exploration_rate(self.step)
        
        self.step += 1
        
        if (exploration_rate > random.random()):
            #exploration
            self.current_action = np.random.choice(self.actions.possible_actions())
            self.take_actions()
            return self.current_action
        else :
            self.current_action = np.argmax(self.agent.policy_model.predict(self.state))
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
      
    def print_state(self):
        print("---State t---")
        print("-A-\t-B-")
        print("___________\t")
        for a, b in zip_longest(reversed(self.A.stack), reversed(self.B.stack), fillvalue='xxx'):
          
          print(f"|{a}\t{b}|")
        print("___________\t")
    
    def create_experience(self, state_t, action, state_t1, reward):
        return self.exp.create_experience(state_t, action, state_t1, reward)
        
        
    def print_experience(self, experience):
        A_t, B_t = np.split(experience.state, 2, axis=0)
        A_t1, B_t1 = np.split(experience.next_state, 2, axis=0)
        
        A_t = A_t.reshape((A_t.shape[1]))
        B_t = B_t.reshape((B_t.shape[1]))
        
        A_t1 = A_t1.reshape((A_t1.shape[1]))
        B_t1 = B_t1.reshape((B_t1.shape[1]))
        
        print("---State t---\t\t---State t+1---")
        print("-A-\t-B-\t\t-A-\t-B-")
        print("___________\t\t___________")
        for a_t, b_t, a_t1, b_t1 in zip_longest(reversed(A_t), reversed(B_t), reversed(A_t1), reversed(B_t1)):
          
          print(f"|{a_t}\t{b_t}|\t\t|{a_t1}\t{b_t1}|")
        print("___________\t\t___________")
        print("----------------------------------")
        print(f"\tAction [{experience.action}]")
        print(f"\tReward [{experience.reward}]")
        print("----------------------------------")