name_list=[]
for i in range(10):
    name=input('enter the name= ')
    name=name.lower()
    name=name[0].upper()+name[1:]
    name_list.append(name)
    
print(name_list)