from itertools import zip_longest
import numpy as np



def print_state(A, B):
    
    print("---State t---")
    print("-A-\t-B-")
    print("___________\t")
    for a, b in zip_longest(reversed(A.stack), reversed(B.stack), fillvalue='xxx'):
        
        print(f"|{a}\t{b}|")
    print("___________\t")
    
    
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
    print(f"\tAction [{experience.action}]")
    print(f"\tReward [{experience.reward}]")
    print("----------------------------------")

def print_buffer(buffer):
    
    print("========== BUFFER ==========")
    for i in buffer:
        print_experience(i)
    print(f"========== [{len(buffer)} experience ] ==========")