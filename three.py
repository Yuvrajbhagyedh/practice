#duplicates


num=[12,34,23,12,34,232,43]

uniq=[]

for i in num:
    if i not in uniq:
        uniq.append(i)
print(uniq)