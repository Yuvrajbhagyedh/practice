lis=[1,2,3,45,6,4,23]
target=51

hashmap={}

for i in range(len(lis)):
    num=lis[i]
    diff=target-num

    if diff in hashmap:
        print(hashmap[diff],i)
    hashmap[num]=i    