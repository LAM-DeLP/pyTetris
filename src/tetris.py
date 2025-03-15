import random
import numpy

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
        pass

class Board:
    def __init__(self,length,height):
        self.grid = numpy.zeros((height,length))
        self.clearStandard = length

    def assignMino(self,x,y,assignList:list):
        for i in range(len(assignList)):
            verlist = assignList[i]
            self.grid[verlist[1]+y][verlist[0]+x] = 1

    def clearLine(self):
        pass

class Game:
    pass

if __name__ == '__main__':
    mino1 = Mino(3)
    mino1.self_generate()
    board1 = Board(10,20)
    board1.assignMino(3,4,mino1.minoVer)
    print(mino1.minoVer)
    print(board1.grid)

    #回転も移動も何か返して妥当性を判定する

    

