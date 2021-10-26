class student:
    school= "newschhol"


    def __init__(self, m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def  getschoolname (cls):
        return cls.school
    @staticmethod
    def info():
        print("this in stdent class")



s1 = student(34,55,66)
s2= student(44,55, 78)
print(s1.avg())
print(student.getschoolname())
student.info()