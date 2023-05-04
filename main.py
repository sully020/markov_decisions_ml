""" 
Markov Decision Processes - main.py
Christopher D. Sullivan
Professor Brian O'Neill
Due 5/4/23

Imports:
https://pymdptoolbox.readthedocs.io/en/latest/ - mdptoolbox

"""


import mdptoolbox.mdp as mdp, mdptoolbox.util as util, mdptoolbox.example as ex
import grid_world as gw
import numpy as np

gw_chanceP = np.array(gw.chance_P)
gw_chanceR = np.array(gw.chance_R)
gw_deterministicP = np.array(gw.deterministic_P)
gw_deterministicR = np.array(gw.deterministic_R)

def new_forest(num_states, fire_prob):
    forest_model = ex.forest(S = num_states, p = fire_prob)
    forest_P = forest_model[0]
    forest_R = forest_model[1]
    return forest_P, forest_R


def value_iter_gw():
    is_chosen = False
    while (is_chosen == False):
        choice = input("Would you like the agent's actions to be deterministic (D) or non-deterministic (N)? ")
        if choice == 'D' or 'd':
            gw_vi = mdp.ValueIteration(gw_chanceP, gw_chanceR, .2)
            is_chosen = True  
        elif choice == 'N' or 'n':
            gw_vi = mdp.ValueIteration(gw_deterministicP, gw_deterministicR, .2)
            is_chosen = True
        else:
            print('Input not recognized. Please select the letter D or the letter N.')

    gw_vi.run()
    print(gw_vi.policy)

def policy_iter_gw():
    is_chosen = False
    while (is_chosen == False):
        choice = input("Would you like the agent's actions to be deterministic (D) or non-deterministic (N)? ")
        if choice == 'D' or 'd':
            gw_vi = mdp.PolicyIteration(gw_chanceP, gw_chanceR, .2)
            is_chosen = True  
        elif choice == 'N' or 'n':
            gw_vi = mdp.PolicyIteration(gw_deterministicP, gw_deterministicR, .2)
            is_chosen = True
        else:
            print('Input not recognized. Please select the letter D or the letter N.')
            
    gw_vi.run()
    print(gw_vi.policy)

def forest_input():
    num_states = input("How many years until the forest reaches its' peak? (Number of states): ")
    fire_prob = input("Enter an integer for probability of fire p: .")

def value_iter_forest():
    states, prob = new_forest()

def value_iter_forest():
    pass

def main():
    value_iter_gw()
    policy_iter_gw()

if __name__ == "__main__":
    main()

# Professor O'Neill, you are the G.O.A.T. Best of luck in your coming endeavors!