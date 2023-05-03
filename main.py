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

gw_P = gw.P
gw_R = gw.R

def new_forest(num_states, fire_prob):
    forest_model = ex.forest(S = num_states, p = fire_prob)
    forest_P = forest_model[0]
    forest_R = forest_model[1]
    return forest_P, forest_R


def value_iter_gw():
    pass

def value_iter_forest():
    pass

def policy_iter_gw():
    pass

def value_iter_forest():
    pass

def main():
    pass

if __name__ == "__main__":
    main()

