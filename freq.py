char="adddacddsad"

freq={}

for i in char:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
    
for i in freq:
    if freq[i]==1:
        print(i)
        break
            