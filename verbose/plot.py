# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    plot.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ebennace <ebennace@student.42lausanne.c    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/06/08 05:38:41 by ebennace          #+#    #+#              #
#    Updated: 2022/06/20 11:32:05 by ebennace         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt 
import numpy as np


def plot_evolution(episode_duration, cummulative_reward, epsilon):
    plt.style.use('dark_background')
    
    fig, ax = plt.subplots(1, 3)
    
    fig.set_figheight(8)
    fig.set_figwidth(20)

    ax[0].plot(episode_duration, 'r', label='Number of Actions')
    ax[0].legend(loc="upper right")
    ax[0].set_ylabel('Number of Actions')
    ax[0].set_xlabel('Episode')
    
    ax[1].plot(cummulative_reward, 'b', label='Cumulative Reward')
    ax[1].legend(loc="upper right")
    ax[1].set_ylabel('Cumulative Reward')
    ax[1].set_xlabel('Episode')
    
    ax[2].plot(epsilon, 'o', label='Epsilon')
    ax[2].legend(loc="upper right") 
    ax[2].set_ylabel('Value of Epsilon')
    ax[2].set_xlabel('Episode')
    
    plt.show()