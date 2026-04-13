class student:
    def __init__(self,name,mark1,mark2,mark3):
        self.name=name
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3

    def average(self):
        a=self.mark1
        b=self.mark2
        c=self.mark3
        avg=(a+b+c)/3

        print(avg)
    @staticmethod
    def hello():
        print("hello")    
        

        
s1=student("yuvraj",99,98,97)
s1.average()
s1.hello()
       