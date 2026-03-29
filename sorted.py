lis=[1,3,231,2771,9881]
flag=1
for i in range(len(lis)-1):
    if lis[i]>lis[i+1]:
        flag=0
        break
    else:
        flag=1

if flag==1:
    print("sorted")           
else:
    print("not ")     