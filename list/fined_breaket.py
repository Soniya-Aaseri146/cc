
# def check(my_string): 
#     brackets = ['()', '{}', '[]'] 
#     while any(x in my_string for x in brackets): 
#         for br in brackets: 
#             my_string = my_string.replace(br, '') 
#     return not my_string 

 
# string=input("Enter the brackets:")
# print(string, "-", "true" 
#       if check(string) else "false") 


breckets=input("Enter the breckets:")
string=["[]","{}","()"]
if breckets in string:
    print("true")
else:
    print("false")





