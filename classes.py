import numpy as np

class Board:

    def __init__(self, name):

        self.name = name

    def start_board(self):

        self = np.full((10,10), ' ')    
        return self


