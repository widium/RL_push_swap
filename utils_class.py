import numpy as np
from collections import namedtuple
import random
from itertools import zip_longest
        
def print_experience(experience):
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
            
    def print_buffer(self, experiences):
        print("========== BUFFER ==========")
        for i in experiences:
            print_experience(i)
        print(f"========== [{len(experiences)} experience ] ==========")
            


class EpsilonGreedy:
    def __init__(self, min, max, decay):
        self.min = min
        self.max = max
        self.decay = decay
    
    def get_exploration_rate(self, current_step):
        return (self.min + (self.max - self.min)*
                (np.exp(-self.decay * current_step)))