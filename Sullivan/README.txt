Markov Decision Processes
Christopher Sullivan
CS-390

1.) Download the files and ensure that main.py, grid_world.py, and example2.py are located in the same directory.
2.) Ensure that mdptoolbox and numpy are installed. 
3.) Run the script main.py and interact with the prompts.

Forest Reward Changes:
Within example2.py, changes were made to the forest.R matrix in order to better reflect the problem domain through the MDP. Rather than the base reward model, the rewards now consist of values of: S + 100 for waiting in oldest state, S + 50 for cutting in oldest state, range {1 -> S} for cutting in any state past 0, and for each state in the latter half of the problem, index(S) - 5 for waiting. The goal of this was to give value to waiting on a relatively old forest in large-state problem instances, whereas typically it would be better to cut right up until the forest is at its' peak age or soon before. However, value is retained for cutting early on, as well as after the forest has reached half its' age, since the value of cutting a mid-aged forest is still five higher than that of waiting. This allows a user to better visualize the Bellman Equation's forward-look-up nature by observing that even though in later states cutting is still more profitable than waiting, the payoff of waiting until the end prevails as optimal so long as fire is not too prevalent.