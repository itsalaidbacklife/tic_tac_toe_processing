class Board:
    def __init__(self):
        self.spaces = [['', '', ''] for x in range(3)] #List of spaces to move in
        self.symbols = ['X', 'O'] #Player symbols
        self.sym_index = 0 #X goes first
        self.winner = ''
        self.game_type = ''
    
    def display(self):
        if self.game_type != '':
            strokeWeight(7)
            line(width/3, height/7, width/3, height*6/7)
            line(width*2/3, height/7, width*2/3, height*6/7)
            line(width/6, height*8/21,  width*5/6, height*8/21)
            line(width/6, height*18/27, width*5/6, height*18/27)
            textSize(24)
            for r_index, row in enumerate(self.spaces):
                for c_index, space in enumerate(row):
                    margin = 0
                    if c_index == 0:
                        margin = width*9/36
                    elif c_index == 1:
                        margin = width*3/18
                    else:
                        margin = width*7/72
                    text(space, c_index * width/3  + margin, r_index * height*5/21 + height*12/42)
            if self.winner != '':
                text("%s Wins!" %self.winner, width/2-width/25, height/2)
        # Ask player to play pvp or pve
        else:
            strokeWeight(4)
            fill(0, 200, 0)
            rect(width/3 - width/12, height*8/21+2.5/21, width/6, height*2.5/21)
            textSize(18)
            fill(255)
            text("2 Player", width/3 - width/25, height*8/21+height*3/42)
            fill(200,0,0)
            rect(width/2 + width/12, height*8/21+2.5/21, width/6, height*2.5/21)
            fill(255)
            text("vs Computer", width/2 + width*2.8/25, height*8/21+height*3/42)                
    
    def locateClick(self):
        res = [0, 0]
        # Set x index
        if mouseX >= width/3 and mouseX <= width*2/3:
            res[1] = 1
        elif mouseX > height*2/3:
            res[1] = 2
            # Set y index
        if mouseY >= height*8/21 and mouseY <= height*18/27:
            res[0] = 1
        elif mouseY >= height*18/27:
            res[0] = 2
        return res
    
    def handleClick(self):
        if self.game_type == '':
            if mouseX >= width/3 - width/12 and mouseX <= width/3 + width/12 + width/6:
                if mouseY >= height*8/21 + 2.5/21 and mouseY <= height*8/21 + 2.5/21 + height*2.5/21:
                    self.game_type = 'Two Player'
                    self.spaces = [['', '', ''] for x in range(3)] #List of spaces to move in
                    self.symbols = ['X', 'O'] #Player symbols
                    self.sym_index = 0 #X goes first
                    self.winner = ''
            elif mouseX >= width/2 + width/12 and mouseX <= width/2 + width/12 + width/6:
                if mouseY >= height*8/21+2.5/21 and mouseY <= height*8/21+2.5/21 + height*2.5/21:
                    self.game_type = 'AI'
                    self.spaces = [['', '', ''] for x in range(3)] #List of spaces to move in
                    self.symbols = ['X', 'O'] #Player symbols
                    self.sym_index = 0 #X goes first
                    self.winner = ''
        else:
            if self.winner == '':
                clicked = self.locateClick()
                if self.spaces[clicked[0]][clicked[1]] == '':
                    self.spaces[clicked[0]][clicked[1]] = self.symbols[self.sym_index] #Place symbol on board
                    self.sym_index = (self.sym_index + 1) % 2 #Switch symbol
                    if self.game_type == 'AI':
                        self.aiMove()
                self.checkForWin()
                
            else:
                self.spaces = [['', '', ''] for x in range(3)] #List of spaces to move in
                self.symbols = ['X', 'O'] #Player symbols
                self.sym_index = 0 #X goes first
                self.winner = ''
                self.game_type = ''
            
    def checkForWinInRow(self):
        for row in self.spaces:
            if row[0] == row[1] and row[1] == row[2] and row[0] != '':
                self.winner = row[0]
    
    def checkForWinInCol(self):
        for col_index in range(3):
            if self.spaces[0][col_index] == self.spaces[1][col_index] and self.spaces[1][col_index] == self.spaces[2][col_index] and self.spaces[2][col_index] != '':
                self.winner = self.spaces[0][col_index]
    
    def checkForWinDiag(self):
        if self.spaces[0][0] == self.spaces[1][1] and self.spaces[1][1] == self.spaces[2][2] and self.spaces[0][0] != '':
            self.winner = self.spaces[0][0]
        elif self.spaces[2][0] == self.spaces[1][1] and self.spaces[1][1] == self.spaces[0][2] and self.spaces[2][0] != '':
            self.winner = self.spaces[2][0]
    
    def checkForWin(self):
        self.checkForWinInRow()
        self.checkForWinInCol()
        self.checkForWinDiag()
        
    def aiMove(self):
        done = True
        for row in self.spaces:
            for space in row:
                if space == '':
                    done = False
        while not done:
            y = int(random(3))
            x = int(random(0, 3))
            if self.spaces[y][x] == '':
                self.spaces[y][x] = self.symbols[self.sym_index]
                self.sym_index = (self.sym_index + 1) % 2
                done = True
        
    
