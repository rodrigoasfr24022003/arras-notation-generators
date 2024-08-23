class AWPPolygon():
    def __init__(self,sides,size):
        self.sides=sides
        self.size=size
    def getSides(self):
        return self.sides
    def getSize(self):
        return self.size
    def setSides(self,sides):
        self.sides=sides
    def setSize(self,size):
        self.size=size
    def __str__(self) -> str:
        return '⟨'+str(self.sides)+', '+str(self.size)+'⟩'