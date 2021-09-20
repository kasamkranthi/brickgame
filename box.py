from headers import *
class box:
    def __init__(self,rows,cols):
        self.__matrix=np.full((rows,cols),Back.BLACK + " " + Back.RESET)
        for i in range(cols-1):
            self.__matrix[0][i]=(Back.WHITE + '#' + Back.RESET)
        for i in range(cols):
            self.__matrix[rows-1][i]=(Back.WHITE + '#' + Back.RESET)
        for i in range(rows-1):
            self.__matrix[i][0]=(Back.WHITE + '#' + Back.RESET)
            self.__matrix[i][cols-1]=(Back.WHITE + '#' + Back.RESET)
    def getbox(self):
        return self.__matrix

