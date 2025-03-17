#classes prototype
# methods,class variables,instance variables,construnctor
class Calculator:
    num = 100

    #default constructor
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("this is a constructor")

    def getData(self):
        print("I am executing method in class")

    def Summation(self):
        return self.a + self.b + self.num

obj = Calculator(2,3)
obj.getData()
print(obj.num)
print(obj.Summation())

obj1 = Calculator(4,5)
obj1.getData()
print(obj1.num)
print(obj1.Summation())