# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    utils_class.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ebennace <ebennace@student.42lausanne.c    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/06/08 05:38:49 by ebennace          #+#    #+#              #
#    Updated: 2022/06/09 05:55:27 by ebennace         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from collections import namedtuple
import random

# def is_sorted(A):
#     for i in range(A.stack.size -1):
#          if A.stack[i+1] > A.stack[i] :
#                return False
#     return True 

def is_sorted(A):
    for i in range(A.stack.size -1):
         if A.stack[i+1] > A.stack[i]:
               return False
    return True 

class ReplayMemory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.memorry = []
        self.nbr_experience = 0
        
    def push(self, experience):
        if len(self.memorry) < self.capacity:
            self.memorry.append(experience)
        else :
            # rewove oldest experience
            self.memorry[self.nbr_experience % self.capacity] = experience
        self.nbr_experience += 1
    
    def get_sample(self, batch_size):
        if batch_size > self.nbr_experience:
            return "Plus assez d'experience"
        return random.sample(self.memorry, batch_size)
    
    def can_provide_sample(self, batch_size):
        return len(self.memorry) >= batch_size
    
    def extract_value(self, experiences):
        
        Experience = namedtuple('Experience', ('state', 'action', 'next_state', 'reward', 'done'))
        
        batch = Experience(*zip(*experiences))
        
        states = np.array([state for state in batch.state])
        actions = np.array([action for action in batch.action])
        next_states = np.array([next_state for next_state in batch.next_state])
        rewards = np.array([reward for reward in batch.reward])
        dones = np.array([done for done in batch.done])
    
        return states, actions, next_states, rewards, dones
    
    def print_history(self, batch_size):
        
        i = 0
        for exp in self.memorry:
            if i > batch_size:
                break
            print(f"Actions : {exp.action} \t Reward : {exp.reward}")
            i += 1
            


class EpsilonGreedy:
    def __init__(self, min, max, decay):
        self.min = min
        self.max = max
        self.decay = decay
        self.epsilon = max
    
    def get_exploration_rate(self, current_step):
        self.epsilon = (self.min + (self.max - self.min)* (np.exp(-self.decay * current_step)))
        return self.epsilon
        