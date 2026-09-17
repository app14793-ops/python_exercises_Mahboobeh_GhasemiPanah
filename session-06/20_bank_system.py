accounts=[ 
    { 
        "username": "ali", 
        "password": "1234", 
        "balance": 5000, 
        "transactions": [] 
    }, 
    { 
        "username": "sara", 
        "password": "5678", 
        "balance": 8000, 
        "transactions": [] 
    } 
] 

def login(accounts:list, username:str, password:str):
    '''
    dar hesab ha jostojoo mikonad 
    agar name karbari vojood nadasht None barmigardanad
    agar name karbari vojood dasht 
    barasi mikonad ke password dorost ast ya na 
    agar dorost bood True 
    agar nabood False barmigardanad
    '''
    
    for i in accounts:
        if i["username"]==username:
            if i["password"]==password:
                
                return True
            else:
                
                return False
    else:
                    
            return None
        

#u=input("usernam: ")        
#p=input("password: ")  

#print(login(accounts, u, p)) 


def withdraw(account:dict,mablagh:int)->dict:
    '''
    SUMMARY.
    hesab va mablagh ra be onvane voroodi migirad 
    sepas mablagh ra az mojoodi hesab kam mikonad va hesab ra berooz rasani mikonad

    Parameters
    ----------
    username : str
        DESCRIPTION.
    mablagh : int
        DESCRIPTION.

    Returns
    -------
    dict
    '''
    
    account["balance"]=account["balance"]-mablagh
    account["transactions"].append({mablagh:"withdraw"})
    return account
     


#print(withdraw(accounts[0], 2000))

def deposit(account:dict,mablagh:int)->dict:
    '''
    SUMMARY.
    hesab va mablagh ra be onvane voroodi migirad 
    sepas mablagh ra be mojoodi hesab ezafe mikonad va hesab ra beroozrasani mikonad

    Parameters
    ----------
    username : str
        DESCRIPTION.
    mablagh : int
        DESCRIPTION.

    Returns
    -------
    dict
    '''
    
    account["balance"]=account["balance"] + mablagh
    account["transactions"].append({mablagh:"deposit"})
    return accounts


deposit(accounts[0], 3000)
withdraw(accounts[0], 100)


def show_transactions(account):
    for i in account["transactions"]:
        print(i)
        
        
show_transactions(accounts[0])        



def transfer(accounts:list, sender_username:str, receiver_username:str, amount:float())->list:
    '''
    SUMMARY.
    liste hesab ha va do name karbari be onvane voroodi migirad
    aval check mikonad ke name karbari ferestande dar liste hesabha mojood bashad
    bad name karbariye girande ra check mikonad
    dar soorati ke dorost bashad bardasht az hesab anjam mishavad

    Parameters
    ----------
    accounts : list
        DESCRIPTION.
    sender_username : str
        DESCRIPTION.
    receiver_username : str
        DESCRIPTION.
    amount : float
        DESCRIPTION.

    Returns
    -------
    list
        DESCRIPTION.
    '''
    for i in accounts:
        if i["username"]==sender_username:
            for j in accounts:
                if j["username"]==receiver_username:
                    i["balance"]=i["balance"]-amount
                    i["transactions"].append({amount:"withdraw"})
                    j["balance"]=j["balance"]+amount
                    j["transactions"].append({amount:"deposit"})
                    #print(sender_username,"balance is: ",i["balance"])
                    #print(receiver_username,"balance is : ",j["balance"])
                    return accounts
    return None




#print(transfer(accounts, "ali", "sara", 1000))    
  
   
    
def get_balance(account:dict,vahed:str="USD")->int:
    '''
    SUMMARY.
    hesab va vahed pool ra be onvane voroodi daryaft mikonad
    agar vahed pool barabar ba rial bood mojoodi hesab ra dar 2500000
    zarb mikonad va barmigardanad
    ama agar vahed pool be tabe dade nashode bood
    USD dar nazar migirad va faghat mojoodi ra barmigardanad

    Parameters
    ----------
    account : dict
        DESCRIPTION.
    vahed : str, optional
        DESCRIPTION. The default is "USD".

    Returns
    -------
    int
        DESCRIPTION.
    '''
    if vahed.upper()=="RIAL":
        return (account["balance"] * 2500000)
    else:    
        return account["balance"]  
    
        
#print(get_balance(accounts[1],"rial"))    
 
    
    
    
    
    
    
    
    
    
