'''
optional3 : yek tabe be name create_profile benevisid ke do vorodie ejbari begire bename name,age 
alave bar in , betavanim har che tedade etelate ezafi ro ba estefade az **kwargs begire.

masalan : city, job, emnail , harchiii

khob tabe bayad inkaro kone :
- namo sen ro jnamayesh bede
- tamame etelaate ezafi ro namayesh dahad
- tedade etelaate ezafi ro chap kone
- agar city vojod dasht ,s hahro ro jodagone neshon bede
- agar email vojod nadasht ebenvise : email not provided
dar enteha ham tamame etelaate karbar ro dakhele yek dictionary jadid bezare o return kone

'''

def create_profile(name,age,**kwargs):
    print(f"name:{name} age:{age}")
    
    
    for i,j in kwargs.items():
        print(i,j)
        
    
    print(len(kwargs))
    
    
    if "city" in kwargs:
        print("city is ",kwargs["city"])
    
        
    if "email" not in kwargs:
        print("email not provided")
    
        
    profile={"name":name,"age":age,}
    profile.update(kwargs)
    return profile
        
create_profile("ali",25,phone="0917",city="shiraz")

print("**************************")


profile= create_profile("maryam",35,city="tehran",email="maryam@gamail.com") 
print(profile)


'''
name:ali age:25
phone 0917
city shiraz
2
city is  shiraz
email not provided
**************************
name:maryam age:35
city tehran
email maryam@gamail.com
2
city is  tehran
{'name': 'maryam', 'age': 35, 'city': 'tehran', 'email': 'maryam@gamail.com'}

''' 