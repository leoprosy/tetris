from random import randint

class Block:
    def __init__(self):
        block = blocks[randint(0,len(blocks)-1)]
        self.shape = block[0]
        self.pos = (0, 3)
        self.color = block[1]

blocks:list = [[
    [[1,1,1,1],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]], (127,255,212)
],[
    [[1,1,0,0],
    [1,1,0,0],
    [0,0,0,0],
    [0,0,0,0]], (255,255,0)
],[
    [[1,1,1,0],
    [0,1,0,0],
    [0,0,0,0],
    [0,0,0,0]], (128,0,128)
],[
    [[1,1,1,0],
    [1,0,0,0],
    [0,0,0,0],
    [0,0,0,0]], (255,165,0)
],[
    [[1,1,1,0],
    [0,0,1,0],
    [0,0,0,0],
    [0,0,0,0]], (0,0,255)
],[
    [[1,1,0,0],
    [0,1,1,0],
    [0,0,0,0],
    [0,0,0,0]], (255,0,0)
],[
    [[0,1,1,0],
    [1,1,0,0],
    [0,0,0,0],
    [0,0,0,0]], (0,255,0)
]]