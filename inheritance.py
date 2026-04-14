class animal:
    def sleep(slef):
        print("animal sleeps")
class human(animal):
    def eats(self):
        print("human also eats")        
class mamma:
    def mm(self):
        print("naan mammal")
class lion(human,mamma):
    def hunt(self):
        print("bete ado prani naanu")        

s1=lion()
s1.sleep()
s1.hunt()
s1.eats()

s1.mm()
print(lion.mro())