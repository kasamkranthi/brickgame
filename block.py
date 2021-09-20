from headers import *
class block:
    def __init__(self,typ):
        self.__visible=True
        self.__myx=0
        self.__myy=0
        self.__change=1
        self.__type=typ
        self.__ct=1
        self.__ispow=0
        temp=random.randint(0,10)
        if temp==1 or temp==2 or temp==3:
            self.__ispow=1
        self.__ispowon=0
        self.__powx=0
        self.__powy=0
        self.__shape1=np.array(
            [
                [Back.BLUE+'*',Back.BLUE+'-',Back.BLUE+'-',Back.BLUE+'-',Back.BLUE+'-',Back.BLUE+'-',Back.BLUE+'-',Back.BLUE+'-',Back.BLUE+'-',Back.BLUE+'-',Back.BLUE+'-',Back.BLUE+'*'],
                [Back.BLUE+'|',Back.BLUE+' ',Back.BLUE+' ',Back.BLUE+' ',Back.BLUE+' ',Back.BLUE+' ',Back.BLUE+' ',Back.BLUE+' ',Back.BLUE+' ',Back.BLUE+' ',Back.BLUE+' ',Back.BLUE+'|'],
                [Back.BLUE+'*',Back.BLUE+'-',Back.BLUE+'-',Back.BLUE+'-',Back.BLUE+'-',Back.BLUE+'-',Back.BLUE+'-',Back.BLUE+'-',Back.BLUE+'-',Back.BLUE+'-',Back.BLUE+'-',Back.BLUE+'*']

            ]
        )
        self.__shape2=np.array(
            [
                [Back.RED+'*',Back.RED+'-',Back.RED+'-',Back.RED+'-',Back.RED+'-',Back.RED+'-',Back.RED+'-',Back.RED+'-',Back.RED+'-',Back.RED+'-',Back.RED+'-',Back.RED+'*'],
                [Back.RED+'|',Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+' ',Back.RED+'|'],
                [Back.RED+'*',Back.RED+'-',Back.RED+'-',Back.RED+'-',Back.RED+'-',Back.RED+'-',Back.RED+'-',Back.RED+'-',Back.RED+'-',Back.RED+'-',Back.RED+'-',Back.RED+'*']

            ]
        )
        self.__shape3=np.array(
            [
                [Back.WHITE+'*',Back.WHITE+'-',Back.WHITE+'-',Back.WHITE+'-',Back.WHITE+'-',Back.WHITE+'-',Back.WHITE+'-',Back.WHITE+'-',Back.WHITE+'-',Back.WHITE+'-',Back.WHITE+'-',Back.WHITE+'*'],
                [Back.WHITE+'|',Back.WHITE+' ',Back.WHITE+' ',Back.WHITE+' ',Back.WHITE+' ',Back.WHITE+' ',Back.WHITE+' ',Back.WHITE+' ',Back.WHITE+' ',Back.WHITE+' ',Back.WHITE+' ',Back.WHITE+'|'],
                [Back.WHITE+'*',Back.WHITE+'-',Back.WHITE+'-',Back.WHITE+'-',Back.WHITE+'-',Back.WHITE+'-',Back.WHITE+'-',Back.WHITE+'-',Back.WHITE+'-',Back.WHITE+'-',Back.WHITE+'-',Back.WHITE+'*']

            ]
        )
        
    def getshape(self):
        if self.__type==1:
            return self.__shape1
        elif self.__type==2:
            return self.__shape2
        elif self.__type==3:
            return self.__shape3
        elif self.__type==4:
            if self.__ct==1:
                return self.__shape1
            elif self.__ct==2:
                return self.__shape2
            elif self.__ct==3:
                return self.__shape3
            
            
    def store_my_cods(self,x,y):
        self.__myx=x
        self.__myy=y
    
    def checkhit(self,bb,x,y):
        
        if self.__visible:
            if self.__myx>=56:
                bb.setexit()
            if x>=self.__myx and x<=(self.__myx + 3) and y>=self.__myy and y<=(self.__myy + 12):
                if(self.__type==4):
                    self.__type=self.__ct
                    if self.__type==3:
                        bb.noblks()
                if self.__type==1:
                    os.system("aplay 2.wav -q &")
                    os.system("powerup.mp3 -q &")
                    if self.__ispow:
                        self.__ispowon=1
                        self.__powx=self.__myx+3
                        self.__powy=self.__myy+6
                    bb.setscore()
                    bb.noblks()
                    flag="1"
                    if x==self.__myx or x==self.__myx+11:
                        flag="0"
                    else:
                        flag="1"
                    bb.changedir(flag)
                    self.__visible=False
                
                elif self.__type==2:
                    bb.setscore()
                    flag="1"
                    if x==self.__myx or x==self.__myx+11:
                        flag="0"
                    else:
                        flag="1"
                    self.__type=1
                    
                    bb.changedir(flag)
                    
                elif self.__type==3:
                    flag="1"
                    if x==self.__myx or x==self.__myx+11:
                        flag="0"
                    else:
                        flag="1"
                    
                    bb.changedir(flag)
            if self.__type==4:
                self.__ct+=1
                self.__ct=self.__ct%3+1

        


    def checkhit2(self,bb,x,y,blt):
    
        
        
        if self.__visible:
            if self.__myx>=56 :
                bb.setexit()
            if x>=self.__myx and x<=(self.__myx + 3) and y>=self.__myy and y<=(self.__myy + 12):
                blt.changestart()
                if(self.__type==4):
                    self.__type=self.__ct
                if self.__type==1:
                    if self.__ispow:
                        self.__ispowon=1
                        self.__powx=self.__myx+3
                        self.__powy=self.__myy+6
                    bb.setscore()
                    bb.noblks()
                    
                    self.__visible=False
                
                elif self.__type==2:
                    bb.setscore()
                    
                   
                    self.__type=1
                    
                  
                    
                elif self.__type==3:
                    self.__type=3
            if self.__type==4:
                self.__ct+=1
                self.__ct=self.__ct%3+1
            
            
    def is_present(self):
        return self.__visible

    def getpowon(self):
        return self.__ispowon
    
    def getx(self):
        return self.__powx
    def gety(self):
        return self.__powy
    def changex(self):
        self.__powx+=1
        

