class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap = self.laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()


    class laptop:
        def __init__(self):
            self.brand= "hp"
            self.cpu = "i4"
            self.ram = "4gb"

        def show(self):
            print(self.brand,self.cpu,self.ram)







s1= student("NAVIN",43)
s2= student("PAN",34)
print(s1.show())

lap1= student.laptop()
lap1.brand
