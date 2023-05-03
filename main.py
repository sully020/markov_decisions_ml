""" 
Markov Decision Processes - main.py
Christopher D. Sullivan
Professor Brian O'Neill
Due 5/4/23

Imports:
https://pymdptoolbox.readthedocs.io/en/latest/ - mdptoolbox

"""


import mdptoolbox.mdp as mdp, mdptoolbox.util as util, mdptoolbox.example as ex


# Up, Left, Down, Right.
gw_P = [
      [
      [.1, .1, 0, 0, .8, 0, 0, 0, 0, 0, 0],
      [.1, 0, .1, 0, 0, .8, 0, 0, 0, 0, 0],
      [0, .1, .8, .1, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, .1, .1, 0, 0, .8, 0, 0, 0, 0],
      [0, 0, 0, 0, .1, .1, 0, .8, 0, 0, 0],
      [0, 0, 0, 0, .1, .1, 0, 0, .8, 0, 0],
      [0, 0, 0, 0, 0, 0, .2, 0, 0, 0, .8], 
      [0, 0, 0, 0, 0, 0, 0, .9, .1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, .1, .8, .1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, .1, .8, .1],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, .1, .9], 
      ], 
      [
      [.9, 0, 0, 0, .1, 0, 0, 0, 0, 0, 0],
      [.8, .1, 0, 0, 0, .1, 0, 0, 0, 0, 0],
      [0, .8, .2, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, .8, .1, 0, 0, .1, 0, 0, 0, 0],
      [.1, 0, 0, 0, .8, 0, 0, .1, 0, 0, 0],
      [0, .1, 0, 0, .8, 0, 0, 0, .1, 0, 0],
      [0, 0, 0, .1, 0, 0, .8, 0, 0, 0, .1], 
      [0, 0, 0, 0, .1, 0, 0, .9, 0, 0, 0],
      [0, 0, 0, 0, 0, .1, 0, .8, .1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, .8, .2, 0],
      [0, 0, 0, 0, 0, 0, .1, 0, 0, .8, .1], 
      ], 
      [
      [.9, .1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [.1, .8, .1, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, .1, .8, .1, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, .1, .9, 0, 0, 0, 0, 0, 0, 0],
      [.8, 0, 0, 0, .1, .1, 0, 0, 0, 0, 0],
      [0, .8, 0, 0, .1, .1, 0, 0, 0, 0, 0],
      [0, 0, 0, .8, 0, 0, .2, 0, 0, 0, 0], 
      [0, 0, 0, 0, .8, 0, 0, .1, .1, 0, 0],
      [0, 0, 0, 0, 0, .8, 0, .1, 0, .1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, .1, .8, .1],
      [0, 0, 0, 0, 0, 0, .8, 0, 0, .1, .1], 
      ], 
      [
      [.1, .8, 0, 0, .1, 0, 0, 0, 0, 0, 0],
      [0, .1, .8, 0, 0, .1, 0, 0, 0, 0, 0],
      [0, 0, .2, .8, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, .9, 0, 0, .1, 0, 0, 0, 0],
      [.1, 0, 0, 0, 0, .8, 0, .1, 0, 0, 0],
      [0, .1, 0, 0, 0, .8, 0, 0, .1, 0, 0],
      [0, 0, 0, .1, 0, 0, 0, .8, 0, 0, .1], 
      [0, 0, 0, 0, .1, 0, 0, .1, .8, 0, 0],
      [0, 0, 0, 0, 0, .1, 0, 0, .1, .8, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, .2, .8],
      [0, 0, 0, 0, 0, 0, .1, 0, 0, 0, .9], 
      ]
]

gw_R = [-.04, -.04, -.04, -.04, -.04, -1, -.04, -.04, -.04, -.04, 1]

def new_forest(num_states, fire_prob):
    forest_model = ex.forest(S = num_states, p = fire_prob)
    forest_P = forest_model[0]
    forest_R = forest_model[1]
    return forest_P, forest_R


def main():
    pass

if __name__ == "__main__":
    main()

