class ACl:
    name = "class A"
    value = 3
    def __init__(self): pass
        #print("init ACl")
        #self.value = 1
        #return
    def print(self):
        print("Name = ",  self.name,  "\nValue = ",  self.value)

class BCl(ACl):
    def __init__(self): pass

acl = ACl()
