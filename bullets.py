from headers import *
class bullets:
    def __init__(self,x,y):
        self.__bulx=x
        self.__buly=y
        self.__start=1
    def checkstart(self):
        return self.__start
    def getx(self):
        return self.__bulx
    def gety(self):
        return self.__buly
    def changex(self):
        self.__bulx-=1
    def changestart(self):
        self.__start=0

