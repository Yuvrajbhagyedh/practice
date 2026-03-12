num=153
lenth=len(str(num))
temp=num
sum=0

while(temp>0):
    digit=temp%10
    sum=sum+digit**lenth
    temp=temp//10

if num==sum:
    print("armstrong number")
else:
    print("not an armstrong number")    
