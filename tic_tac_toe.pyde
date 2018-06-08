from BoardFile import Board
def setup():
    size(1000, 800)
    global board
    board = Board()
    
def draw():
    global board
    background(150)
    board.display()
    # board.checkForWin()

def mousePressed():
    global board
    board.handleClick()

# Reset game when player hits spacebar
def keyPressed():
    global board
    if key == ' ':
        board = Board()
