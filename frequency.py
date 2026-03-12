num=[12,334,12,43,12,43,34,23,34]
freq={}

for i in num:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1    


print(freq)        