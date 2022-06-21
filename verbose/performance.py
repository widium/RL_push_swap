# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    performance.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ebennace <ebennace@student.42lausanne.c    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/06/21 06:09:03 by ebennace          #+#    #+#              #
#    Updated: 2022/06/21 06:43:56 by ebennace         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from traceback import print_tb


def print_performance(epsilon, number_actions, cummulative_reward):
    print("----------------------------------")
    print(f"Epsilon [{epsilon}]")
    print(f"Number of Actions [{number_actions}]")
    print(f"Cumulative Reward [{cummulative_reward}]")
    print("----------------------------------")
    
def print_episode_duration(episode_duration):
    i = 0
    for e in episode_duration:
        i += 1
        print(f"- Episode {i} : {e} Actions")