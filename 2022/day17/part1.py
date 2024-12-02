import numpy as np

shapes = [
    [0b11110],
    [
        0b1000,
        0b11100,
        0b1000
    ],
    [
        0b100,
        0b100,
        0b11100
    ],
    [
        0b10000,
        0b10000,
        0b10000,
        0b10000
    ],
    [
        0b11000,
        0b11000
    ]
]

def can_shift_right(shape, shape_height, chamber_state):
    if any(bit % 2 == 1 for bit in shape):
        return False
    
    for i in range (0, len(shape)):
        chamber_row = shape_height - i
        if chamber_row >= len(chamber_state):
            return True
        
        shifted = shape[i] >> 1
        if shifted & chamber_state[chamber_row] != 0b0:
            return False
        
    return True

def shift_shape_right(shape):
    return [row >> 1 for row in shape]
    
def can_shift_left(shape, shape_height, chamber_state):
    if any(bit >= 0b1000000 for bit in shape):
        return False
    
    for i in range (0, len(shape)):
        chamber_row = shape_height - i
        if chamber_row >= len(chamber_state):
            return True
        
        shifted = shape[i] << 1
        if shifted & chamber_state[chamber_row] != 0b0:
            return False
        
    return True

def shift_shape_left(shape):
    return [row << 1 for row in shape]

def can_drop_shape(shape, shape_height, chamber_state):
    if shape_height - len(shape) < 0:
        return False
    
    for i in range (0, len(shape)):
        chamber_row = shape_height - (i + 1)
        if chamber_row >= len(chamber_state):
            return True
        
        if shape[i] & chamber_state[chamber_row] != 0b0:
            return False
        
    return True
    
def update_chamber_state(shape, shape_height, chamber_state):
    for i in range (0, len(shape)):
        chamber_row = shape_height - i
        
        chamber_state[chamber_row] = chamber_state[chamber_row] | shape[i]
        
    return chamber_state

def place_shape(shape, chamber_state, currents):
    chamber_state = chamber_state + list(np.repeat(0b0, 3 + len(shape)))
    shape_height = len(chamber_state) - 1
    dropping = True
    
    while dropping:
        current = currents[0]
        currents = currents[1:] + current[0]
        
        if current == '>':
            if can_shift_right(shape, shape_height, chamber_state):
                shape = shift_shape_right(shape)
        elif current == '<':
            if can_shift_left(shape, shape_height, chamber_state):
                shape = shift_shape_left(shape)
                
        if can_drop_shape(shape, shape_height, chamber_state):
            shape_height -= 1
        else:
            chamber_state = update_chamber_state(shape, shape_height, chamber_state)
            dropping = False
            
    return chamber_state[:chamber_state.index(0)], currents

chamber = []

file = open("day17/input.txt")
currents = file.read().strip()
        
for i in range(2022):
    shape = shapes[i % 5].copy()
    chamber, currents = place_shape(shape, chamber, currents)

print(len(chamber))
