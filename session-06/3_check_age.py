def check_age(age:int)->str:
    if age>=18:
        return "Welcome"
    else:
        return "Access Denied"
    
age=int(input("enter age: "))  
print(check_age(age))  
    