import numpy as np
from collections import namedtuple


Experience = namedtuple(
    'Experience', ('state', 'action', 'next_state', 'reward')) 


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