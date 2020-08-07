dic = {
    'ball': 'red',
    'bat': 4,
    'wicket': 8,
    'ball': 'green',
    'bat': 3
}
new_dic={}
for key,value in dic.items():
  if value not in new_dic.values():
    new_dic[key] = value
print(new_dic)