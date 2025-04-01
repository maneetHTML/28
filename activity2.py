class fruit:
    taste="Sweet"#taste is a class variable 
    def __init__(self,name,color):
        self.nam=name
        self.col=color
    def info(self): #info is an user defined method
        print("fruit is healthy")
obj=fruit("Banana","yellow")
print(obj.nam)
print(obj.col,obj.taste)
obj.info()