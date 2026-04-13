class animal:
    def sound(self):
        print("animals make sound")
class cat(animal):
    def sound(self):
        print("meowws")
class dog(animal):
    def sound(self):
        print("barkss")        

s2=animal()
s1=cat()
s1.sound()
s2.sound()            