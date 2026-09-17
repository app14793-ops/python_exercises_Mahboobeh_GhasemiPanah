def check_email(email):
    if email.find("@")!=-1 and email.find(".com")!=-1 and email.find(" ")==-1:
        return True
    else:
        return False
    
    
print(check_email("mhbb.1388@gmail.com"))
print(check_email("zjhgvfjksadjvasdjkv"))   
    