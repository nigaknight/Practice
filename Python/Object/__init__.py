class Person():
    def __init__(self,name):
        self.name=name 
    def Sayhi(self):
        print("Hello,my name is {}".format(self.name))
P=Person('swaroop')
P.Sayhi()