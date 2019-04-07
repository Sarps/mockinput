index = 0

def input():
    global index
    index += 1
    return inputs[index-1]

def set_input_src(src):
    global inputs
    inputs = src