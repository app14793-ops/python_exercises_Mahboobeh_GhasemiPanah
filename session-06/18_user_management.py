users = [ 
    { 
        "username": "ali", 
        "age": 25, 
        "city": "Tehran", 
        "active": True 
    }, 
    { 
        "username": "sara", 
        "age": 17, 
        "city": "Tabriz", 
        "active": True 
    } 
] 

def add_user(users:list, username:str, age:int, city:str,active:bool=True)->list:
    '''
    list karbarha va etelate marboot be karbare jadid ra be onvane voroodi migirad
    va karbare jadid ra be list ezafe mikonad va list jadid ra barmigardanad
    '''
    users.append({"username": username, 
    "age": age, 
    "city": city, 
    "active": active})
    return users

#print(add_user(users,"maryam",35,"shiraz"))


def find_user(users, username):
    
    for i in users:
        if i['username']==username:
            
            return i
    
    return None
       
#print(find_user(users, "maryam"))
#print(find_user(users, "reza"))  


def check_access(users, username):
    for i in users:
        
        if i["username"]==username:
            if i["age"]>=18 and i["active"]==True:
                
                return True
    
    return False


#print(check_access(users, "maryam"))
#print(check_access(users, "sara"))

def get_adult_users(users):
    adult_users=[]
    for i in users:
        if i["age"]>=18:
            adult_users.append(i["username"])
            
    return adult_users


#print(get_adult_users(users))        







      