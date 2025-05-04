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
        self.grid = numpy.zeros((self.height,self.length))
        self.blockdata = numpy.zeros((self.height,self.length))
        self.clearStandard = length
        self.initcoord = [ix,iy]
        self.minocoord = [self.initcoord[0],self.initcoord[1]]

    def x_validmove(self,shape,dx):
        for rx,ry in shape:
            x = self.minocoord[0]+rx+dx
            y = self.minocoord[1]+ry
            if x<0 or x>=len(self.grid[0]):
                return False
            elif self.blockdata[y][x]==1:
                return False
        return True          
        
    def y_validmove(self,shape,dy):
        for rx,ry in shape:
            x = self.minocoord[0]+rx
            y = self.minocoord[1]+ry+dy
            if y<0 or y>=len(self.grid):
                return False
            elif self.blockdata[y][x]==1:
                return False
        return True
        
    def set_mino(self,shape):
        self.grid = numpy.copy(self.blockdata)
        for rx,ry in shape:
            x=self.minocoord[0]+rx
            y=self.minocoord[1]+ry
            self.grid[y][x] = 1

    def is_fixed(self,lifetime):
        if lifetime<=0:
            self.blockdata = numpy.copy(self.grid)
            self.minocoord = [self.initcoord[0],self.initcoord[1]]
            for y,row in enumerate(self.blockdata):
                if numpy.sum(self.blockdata[y])==10:
                    self.blockdata =numpy.delete(self.blockdata,y,axis=0)
                    self.blockdata =numpy.insert(self.blockdata,0,numpy.zeros((10,1)),axis=0)
            return False
        else:
            return True

    def move_mino(self,dx,dy):
        self.minocoord[0] += dx
        self.minocoord[1] += dy

    def get_minostate(self):
        pass

class Game:
    def __init__(self):
        self.board = Board(10,20,5,3)
        self.mino = Mino(3)
        self.mino.self_generate()
        self.flametime = 0
        self.dx,self.dy = 0,0

    def flamemanager(self,dx,dy,dt):
        if self.flametime > 100:
            self.board.move_mino(dx,dy)
            self.flametime = 0
        else:
            self.flametime += dt

    def update(self):

        shape = self.mino.get_shape()
        lifetime = self.mino.get_lifetime()


                
        if self.board.y_validmove(shape,1) == False:
            self.mino.decrease_lifetime(2)
            if self.board.is_fixed(lifetime) == False:
                self.mino.self_generate()
                self.mino.reset_lifetime()
        else:
            self.flamemanager(0,1,10)

        if self.board.y_validmove(shape,self.dy) == False:
            self.mino.decrease_lifetime(2)
            if self.board.is_fixed(lifetime) == False:
                self.mino.self_generate()
                self.mino.reset_lifetime()
        else:
            self.board.move_mino(0,self.dy)

        if self.board.x_validmove(shape,self.dx)==False:
            pass
        else:
            self.board.move_mino(self.dx,0)

        self.board.set_mino(shape)
        self.dx,self.dy = 0,0

if __name__ == '__main__':
    game1 = Game()
    game1.update()
    #回転も移動も何か返して妥当性を判定する