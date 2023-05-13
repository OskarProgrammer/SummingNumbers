
class Sum:
    """
    A class that sums the numbers in the given list

    params: list -> list of integers or floats numbers
    returns: integer or float -> that show the sum of the numbers 
    """

    def __init__(self,list:list,name:str):
        self.list = list
        self.len = len(list)
        self.name = name
        self.suma = 0 
        for x in range (0,self.len):
            liczba = self.summing(x)
            self.suma +=liczba
    
    def setName(self,name:str):
        self.name = name
    
    def summing(self,index:int):
        return self.list[index]

    def getAnswer(self):
        return self.suma
    
    def getName(self):
        return self.name
