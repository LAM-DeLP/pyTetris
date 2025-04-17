import random
import numpy
import time

class Mino:

    velo = [[1,0],[-1,0],[0,1],[0,-1]]
    def __init__(self,numOfmino):
        self.minoVer = [[0,0]]
        self.times = numOfmino

    def self_generate(self):
        for i in range(self.times):
            tempVer = []
            for j in range(4):                
                combined = [x+y for (x,y) in zip(self.minoVer[i],Mino.velo[j])]
                if not(combined in self.minoVer):
                    tempVer.append(Mino.velo[j])
                else:
                    pass
            combined = [x+y for (x,y) in zip(self.minoVer[i],random.choice(tempVer))]
            self.minoVer.append(combined)

    def rotate(self):
        for i in range(len(self.minoVer)):
            self.minoVer[i] = [-self.minoVer[i][1],self.minoVer[i][0]]

    def get_position(self):
        return self.minoVer

class Board:
    def __init__(self,length,height):
        self.grid = numpy.zeros((height,length))
        self.blockdata = numpy.zeros((height,length))
        self.clearStandard = length

    def assign(self,positions,x,y):
        self.grid = self.blockdata.copy()
        for dx,dy in positions:
            if x+dx < 0 or x+dx > len(self.grid[0]) or y+dy < 0 or y+dy > len(self.grid):
                self.brockdata = self.grid.copy()
            else:
                self.grid[y+dy][x+dx] += 1

            
            

class Game:
    def __init__(self):
        self.board = Board(10,20)


    def update(self):
        x=3
        y=10
        
        while True:
            self.mino = Mino(3)
            self.mino.self_generate()
            
            positions = self.mino.get_position()
            self.board.assign(positions,x,y)
            print(self.board.grid)
            time.sleep(0.25)
            y -= 1
        



if __name__ == '__main__':
    game1 = Game()
    game1.update()



    #回転も移動も何か返して妥当性を判定する

    

