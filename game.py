

class connect4:
    width = 7
    height = 6
    connect = 4

    # Create a 6 x 7 board
    def __init__(self):
        self.gamestate = [['_' for i in range(self.width)] for i in range(self.height)]

    # Places a piece (X or O) in a position (0 to 6)
    # Calls win function to determine if move resulted in win
    def move(self, pos, piece):
        x = pos
        played = False
        for y in range(self.height-1, -1, -1):
            if self.gamestate[y][x] == '_':
                played = True
                self.gamestate[y][x] = piece
                break
        return (played, self.win((x,y), piece))

    def printgame(self):
        for y in range(self.height):
            print(' '.join(self.gamestate[y]))

    def win(self, coord, piece):
        dir = [-1, 0, 1]
        for dy in dir:
            for dx in dir:
                if dx == dy == 0:
                    continue
                xstart = coord[0]
                ystart = coord[1]
                for i in range(3):
                    if xstart > 0 and xstart <= self.width - 1 and ystart > 0 and ystart <= self.height - 1:
                        xstart -= dx
                        ystart -= dy
                count = 0
                for i in range(self.connect*2 -1):
                    posx = xstart + i*dx
                    posy = ystart + i*dy
                    if posx >= 0 and posx <= self.width - 1 and posy >= 0 and posy <= self.height - 1:
                        if self.gamestate[posy][posx] == piece:
                            count += 1
                        else:
                            count = 0
                        if count == 4:
                            return True
                    else:
                        break
        return False

game = connect4()
game.printgame()
print('---------------------------')
for i in range(4):
    print(game.move(i, 'O'))
game.printgame()

