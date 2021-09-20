from headers import *
class ball:
    def __init__(self):
        self.__moving=False
        self.__x=57
        self.__togglex=1
        self.__fall=0
        self.__toggley=1
        self.__y=22
        self.__shape=np.array(
            [
                [Back.GREEN + 'O'+ Back.RESET]
            ]
        )
        self.__score=0
        self.__sx=1
        self.__sy=1
        self.__blks=0
        self.__exit=0
        self.__isdead=0

    
    def changedir(self,toggle):
        if(toggle=='1'):
            print("came to here x")
            self.__togglex*=-1
        if(toggle=='0'):
            print("came to here y")
            self.__toggley*=-1
        if toggle=='2':
            print("came to both bro")
            self.__togglex*=-1
            self.__toggley*=-1


    def setmove(self):
        self.__moving=True

    def present(self):
        if self.__moving:

            self.__x -= self.__togglex*self.__sx

            if self.__x<=0 or self.__x>=59:
                self.__togglex*=-1
            

            self.__y -= self.__toggley*self.__sy

            if self.__y<=0 or self.__y>=59:
                self.__toggley*=-1
    

    def getx(self):
        return self.__x
    def gety(self):
        return self.__y
    def getshape(self):
        return self.__shape
    
    def setscore(self):
        self.__score+=1
    def getscore(self):
        return self.__score

    def changex(self,temp):
        self.__sy-=temp
    def noblks(self):
        self.__blks+=1
    def getnoblks(self):
        return self.__blks
    def setnoblks(self):
        self.__blks=0
    def changefall(self):
        self.__fall+=1
    def getfall(self):
        return self.__fall
    def getexit(self):
        return self.__exit
    def setexit(self):
        self.__exit=1
    def refresh(self):
        self.__moving=False
        self.__sx=1
        self.__sy=1
        self.__blks=0
        self.__x=57
        self.__togglex=1
        self.__toggley=1
        self.__y=22
        self.__fall=0
        self.__isdead=0
    
    def isdead(self):
        return self.__isdead
    def makedead(self):
        self.__isdead=1
    def refresh2(self):
        self.__moving=False
        self.__sx=1
        self.__sy=1
        self.__x=57
        self.__togglex=1
        self.__toggley=1
        self.__y=22
        self.__isdead=0
    

    

