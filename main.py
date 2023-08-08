""" 
Markov Decision Processes - main.py
Christopher D. Sullivan
Professor Brian O'Neill
Due 5/5/23

Imports:
https://pymdptoolbox.readthedocs.io/en/latest/ - mdptoolbox
https://numpy.org/ - numpy
"""

import mdptoolbox.mdp as mdp
import numpy as np
import grid_world as gw
from example2 import forest

gw_stochasticP = np.array(gw.stochastic_P)
gw_deterministicP = np.array(gw.deterministic_P)
gw_R = np.array(gw.R)


def translate_gw_policy(policy):
    engl_pol = list(range(11))
    for i in range(len(policy)):
        match policy[i]:
            case 0:
                engl_pol[i] = 'Up'
            case 1:
                engl_pol[i] = 'Left'
            case 2:
                engl_pol[i] = 'Down'
            case 3:
                engl_pol[i] = 'Right'
    return str(engl_pol)

def value_iter_gw():
    print("Grid World: Value Iteration - ")
    is_chosen = False
    while (is_chosen == False):
        choice = input("Would you like the agent's actions to be deterministic (D) or non-deterministic (N)? ")
        if choice == 'D' or choice == 'd':
            discount = float(input("Please enter the decimal discount factor for future rewards: "))
            gw_vi = mdp.ValueIteration(gw_deterministicP, gw_R, discount, epsilon = .01)
            is_chosen = True  
        elif choice == 'N' or choice == 'n':
            discount = float(input("Please enter the decimal discount factor for future rewards: "))
            gw_vi = mdp.ValueIteration(gw_stochasticP, gw_R, discount)
            is_chosen = True
        else:
            print('Input not recognized. Please select the letter D or the letter N.\n')
            continue

    gw_vi.run()
    print("The grid-world policy returned by Value Iteration was: " + translate_gw_policy(gw_vi.policy))
    print("The number of iterations in which Value Iteration converged was: " + str(gw_vi.iter) + "\n")

def policy_iter_gw():
    print("Grid World: Policy Iteration - ")
    is_chosen = False
    while (is_chosen == False):
        choice = input("Would you like the agent's actions to be deterministic (D) or non-deterministic (N)? ")
        if choice == 'D' or choice == 'd':
            discount = float(input("Please enter the decimal discount factor for future rewards: "))
            gw_pi = mdp.PolicyIteration(gw_deterministicP, gw_R, discount)
            is_chosen = True  
        elif choice == 'N' or choice == 'n':
            discount = float(input("Please enter the decimal discount factor for future rewards: "))
            gw_pi = mdp.PolicyIteration(gw_stochasticP, gw_R, discount)
            is_chosen = True
        else:
            print('Input not recognized. Please select the letter D or the letter N.\n')
            continue
            
    gw_pi.run()
    print("The grid-world policy returned by Policy Iteration was: " + translate_gw_policy(gw_pi.policy))
    print("The number of iterations in which Policy Iteration converged was: " + str(gw_pi.iter) + "\n")


def translate_forest_policy(policy, num_states):
    engl_pol = list(range(num_states))
    for i in range(len(policy)):
        match policy[i]:
            case 0:
                engl_pol[i] = str(i) + ': Wait'
            case 1:
                engl_pol[i] = str(i) + ': Cut'
    return str(engl_pol)

def forest_input():
    num_states = int(input("How many years (# of states) until the forest reaches its' peak?: "))
    fire_prob = float(input("Enter the decimal probability of fire p: "))
    return num_states, fire_prob

def new_forest(num_states, fire_prob):
    forest_model = forest(S = num_states, p = fire_prob)
    forest_P = forest_model[0]
    forest_R = forest_model[1]
    return forest_P, forest_R

def value_iter_forest():
    num_states, fire_prob = forest_input()
    discount = float(input("Please enter the decimal discount factor for future rewards: "))
    forest_P, forest_R = new_forest(num_states, fire_prob)
    vi_forest = mdp.ValueIteration(forest_P, forest_R, discount)
    vi_forest.run()
    print("The forest management policy returned by Value Iteration was: " + translate_forest_policy(vi_forest.policy, num_states))
    print("The number of iterations in which Value Iteration converged was: " + str(vi_forest.iter) + "\n")

def policy_iter_forest():
    num_states, fire_prob = forest_input()
    discount = float(input("Please enter the decimal discount factor for future rewards: "))
    forest_P, forest_R = new_forest(num_states, fire_prob)
    pi_forest = mdp.ValueIteration(forest_P, forest_R, discount)
    pi_forest.run()
    print("The forest management policy returned by Policy Iteration was: " + translate_forest_policy(pi_forest.policy, num_states))
    print("The number of iterations in which Policy Iteration converged was: " + str(pi_forest.iter) + "\n")


def test_gw():
    value_iter_gw()
    policy_iter_gw()

def test_forest():
    value_iter_forest()
    policy_iter_forest()

def main():
    print()
    #test_gw()
    test_forest()

if __name__ == "__main__":
    main()

# Professor O'Neill, you are the G.O.A.T. Best of luck in your coming endeavors!