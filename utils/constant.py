# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    constant.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ebennace <ebennace@student.42lausanne.c    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/06/08 05:39:04 by ebennace          #+#    #+#              #
#    Updated: 2022/06/20 11:45:38 by ebennace         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


STACK_SIZE = 3

EPISODE = 2
CAPACITY = 100_000
BATCH_SIZE = 100
MIN_REPLAY_MEMORY_SIZE = 100

DECAY = 0.001
START_EPSILON = 1
MIN_EPSILON = 0.15
TARGET_UPDATE = 10

## ----- Reward ----- ## 
ACTION_REWARD = -1
EMPTY_REWARD = -5
USELESS_ACTION = -5
BAD_FINISH_REWARD = -8
FINISH_REWARD = 100

LEARNING_RATE = 0.1
DISCOUNT = 0.95
GAMMA = 0.99
