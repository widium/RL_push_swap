import numpy as np
from collections import namedtuple
import random


class Experience:
    
    def __init__(self):
        self.tuple = namedtuple(
                'Experience', ('state', 'action', 'next_state', 'reward'))
        
    def create_experience(self, state, action, next_state, reward):
        return self.tuple(state, action, next_state, reward)
        
        
        
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


class Agent:
    def __init__(self, epsilongreedy, num_actions):
        self.step = 0
        self.epsilongreedy = epsilongreedy
        self.num_actions = num_actions
    
    def select_action(self, state, policy_network):
        exploration_rate = self.epsilongreedy.get_exploration_rate(self.step)
        self.step += 1
        
        if (exploration_rate > random.random()):
            #exploration
            return random.randrange(self.num_actions)
        else :
            return policy_network.predict(state).argmax()