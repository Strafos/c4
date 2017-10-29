import winc4 as bot

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

# Human play vs computer
def test1():
    game = connect4()
    for i in range(20):
        zb = int(input('move? '))
        game.move(zb, 'O')
        game.printgame()
        print('---------------------------')
        botmove = bot.findmove(game)
        game.move(botmove, 'X')
        game.printgame()
        print('---------------------------')

# Set up board to debug findwin
def test2():
    game = connect4()
    game.move(3, 'O')
    game.move(4, 'O')
    game.move(5, 'O')
    game.move(3, 'X')
    game.move(6, 'X')
    # game.move(3, 'X')
    game.printgame()
    botmove = bot.findmove(game)
    game.move(botmove, 'X')
    game.printgame()

test1()