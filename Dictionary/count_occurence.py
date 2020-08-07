# word = "MISSISSIPPI"
# count = {"M":0,"I":0,"S":0,"P":0}
# for i in word:
# 	if i == "M":
# 		count['M'] = count['M']+1
# 	elif i == "I":
# 		count['I'] = count['I']+1
# 	elif i == "S":
# 		count['S'] = count['S']+1
# 	else:
# 		count['P'] = count['P']+1
# print (count)


list1=[2,6,24,54,2,6,2,24,5]
i=0
my_list=[]
while i<len(list1):
    j=0
    count=0 
    while j<len(list1):
        if list1[i]==list1[j]:
            # n=list1[i]
            count+=1
        j+=1
    if count==2:
        my_list.append(list1[i])
    i+=1
print(my_list)


