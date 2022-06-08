# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    constant.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ebennace <ebennace@student.42lausanne.c    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/06/08 05:39:04 by ebennace          #+#    #+#              #
#    Updated: 2022/06/08 06:23:41 by ebennace         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


STACK_SIZE = 10

EPISODE = 1
CAPACITY = 100_000
BATCH_SIZE = 10
MIN_REPLAY_MEMORY_SIZE = 100

DECAY = 0.001
START_EPSILON = 1
MIN_EPSILON = 0.15
TARGET_UPDATE = 10

ACTION_REWARD = -1
INVERSE_ACTION_REWARD = -5
FINISH_REWARD = 100

LEARNING_RATE = 0.1
DISCOUNT = 0.95
GAMMA = 0.99
