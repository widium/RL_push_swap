# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    verbose.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ebennace <ebennace@student.42lausanne.c    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/06/07 06:34:16 by ebennace          #+#    #+#              #
#    Updated: 2022/06/20 06:00:50 by ebennace         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from ast import arg
import numpy as np
from itertools import zip_longest
from actions import possible_actions

def name_action(action):
    if action == 0:
        return "push_b"
    elif action == 1:
        return "push_a"
    elif action == 2:
        return "rotate_b"
    elif action == 3:
        return "rotate_a"
    elif action == 4:
        return "inverse_rotate_b"
    elif action == 5:
        return "inverse_rotate_a"
    elif action == 6:
        return "swap_b"
    elif action == 7:
        return "swap_a"
    elif action == 8:
        return "rotate"
    elif action == 9:
        return "reverse"
    elif action == 10:
        return "swap"

def print_action_available(env):
    actions = possible_actions(env.A, env.B)
    print("=== Actions available ===")
    for a in actions:
        print(f"{name_action(a)}")
    print("=============")

def print_shapes(state, next_state):
    print(f" State shape : {state.shape}")
    print(f" Next State shape : {next_state.shape}")
    

def print_state(env, shape=False):
    
    A = env.A.stack.reshape((env.A.stack.shape[0]))
    B = env.B.stack.reshape((env.B.stack.shape[0]))
    
    print("---State t---")
    print("-A-\t-B-")
    print("___________\t")
    for a, b in zip_longest(A, B, fillvalue='xxx'):
        
        print(f"|{a}\t{b}|")
    print("___________\t")
    if (shape == True):
        print(f"A shape : {env.A.stack.shape}")
        print(f"B shape : {env.B.stack.shape}")
        print("___________\t")
    print("------------")   
    print(f"Env : {env.state()}")
    print("------------")
    
    
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
    print(f"\tAction [{name_action(experience.action)}]")
    print(f"\tReward [{experience.reward}]")
    print("----------------------------------")
    if experience.done:
        print("----------------------------------")
        print(f"\t Last State Done = {experience.done}")
        print("----------------------------------")

def print_buffer(buffer):
    
    print("========== BUFFER ==========")
    for i in buffer:
        print_experience(i)
    print(f"========== [{len(buffer)} experience ] ==========")
    
def print_interaction(epsilon, action, reward):
    print("----------------------------------")
    print(f"Action : [{name_action(action)}]")
    print(f"Reward : [{reward}]")
    # print(f"Epsilon : [{epsilon}]")
    print("----------------------------------")
    
def print_cummulative_reward(env):
    print("----------------------------------")
    print(f"Cumulative Reward [{env.cummulative_reward}]")
    print("----------------------------------")
    
    
def print_vector(vector):
    max = ' '
    i = 0
    arg_max = np.argmax(vector)
    print(f"Argmax -> {arg_max}")
    vector = vector.reshape((vector.shape[1]))
    print("--- Vector of Actions ---")
    print("___________\t")
    for a in vector:
        if i == arg_max:
            max = f"-> argmax : [{name_action(i)}]"
        else :
            max = ' '
        
        print(f"|{a}|{max}")
        i+= 1
    print("___________\t")