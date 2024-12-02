import math
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

memory = []
heights = []
first_instance = 0
next_instance = 0
        
for i in range(2022):
    shape = shapes[i % 5].copy()
    chamber, currents = place_shape(shape, chamber, currents)
    heights.append(len(chamber))
    
    if i > 30:
        state_string = f"{i % 5}:{','.join([str(n) for n in chamber[-30:]])}"
        if state_string in memory:
            first_instance = memory.index(state_string)
            next_instance = i
            break
        else:
            memory.append(state_string)
            
diff = next_instance - first_instance
leftover = 1000000000000 - first_instance
quot = math.floor(leftover / diff)
remainder = leftover % diff

full_stack = heights[-2] - heights[first_instance]

height = heights[first_instance] + (full_stack * quot) + heights[first_instance + remainder]

print(height)

# 1520000000257
# 1514285714288
# 1598536036235

# 1598536036235
# 1596283783987

# 1595988538691