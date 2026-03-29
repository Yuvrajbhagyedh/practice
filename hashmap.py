lis=[12,3,4,5,5,34,3]

target=15
hashmap={}
for i in range(len(lis)):
    num=lis[i]
    diff=target-num


    if diff in hashmap:
        print(hashmap[diff],i)

    hashmap[num]=i    