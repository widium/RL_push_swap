import numpy as np
from collections import namedtuple
import random
        
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
        
        Experience = namedtuple('Experience', ('state', 'action', 'next_state', 'reward'))
        
        batch = Experience(*zip(*experiences))
        
        state = np.array([state for state in batch.state])
        action = np.array([action for action in batch.action])
        next_state = np.array([next_state for next_state in batch.next_state])
        reward = np.array([reward for reward in batch.reward])
    
        return state, action, next_state, reward
    
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
    
    def get_exploration_rate(self, current_step):
        return (self.min + (self.max - self.min)*
                (np.exp(-self.decay * current_step)))