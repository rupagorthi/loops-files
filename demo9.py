even_list=[]
odd_list=[]
li=range(1,21)
for i in range(len(li)):
    if i/2 == 0:
        even_list.append(li[i])
    else:
        odd_list.append(li[i])
print (even_list)
print(odd_list)


