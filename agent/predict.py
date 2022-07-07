# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    predict.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ebennace <ebennace@student.42lausanne.c    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/07/07 11:21:35 by ebennace          #+#    #+#              #
#    Updated: 2022/07/07 14:09:31 by ebennace         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from asyncio import FastChildWatcher
import numpy as np

from agent.DQN import DQNAgent
from environnement.env import Env
from verbose.verbose import print_state
from environnement.pre_processing import pre_processing_state, denormalize_vector

from verbose.verbose import print_vector, print_list_action


def predict_sort(env : Env, agent : DQNAgent, verbose : bool = False ):
    
    list_actions = list()
    
    if (verbose == True):
        print_state(env)
    
    while (1):
        
        state = env.get_state()
        state = pre_processing_state(state)
        
        vector = agent.policy_model.predict(state)
        
        env.current_action = np.argmax(vector)
        action_name = plot_action(env.current_action)
        list_actions.append(action_name)
        env.take_actions()
        
        if (verbose == True):
            print_vector(vector)
            print_state(env)
        
        if (env.state() == 'done'):
            
            if (verbose == True):
                print_list_action(list_actions)
            
            else :
                for action in list_actions:
                    print(action)
    
            break
        

def plot_action(current_action : int):
    if current_action == 0:
        return "pb"
    elif current_action == 1:
        return "pa"
    elif current_action == 2:
        return "rb"
    elif current_action == 3:
        return "ra"
    elif current_action == 4:
        return "rrb"
    elif current_action == 5:
        return "rra"
    elif current_action == 6:
        return "sb"
    elif current_action == 7:
        return "sa"
    elif current_action == 8:
        return "rr"
    elif current_action == 9:
        return "rrr"
    elif current_action == 10:
        return "ss"  