# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    constant.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ebennace <ebennace@student.42lausanne.c    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/06/08 05:39:04 by ebennace          #+#    #+#              #
#    Updated: 2022/07/07 10:20:13 by ebennace         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# ---- Input ---- #
STACK_SIZE = 3
NBR_STACK = 2
NULL_VALUE = -1

# ---- Env ---- #
EPISODE = 1

# ---- Replay Memory ---- #
CAPACITY = 100_000
BATCH_SIZE = 50
MIN_REPLAY_MEMORY_SIZE = 50

# ---- Epsilon ---- #
DECAY = 0.001
START_EPSILON = 1
MIN_EPSILON = 0.15

## ----- Reward ----- ## 
ACTION_REWARD = -1
EMPTY_REWARD = -5
USELESS_ACTION = -5
BAD_FINISH_REWARD = -8
FINISH_REWARD = 100

# ---- Learning ---- #
LEARNING_RATE = 0.1
DISCOUNT = 0.95
GAMMA = 0.99
TARGET_UPDATE = 10
