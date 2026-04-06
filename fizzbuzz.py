num=int(input("enter a number"))

if num%3==0 and num%7==0:
    print("Fizzpop")
elif num%3==0 and num%5==0:
    print("FizzBuzz")
elif num%5==0:
    print("Buzz")
elif num%3==0:
    print("Fizz")        
elif num%7==0:
    print("pop")
else:
    print("not divisible by any")