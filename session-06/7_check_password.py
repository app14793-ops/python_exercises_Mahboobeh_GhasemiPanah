def check_password(password):
    if len(password)>=8 and password.isalnum():
        print("password sabt shod")
    else:
        print("password kamel nist")
        
        
        
        
        
def check_password_return_True_or_False(password):
    if len(password)>=8 and password.isalnum():
        return True
    else:
        return False
    
    
    
def check_password_strength(password):
    if len(password)>=8 and password.isalnum() and password.islower()==False and password.isupper()==False:   
        return 4
    elif len(password)>=8 and password.isalnum():
        return 3
    elif len(password)>=8:
        return 2
    elif len(password)<8:
        return 1
    
print(check_password_strength("12werfGGJJKJ555555SFVVaa"))    