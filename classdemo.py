class computer:

    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram


    def config(self):
        print("15gb", self.cpu, self.ram)


com1= computer(10,11)
com2= computer(12,13)
print(type(com1))
com1.config()
computer.config(com1)
computer.config(com2)
