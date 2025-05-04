import random
import numpy
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
    
    def decrease_lifetime(self,dt):
        self.lifetime -= dt
    
    def reset_lifetime(self):
        self.lifetime = 100

    def get_shape(self):
        return self.minoVer
    def get_lifetime(self):
        return self.lifetime

class Board:
    def __init__(self,length,height,ix,iy):
        self.length = length
        self.height = height
        self.grid,self.blockdata = numpy.zeros((self.height,self.length)),numpy.zeros((self.height,self.length))
        self.initcoord = [ix,iy]
        self.minocoord = [self.initcoord[0],self.initcoord[1]]

    def validmove(self,shape,dx,dy):
        for rx,ry in shape:
            x = self.minocoord[0]+rx+dx
            y = self.minocoord[1]+ry+dy
            if x<0 or x>=len(self.grid[0]):
                return False
            if y<0 or y>=len(self.grid):
                return False
            elif self.blockdata[y][x]==1:
                return False
        return True          
        
    def set_mino(self,shape):
        self.grid[:] = self.blockdata
        for rx,ry in shape:
            x=self.minocoord[0]+rx
            y=self.minocoord[1]+ry
            self.grid[y][x] = 1

    def is_fixed(self,lifetime):
        if lifetime<=0:
            self.blockdata[:] = self.grid
            self.minocoord = [self.initcoord[0],self.initcoord[1]]
            for y,row in enumerate(self.blockdata):
                if numpy.sum(self.blockdata[y])==self.length:
                    self.blockdata =numpy.delete(self.blockdata,y,axis=0)
                    self.blockdata =numpy.insert(self.blockdata,0,[0,0,0,0,0,0,0,0,0,0],axis=0)
            return False
        else:
            return True

    def move_mino(self,dx,dy):
        self.minocoord[0] += dx
        self.minocoord[1] += dy
class Game:

    def __init__(self):
        self.board = Board(10,20,5,3)
        self.mino = Mino(3)
        self.mino.self_generate()
        self.flametime = 0
        self.dx,self.dy = 0,0
        self.is_rotate = False

    def flamemanager(self,dx,dy,dt):
        if self.flametime > 100:
            self.board.move_mino(dx,dy)
            self.flametime = 0
        else:
            self.flametime += dt

    def update(self):

        shape = self.mino.get_shape()
        lifetime = self.mino.get_lifetime()
        if self.is_rotate == True:
            tempShape = numpy.copy(shape)
            for i in range(len(tempShape)):
                tempShape[i] = [-tempShape[i][1],tempShape[i][0]]
            if self.board.validmove(tempShape,0,0):
                self.mino.rotate()
            self.is_rotate = False       
                 
        if self.board.validmove(shape,0,1) == False:
            self.mino.decrease_lifetime(2)
            if self.board.is_fixed(lifetime) == False:
                self.mino.self_generate()
                self.mino.reset_lifetime()
        else:
            self.flamemanager(0,1,5)

        if self.board.validmove(shape,0,self.dy) == False:
            self.mino.decrease_lifetime(2)
            if self.board.is_fixed(lifetime) == False:
                self.mino.self_generate()
                self.mino.reset_lifetime()
        else:
            self.board.move_mino(0,self.dy)

        if self.board.validmove(shape,self.dx,0)==True:
            self.board.move_mino(self.dx,0)

        self.board.set_mino(shape)
        self.dx,self.dy = 0,0