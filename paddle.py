from headers import *
class paddle:
    def __init__(self):
    
        self.__shape1=np.array(
            [
                [Back.BLUE+'-'+ Back.RESET,Back.BLUE+'-'+ Back.RESET,Back.BLUE+'-'+ Back.RESET,Back.BLUE+'-'+ Back.RESET,Back.BLUE+'-'+ Back.RESET,Back.BLUE+'-'+ Back.RESET,Back.BLUE+'-'+ Back.RESET,Back.BLUE+'-'+ Back.RESET,Back.BLUE+'-'+ Back.RESET,Back.BLUE+'-'+ Back.RESET,Back.BLUE+'-'+ Back.RESET,Back.BLUE+'-'+ Back.RESET],
               

            ]
        )
        self.__myx=58
        self.__myy=20
    def getshape(self):
        return self.__shape1
    
    def setpos(self,x,y):
        self.__myx=x
        self.__myy=y
    
    def checkhit(self,bb):
        x=bb.getx()
        y=bb.gety()
        if x>self.__myx-1: 
            if  y>=self.__myy and y<=self.__myy+12:
                if self.__myy-y<1:
                    bb.changedir("1")
                    bb.changedir("0")
                if y>self.__myy+11:
                    bb.changedir("1")
                    bb.changedir("0")
                else:
                    temp=y-self.__myy-6
                    temp=temp/6
                    bb.changefall()
                    bb.changex(temp)
                    bb.changedir("1")
            else:
                    bb.makedead()
                    print("came here")
    def getx(self):
        return self.__myx
    def gety(self):
        return self.__myy
