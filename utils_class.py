# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    utils_class.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ebennace <ebennace@student.42lausanne.c    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/06/08 05:38:49 by ebennace          #+#    #+#              #
#    Updated: 2022/06/20 09:28:45 by ebennace         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from collections import namedtuple
import random


def is_sorted(A : np.ndarray):
    for i in range(A.size -1):
         if A[i+1] > A[i]:
               return False
    return True 

def is_finish(A : np.ndarray, B : np.ndarray):
    if is_sorted(A) and np.count_nonzero(B) == 0:
        return True
    else :    
        return False
    
def is_empty(A : np.ndarray):
    if (np.count_nonzero(A) == 0):
        return True
    else :
        return False
    
def top_is_empty(A : np.ndarray):
    if A[0] == 0:
        return True
    else :
        return False
    
def less_than_two_element(A : np.ndarray):
    if (np.count_nonzero(A) < 2):
        return True
    else :
        return False
    
def index_of_bot(A : np.ndarray):
    return -(np.count_nonzero(A == 0))

def get_bot(A : np.ndarray):
    index_bot = index_of_bot(A)
    return (A[index_bot - 1])
    

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
        