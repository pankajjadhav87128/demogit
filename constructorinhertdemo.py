class A:

    def __init__(self):
        print("printa")
    def feature1(self):
        print(" feature1 working")
    def feature2(self):
        print(" feature2 working")

class B():
    def __init__(self):
        super().__init__()
        print("printb")
    def feature1(self):
        print(" feature3 working")
    def feature4(self):
        print(" feature4 working")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("printC")
    def feat(self):
        super().feature2()



# a1=A()
# a1.feature1()
# a1.feature2()
a2=C()
# b1 = B()
# b1.feature1()
# b1.feature2()
# b1.feature3()
# b1.feature4()
a2.feat()