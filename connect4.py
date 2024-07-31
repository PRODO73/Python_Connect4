import numpy as np

class Connect4:

    def __init__(self, rows, columns):
        
        self.grid = np.zeros((rows, columns), dtype=int)
        self.rows = rows 
        self.columns = columns
        self.turns = 0
    
    def render(self):
        for row in range(self.rows):
            for column in range(self.columns):
                if column == self.columns - 1:
                    print(self.grid[row][column])
                else:
                    print(self.grid[row][column], end="")

if __name__ == "__main__":
    game = Connect4(3,3)
    game.render()