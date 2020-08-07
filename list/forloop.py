list1=[2,0,5,4,9,0,9,7,0,9]
index=0
list2=[]
while index<len(list1):
    if list1[index]<1:
        list1.remove(list1[index])
        list1.append(0)
    index+=1
print(list1)


list1=[2,0,5,4,9,0,0,7,0,9]
for i in range(len(list1)):
    if list1[i]<1:
        list1.remove(list1[i])
        list1.append(0)
print(list1)




