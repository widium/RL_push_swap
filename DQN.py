import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from stack import Stack
from utils_class import ReplayMemory


test = 1
BATCH_SIZE = 64
MIN_REPLAY_MEMORY_SIZE = 100
GAMMA = 0.99

class DQNAgent:
  def __init__(self, size):

    #policy model
    # train every steps
    self.policy_model = self.create_model()

    #target model
    #.predict() every steps
    self.target_model = self.create_model()
    self.target_model.set_weights(self.policy_model.get_weights())

    self.replay_memory = ReplayMemory(size)
    self.target_update_counter = 0


  def create_model(self):
    model = Sequential()
    model.add(Dense(100, activation='relu', input_dim=1))
    model.add(Dense(11, activation="softmax"))
    model.compile(optimizer='adam', loss='mae')
    return model

  def update_replay_memory(self, experience):
    self.replay_memory.push(experience)
  
  def get_Q_value(self, state, step):
    return self.policy_model.predict(np.array(state))

  def train(self, state_t, step):
    # Si il n'y a pas de memory
    if len(self.replay_memory) < MIN_REPLAY_MEMORY_SIZE:
      return
 
    #checker si il ya asser d'experience fournir un batch
    if self.replay_memory.get_provide_sample(self, BATCH_SIZE):
      minibatch = self.replay_memory.get_sample(BATCH_SIZE)

      ##-------Recuperer en Avance tous les Q value------###

      #calculer toute les Q_t dans le batch avec tous les state_t
      state_t = np.array([experience[0] for experience in minibatch])
      Q_policy_list = self.policy_model.predict(state_t)

      #calculer toute les Q_nex dans le batch avec tous les state_t+1
      state_next = np.array([experience[2] for experience in minibatch])
      Q_target_list = self.target_model.predict(state_next)
    
    X = []
    y = []

    ##--------Creer X et Y pour l'entrainement du model-----##
    for i, (state_t, action, reward, state_next) in enumerate(minibatch):
      #tant que c'est pas la dernier q value
      #calculer la q value actuel avec la belman equation
      if i < BATCH_SIZE:
        #recuperer la max Qvalue a linstant i
        max_Q_target = np.max(Q_target_list[i])
        max_Q_value = reward + GAMMA * max_Q_target
      
      #si c'est la derniere q value on lui assigne un reward
      else :
        max_Q_value = reward

      #recuperer les Q value a l'instant t 
      Q_target = Q_policy_list[i]
      #assigner la meilleur actions 
      Q_target[action] = max_Q_value

      #Ajouter les State dans X
      #Ajouter les Q_value avec l'argmax.
      X.append(state_t)
      y.append(Q_target)

    self.policy_model.fit(np.array(X), np.array(y), batch_size=BATCH_SIZE, verbose=1, shuffle=False) 

    self.target_update_counter += 1

    # If counter reaches set value, update target network with weights of main network
    self.target_model.set_weights(self.policy_model.get_weights())