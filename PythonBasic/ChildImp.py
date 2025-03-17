from OopsDemo import Calculator


class ChildImp:
    def getCompleteData(self):
        pass


class ChildImp(Calculator):
    print("This is a child class")
    num2 = 200

    def __init__(self):
        Calculator.__init__(self,10,2)
        
    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()

childobj = ChildImp()
print(childobj.getCompleteData())