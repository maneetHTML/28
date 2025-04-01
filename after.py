class dog:
    taste="pitbull"#taste is a class variable 
    taste="Amarica pitbull"#taste is a class variable 
    def __init__(self,name,age):
        self.nam=name
        self.ag=age
    def info(self): #info is an user defined method
        print("Dogs are cute.")
obj=dog("jam","2")
print("name : ",obj.nam,obj.taste)
print(obj.ag, "year old")


obj=dog("suff","3")
print("name : ",obj.nam,obj.taste)
print(obj.ag, "year old")

obj.info()