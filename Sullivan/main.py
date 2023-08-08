""" 
Markov Decision Processes - main.py
Christopher D. Sullivan
Professor Brian O'Neill
Due 5/5/23

The purpose of this script is to employ reinforcement learning algorithms in order to solve two 
MDP-model logical problems. This is achieved by employing the Value Iteration and Policy Iteration
algorithms against a custom Grid World MDP problem, and the mdptoolbox Forest example problem.

Imports:
https://pymdptoolbox.readthedocs.io/en/latest/ - mdptoolbox
https://numpy.org/ - numpy
"""

import mdptoolbox.mdp as mdp
import numpy as np
import grid_world as gw      # Customized Grid World, presented in analysis.pdf
from example2 import forest  # mdptoolbox forest problem with revised reward matrix

# Grid World representation matrices
gw_stochasticP = np.array(gw.stochastic_P)     
gw_deterministicP = np.array(gw.deterministic_P)
gw_R = np.array(gw.R)

# Takes Grid World policy object and converts it into readable list.
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

# Function which runs value iteration over the user's choice of deterministic or stochastic Grid World.
def value_iter_gw():
    print("Grid World: Value Iteration - ")
    is_chosen = False
    while (is_chosen == False):
        choice = input("Would you like the agent's actions to be deterministic (D) or non-deterministic (N)? ")
        if choice == 'D' or choice == 'd':
            discount = float(input("Please enter the decimal discount factor for future rewards: "))
            gw_vi = mdp.ValueIteration(gw_deterministicP, gw_R, discount)
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

# Function which runs policy iteration over D/S Grid World.
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

# Converts Forest policy into readable list.
def translate_forest_policy(policy, num_states):
    engl_pol = list(range(num_states))
    for i in range(len(policy)):
        match policy[i]:
            case 0:
                engl_pol[i] = str(i) + ': Wait'
            case 1:
                engl_pol[i] = str(i) + ': Cut'
    return str(engl_pol)

# Takes user input as forest problem parameters.
def forest_input():
    num_states = int(input("How many years (# of states) until the forest reaches its' peak?: "))
    fire_prob = float(input("Enter the decimal probability of fire p: "))
    return num_states, fire_prob

# Create new forest problem model, return transition-prob. & reward matrices.
def new_forest(num_states, fire_prob):
    forest_model = forest(S = num_states, p = fire_prob)
    forest_P = forest_model[0]
    forest_R = forest_model[1]
    return forest_P, forest_R

# Function which runs value iteration over the revised forest problem.
def value_iter_forest():
    print("Forest Management: Value Iteration - ")
    num_states, fire_prob = forest_input()
    discount = float(input("Please enter the decimal discount factor for future rewards: "))
    forest_P, forest_R = new_forest(num_states, fire_prob)
    vi_forest = mdp.ValueIteration(forest_P, forest_R, discount)
    vi_forest.run()
    print("The forest management policy returned by Value Iteration was: " + translate_forest_policy(vi_forest.policy, num_states))
    print("The number of iterations in which Value Iteration converged was: " + str(vi_forest.iter) + "\n")

# Function which runs policy iteration over the revised forest problem.
def policy_iter_forest():
    print("Forest Management: Policy Iteration - ")
    num_states, fire_prob = forest_input()
    discount = float(input("Please enter the decimal discount factor for future rewards: "))
    forest_P, forest_R = new_forest(num_states, fire_prob)
    pi_forest = mdp.PolicyIteration(forest_P, forest_R, discount)
    pi_forest.run()
    print("The forest management policy returned by Policy Iteration was: " + translate_forest_policy(pi_forest.policy, num_states))
    print("The number of iterations in which Policy Iteration converged was: " + str(pi_forest.iter) + "\n")


# Convenience function which tests both algorithms over Grid World. 
def test_gw():
    value_iter_gw()
    policy_iter_gw()

# Convenience function which tests both algorithms using Forest Management problem. 
def test_forest():
    #value_iter_forest()
    policy_iter_forest()
    

def main():
    print()
    #test_gw()
    test_forest()

if __name__ == "__main__":
    main()

# Professor O'Neill, you are the G.O.A.T. Best of luck in your coming endeavors!