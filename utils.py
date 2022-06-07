import numpy as np

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

def pre_processing_state(state):
    return state.reshape((1, state.shape[0], state.shape[1]))
    
def is_sorted(A):
    for i in range(A.stack.size -1):
         if A.stack[i+1] > A.stack[i] :
               return False
    return True


    
    
