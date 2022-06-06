import numpy as np
from keras.models import Sequential
from keras.layers import Conv1D, MaxPooling1D, Flatten
from keras.layers import Dense
from constant import *

class DQNAgent:
  def __init__(self, n_steps, features, actions_space):

    #policy model
    # train every steps
    self.policy_model = self.create_model(n_steps, features, actions_space)

    #target model
    #.predict() every steps
    self.target_model = self.create_model(n_steps, features, actions_space)
    self.target_model.set_weights(self.policy_model.get_weights())

    self.target_update_counter = 0


  def create_model(self, n_steps, features, actions_space):
    
    model = Sequential()
    model.add(Conv1D(64, 2, activation='relu', input_shape=(n_steps, features)))
    model.add(MaxPooling1D(data_format="channels_first"))
    model.add(Flatten())
    model.add(Dense(50, activation='relu'))
    model.add(Dense(actions_space))
    model.compile(optimizer='adam', loss='mae')
    return model

  
  def get_Q_value(self, state):
    return self.policy_model.predict(np.array(state))

  def train(self, states, next_states, buffer):
    
    ##--------Recuperer toutes les Q values des 2 model-----##
    Q_policy_list = self.policy_model.predict(states)
    Q_target_list = self.target_model.predict(next_states)
    
    #==== compute value function ====#
    X, Y = value_function(buffer, Q_target_list, Q_policy_list)
    
    #==== Fit and compute loss ====#
    self.policy_model.fit(X, Y, batch_size=BATCH_SIZE, verbose=1, shuffle=False) 

    # ==== Update Target Model ====#
    self.target_model.set_weights(self.policy_model.get_weights())
    self.target_update_counter += 1
    

def value_function(buffer, Q_target_list, Q_policy_list):
  
    X = list()
    y = list()

    ##--------Creer X et Y pour l'entrainement du model-----##
    for t, (state, action, next_state, reward) in enumerate(buffer):
      
      #tant que c'est pas la dernier q value
      #calculer la q value actuel avec la belman equation
      
      if not state == 'done':
        #recuperer la max Q_target & calculer sa Qvalue a linstant t
        max_Q_target = np.max(Q_target_list[t])
        max_Q_value = reward + GAMMA * max_Q_target
      
      #si c'est la derniere q value on lui assigne un reward
      elif (next_state == 'done') :
        max_Q_value = reward

      #recuperer les Q value a l'instant t [11]
      Q_target = Q_policy_list[t]
      #assigner la meilleur actions  [1]
      Q_target[action] = max_Q_value

      #Ajouter les State dans X
      #Ajouter les Q_value avec l'argmax.
      X.append(state)
      y.append(Q_target)
    
    return np.array(X), np.array(y)
  