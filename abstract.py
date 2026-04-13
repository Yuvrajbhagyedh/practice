from abc import ABC,abstractmethod

class car(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def ram(self):
        pass

class tesla(car):
    def start(self):
        print("car started")
    def ram(self):
        print("random")
class rangerover(car):
    def start(self):
        print("car started")
    def ram(self):
        print("random")
   
s1=tesla()
s1.start()    
    