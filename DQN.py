import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from stack import Stack
from constant import *

class DQNAgent:
  def __init__(self, state, actions_space):

    #policy model
    # train every steps
    self.policy_model = self.create_model(state, actions_space)

    #target model
    #.predict() every steps
    self.target_model = self.create_model(state, actions_space)
    self.target_model.set_weights(self.policy_model.get_weights())

    self.target_update_counter = 0


  def create_model(self, state, actions_space):
    model = Sequential()
    model.add(Dense(100, activation='relu', input_dim=state))
    model.add(Dense(actions_space, activation="softmax"))
    model.compile(optimizer='adam', loss='mae')
    return model

  
  def get_Q_value(self, state, step):
    return self.policy_model.predict(np.array(state))

  def train(self, states, next_states, experiences):
    
    print(states.shape)
    # print(next_states)
    ##--------Recuperer toutes les Q values des 2 model-----##
    Q_policy_list = self.policy_model.predict(states)
    Q_target_list = self.target_model.predict(next_states)
    
    
    X = []
    y = []

    ##--------Creer X et Y pour l'entrainement du model-----##
    for t, (state, action, next_state, reward) in enumerate(experiences):
      
      #tant que c'est pas la dernier q value
      #calculer la q value actuel avec la belman equation
      if t < BATCH_SIZE:
        
        #recuperer la max Q_target & calculer sa Qvalue a linstant t
        max_Q_target = np.max(Q_target_list[t])
        max_Q_value = reward + GAMMA * max_Q_target
      
      #si c'est la derniere q value on lui assigne un reward
      else :
        max_Q_value = reward

      #recuperer les Q value a l'instant t [11]
      Q_target = Q_policy_list[t]
      #assigner la meilleur actions  [1]
      Q_target[action] = max_Q_value

      #Ajouter les State dans X
      #Ajouter les Q_value avec l'argmax.
      X.append(state)
      y.append(Q_target)

    self.policy_model.fit(np.array(X), np.array(y), batch_size=BATCH_SIZE, verbose=1, shuffle=False) 

    target_update_counter += 1

    # If counter reaches set value, update target network with weights of main network
    self.target_model.set_weights(self.policy_model.get_weights())