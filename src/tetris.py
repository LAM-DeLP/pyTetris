import random
import numpy
import time

class Mino:

    velo = [[1,0],[-1,0],[0,1],[0,-1]]
    def __init__(self,numOfmino):
        self.minoVer = [[0,0]]
        self.times = numOfmino
        self.lifetime = 100

    def self_generate(self):
        self.minoVer = [[0,0]]
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
    
    def decrease_lifetime(self):
        self.lifetime -= 20
    
    def reset_lifetime(self):
        self.lifetime = 100

    def get_shape(self):
        return self.minoVer
    def get_lifetime(self):
        return self.lifetime

class Board:
    def __init__(self,length,height,ix,iy):
        self.grid = numpy.zeros((height,length))
        self.blockdata = numpy.zeros((height,length))
        self.clearStandard = length
        self.minocoord = [ix,iy]
        self.minospeed = [0,0]

    def x_validmove(self,shape,dx):
        for rx,ry in shape:
            x = self.minocoord[0]+rx+dx
            y = self.minocoord[1]+ry
            if x<0 or x>=len(self.grid[0]):
                self.minospeed[0] = 0
                return False
            elif self.blockdata[y][x]==1:
                self.minospeed[0] = 0
                return False
        self.minospeed[0] = dx  
        return True          
        
    def y_validmove(self,shape,dy):
        for rx,ry in shape:
            x = self.minocoord[0]+rx
            y = self.minocoord[1]+ry+dy
            if y<0 or y>=len(self.grid):
                self.minospeed[1] = 0
                return False
            elif self.blockdata[y][x]==1:
                self.minospeed[1] = 0
                return False
        self.minospeed[1] = dy
        return True
        
    def set_mino(self,shape):
        self.grid = numpy.copy(self.blockdata)
        print(self.minospeed)
        self.minocoord[0]+=self.minospeed[0]
        self.minocoord[1]+=self.minospeed[1]
        for rx,ry in shape:
            x=self.minocoord[0]+rx
            y=self.minocoord[1]+ry
            self.grid[y][x] = 1

    def is_fixed(self,lifetime):
        if lifetime<=0:
            self.blockdata = numpy.copy(self.grid)
            self.minocoord = [4,4]
            return False
        else:
            return True
        

    def get_minostate(self):
        pass

class Game:
    def __init__(self):
        self.board = Board(10,20,4,4)
        self.mino = Mino(3)
        self.mino.self_generate()
    
    def update(self):
        while True:
            dy=1
            dx=random.choice([-1,0,1])
            shape = self.mino.get_shape()
            lifetime = self.mino.get_lifetime()
            self.board.x_validmove(shape,dx)
            if self.board.y_validmove(shape,dy) == False:
                self.mino.decrease_lifetime()
            if self.board.is_fixed(lifetime) == False:
                self.mino.self_generate()
                self.mino.reset_lifetime()
            self.board.set_mino(shape)

            print(self.board.grid)
            time.sleep(0.25)
            


if __name__ == '__main__':
    game1 = Game()
    game1.update()
    #回転も移動も何か返して妥当性を判定する