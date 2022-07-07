# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    plot.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ebennace <ebennace@student.42lausanne.c    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/06/08 05:38:41 by ebennace          #+#    #+#              #
#    Updated: 2022/07/07 11:12:56 by ebennace         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt 
import numpy as np


def plot_evolution(episode, number_of_actions, cummulative_reward):
    # plt.style.use('dark_background')
    plt.style.use('seaborn')
    
    fig, ax = plt.subplots(1, 2)
    
    fig.set_figheight(8)
    fig.set_figwidth(20)

    ax[0].plot(episode, number_of_actions, color='red', label='Number of Actions')
    ax[0].legend(loc="upper left")
    ax[0].set_ylabel('Number of Actions')
    ax[0].set_xlabel('Episode')
    
    ax[1].plot(episode, cummulative_reward, color='orange', label='Cumulative Reward')
    ax[1].legend(loc="upper left")
    ax[1].set_ylabel('Cumulative Reward')
    ax[1].set_xlabel('Episode')
    
    # ax[2].plot(episode, epsilon, label='Epsilon')
    # ax[2].legend(loc="upper left") 
    # ax[2].set_ylabel('Value of Epsilon')
    # ax[2].set_xlabel('Episode')
    
    plt.show()