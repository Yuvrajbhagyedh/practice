s=-121
temp=s
rev=0
if s<0:
    print("its not ") 
    

while(temp>=0):
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10

if rev==s:
    print("palindrome number")
else:
    print("not")            