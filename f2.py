strin="aabcaada"
freq={}

for i in strin:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1    
for i in strin:
    if freq[i]==1:
        print(i) 
        break       