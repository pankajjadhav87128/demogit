from abc import ABC,abstractmethod

class computer(ABC):

    @abstractmethod
    def process(self):
        pass
class laptop(computer):
    def process(self):
        print("this is laptop")

class whiteboard():
    def write(self):
        print("this is whiteborad")



class programer:
    def work(self,com):
        print("this is programer")
        com.process()


# com = computer()
# com.process()
com1=laptop()
com2 = whiteboard()
# com1.process()

prog1= programer()
prog1.work(com2)

