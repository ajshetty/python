
class player ():
    def __init__(self, name, age, sex, weight):
        self.name = name
        self.age = age 
        self.sex = sex
        self.weight = weight 
    
    def get_age(self):
        return print(self.name + " has a age of " + str(self.age))
    
p1 = player("AKshit", 12, "M", 150)
print(p1.get_age())
p2 = player("Bonny" ,232, "F", 556)
print(p2.get_age())





