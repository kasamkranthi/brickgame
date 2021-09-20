from headers import *
from paddle import paddle
from time import sleep
from keys_hit import keys_hit
from ball import ball
from block import block
from bullets import bullets


class board:
    def __init__(self,rows,cols):
        self.__rows=rows
        self.__cols=cols
        self.__addtemp=0
        self.__matrix=np.full((rows,cols),Back.BLACK + " "+Back.RESET)
        
        self.__matrix[0,:] = Back.WHITE+" "+Back.RESET 
        self.__matrix[rows-1,:] = Back.WHITE+" "+Back.RESET
        self.__rows=rows
        self.__matrix[:,0] = Back.WHITE+" "+Back.RESET
        self.__cols=cols
        self.__matrix[:,cols-1] = Back.WHITE+" "+Back.RESET
        self.__bts=[]
        self.__len=0
        self.__ispower=0
        self.__bulletshape=np.array(
            [
                [Back.RED + 'O'+ Back.RESET]
            ]
        )
        self.__powshape=np.array(
            [
                [Back.YELLOW + 'O'+ Back.RESET]
            ]
        )

    def refresh(self):
        self.__matrix=np.full((self.__rows,self.__cols),Back.BLACK + " "+Back.RESET)
        rows=self.__rows
        cols=self.__cols
        self.__matrix[0,:] = Back.WHITE+" "+Back.RESET 
        self.__matrix[rows-1,:] = Back.WHITE+" "+Back.RESET
        rows=self.__rows
        self.__matrix[:,0] = Back.WHITE+" "+Back.RESET
        cols=self.__cols
        self.__matrix[:,cols-1] = Back.WHITE+" "+Back.RESET

    def printmarix(self):
       
        for row in self.__matrix:
            print("".join(row),file=sys.stdout,flush = True)
        


    def addpaddle(self,paddle,x,y,len):
        self.__matrix[x:x+1,y:y+len]=paddle.getshape()
        paddle.setpos(x,y)

    def addblock(self,block,x,y,len,paddle):
        if block.is_present():
            self.__matrix[x:x+3,y:y+len]=block.getshape()
        block.store_my_cods(x,y)
        if block.getpowon():
            x=block.getx()
            y=block.gety()
            self.__matrix[x:x+1,y:y+1]=self.__powshape
            block.changex()
            x_p=paddle.getx()
            y_p=paddle.gety()
            if x==x_p and y>=y_p and y<=y_p+12:
                self.__ispower=1

    def checkpow(self):
        return self.__ispower
    
    def getball(self,bb):
        x=round(bb.getx())
        y=round(bb.gety())
        self.__matrix[x:x+1,y:y+1]=bb.getshape()


    
    def addbullet(self,paddle):
        
        x=paddle.getx()-2
        y=paddle.gety()
        self.__bts.append(bullets(x,y+1))
        self.__bts.append(bullets(x,y+11))
        self.__len+=2
    def bullethit(self):
        len=self.__len
        for i in range(len):
            chk=self.__bts[i].checkstart()
            if(chk):
                x=self.__bts[i].getx()
                y=self.__bts[i].gety()
                self.__matrix[x:x+1,y:y+1]=self.__bulletshape
                self.__bts[i].changex()
    
    def checkhit(self,bb,blk):
        len=self.__len
        for i in range(len):
            chk=self.__bts[i].checkstart()
            if(chk):
                x=self.__bts[i].getx()
                y=self.__bts[i].gety()
                blk.checkhit2(bb,x,y,self.__bts[i])
    def removeblts(self):
        self.__bts=[]
    def background(self):
        self.__matrix[0:self.__rows,0:self.__cols]=self.__box.getbox()
    
    def changeurpow(self):
        self.__ispower=0
        

    


