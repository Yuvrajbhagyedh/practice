lis=[12,3,3,43,54,43]

left=0
right=len(lis)-1

while(left<right):
    temp=lis[left]
    lis[left]=lis[right]
    lis[right]=temp
    left+=1
    right-=1

print(lis)    

