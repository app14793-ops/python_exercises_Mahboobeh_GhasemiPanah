def name_cleaner(name):
    l=name.split(" ")
    new_l=[]
    for i in l:
        if i!="":
            new_l.append(i)
        
    new_name=""
    for i in new_l:
        new_name=new_name+" "+i
    return new_name.strip().lower().title()


    
n=input("name: ")
print(name_cleaner(n))


'''
khorooji:

    

name: MahBOOBEH    ghasemi     PANah

Mahboobeh Ghasemi Panah


'''