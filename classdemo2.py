class computer:

    wheels = 4
    def __init__(self):
        self.name="navin"
        self.age=15
    def update(self):
        self.age=30
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            print("they are diff")
            return False

c1 = computer()
c1.age =10
c2 = computer()
if c1.compare(c2):
     print("they ar e same")
computer.wheels=5

print(c1.name)
print(c2.name)
print(c1.name,c1.age,c1.wheels)
print(c2.name,c2.age,c2.wheels)