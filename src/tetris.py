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
        
        for dx,dy in positions:
            if x+dx < 0 or x+dx > len(self.grid[0]) or y+dy < 0 or y+dy > len(self.grid):
                self.brockdata = self.grid.copy()
                print("---------------------")
                print(self.blockdata)
                raise Exception("Invalid position")
            else:
                self.grid[y+dy][x+dx] += 1

    def is_validmove(self,positions,x,y):
        for dx,dy in positions:
            if x+dx < 0 or x+dx > len(self.grid[0]) or y+dy < 0 or y+dy > len(self.grid):
                return False
        return True
                
            
            

class Game:
    def __init__(self):
        self.board = Board(10,20)
        self.mino = Mino(3)
        self.mino.self_generate()


    def update(self):
        positions = self.mino.get_position()
        self.board.is_validmove(positions,3,10)

        




if __name__ == '__main__':
    game1 = Game()
    game1.update()



    #回転も移動も何か返して妥当性を判定する

    

