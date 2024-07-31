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
        print("\n")
    
    def placeCounter(self, playedColumn):
        for row in reversed(range(self.rows)):
            if self.grid[row][playedColumn] == 0:
                self.grid[row][playedColumn] = 1
                return
            
        print("Sorry, no numbers below zero")
        return

if __name__ == "__main__":
    game = Connect4(3,3)
    while True:
        playerInput = input('Place a counter: ')
        game.placeCounter(int(playerInput))
        game.render()