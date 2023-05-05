# Up, Left, Down, Right.
stochastic_P = [
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

deterministic_P = [
      [
      [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
      [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
      ], 
      [
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
      ], 
      [
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
      ], 
      [
      [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
      ], 
]

R = [-.04, -.04, -.04, -.04, -.04, -1, -.04, -.04, -.04, -.04, 1]