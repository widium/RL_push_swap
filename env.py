# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    env.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ebennace <ebennace@student.42lausanne.c    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/06/08 05:38:54 by ebennace          #+#    #+#              #
#    Updated: 2022/06/08 08:19:21 by ebennace         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from numpy import nan

import random
from collections import namedtuple
from stack import Stack
from actions import Moove, Action, List_actions
from utils_class import EpsilonGreedy, ReplayMemory, is_sorted
from constant import *
from pre_processing import Normalize, pre_processing_state
from sklearn.preprocessing import MinMaxScaler


class Env:
    
    
    def __init__(self, size):
        self.A = Stack(size, empty=False)
        self.B = Stack(size, empty=True)
        self.size = size
        self.matrice = None
        # self.scaler = Normalize()
        # self.scaler = MinMaxScaler(feature_range=(0, 1))
        # self.A.stack = self.scaler.fit_transform(self.A.stack)
        
        self.moover = Moove(self.A, self.B, size)
        self.actions = Action(self.A, self.B)
        self.liste = List_actions()
        self.current_action = 1;
        
        self.cummulative_reward = 0
        self.current_reward = 0
        self.step = 0
        
        self.replaymemory = ReplayMemory(CAPACITY)
    
    def reset(self, size):
        self.A = Stack(size, empty=False)
        self.B = Stack(size, empty=True)
        # self.A.stack = self.scaler.fit_transform(self.A.stack)
        # self.A = self.scaler.transform(self.A.stack)

        self.cummulative_reward = 0
        self.current_reward = 0
        
    def state(self):
        if is_sorted(self.A) and np.count_nonzero(~np.isnan(self.B.stack)) == 0:
            return 'done'
        return 'in progress'

    def get_state(self):
        self.matrice = np.vstack((self.A.stack, self.B.stack))
        return self.matrice
    
    def actions_available(self):
        return self.actions.possible_actions()
    
    def reward(self):
        if is_sorted(self.A) and np.count_nonzero(~np.isnan(self.B.stack)) == 0:
            self.current_reward += 100
        
        #add to cummulative reward
        self.cummulative_reward += self.current_reward
        
        # paste in tmp for reset and return reward
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
            self.current_reward += self.moover.rotate_b(self.A, self.B)
            
        elif self.current_action == 3:
            self.current_reward += self.moover.rotate_a(self.A, self.B)
            
        elif self.current_action == 4:
            self.current_reward += self.moover.inverse_rotate_b(self.A, self.B)
            
        elif self.current_action == 5:
            self.current_reward += self.moover.inverse_rotate_a(self.A, self.B)
            
        elif self.current_action == 6:
           self.current_reward += self.moover.swap_b(self.A, self.B)
            
        elif self.current_action == 7:
            self.current_reward += self.moover.swap_a(self.A, self.B)
            
        elif self.current_action == 8:
           self.current_reward += self.moover.rotate(self.A, self.B)
            
        elif self.current_action == 9:
            self.current_reward += self.moover.reverse(self.A, self.B)
            
        elif self.current_action == 10:
            self.current_reward += self.moover.swap(self.A, self.B)
       
    def choose_action(self, state, policy_model, exploration_rate):
        
        if (exploration_rate > random.random()):
            print("Exploration")
            #exploration
            self.current_action = np.random.choice(self.actions.possible_actions())
            self.take_actions()
            return self.current_action
        else :
            print("Exploitation")
            state = pre_processing_state(state)
            self.current_action = np.argmax(policy_model.predict(state))
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
    
    def create_experience(self, state, action, next_state, reward):
        Experience = namedtuple(
                'Experience', ('state', 'action', 'next_state', 'reward', 'done'))
        
        if (self.state() == 'done') :
            done = 1
        else :
            done = 0
        
        return Experience(state, action, next_state, reward, done)