from abc import ABC,abstractmethod

class car(ABC):
    @abstractmethod
    def start(self):
        pass

class tesla(car):
    def start(self):
        print("car started")
class rangerover(car):
    def start(self):
        print("range rover started")
s1=tesla()
s1.start()    
s2=rangerover()
s2.start()    