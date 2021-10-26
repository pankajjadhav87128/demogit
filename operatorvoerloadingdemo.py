class student:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def __add__(self,other):
        m1=self.m1 + other.m1
        m2= self.m2+ other.m2
        m3= self.m3 + other.m3
        return student(m1,m2,m3)
    def __gt__(self, other):
        r1=self.m1+self.m2
        r2 = other.m1+other.m2
        if r1>r2:
            return True
        else:
            return False

s1=student(18,20,30)
s2=student(12,22,35)
s3=s1+s2
print(s3.m1)
if s1>s2:
    print("s1 is grater thanss2")
else:
    print("not greater")