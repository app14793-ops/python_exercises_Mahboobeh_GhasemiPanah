products =[ 
    {"code": "p1", "name": "Keyboard", "price": 50, "stock": 4}, 
    {"code": "p2", "name": "Mouse", "price": 30, "stock": 7}, 
    {"code": "p3", "name": "Monitor", "price": 250, "stock": 2}, 
    {"code": "p4", "name": "Headphone", "price": 80, "stock": 0} 
] 

cart=[]


def find_product(products:list, code:str)->dict:
    '''
    SUMMARY.
    list mahsoolat va code ra be onvane voroodi daryaft mikonad
    agar code mahsool mojood bood moshakhasate an ra barmigardanad
    agar nabood None barmigardanad

    Parameters
    ----------
    products : list
        DESCRIPTION.
    code : str
        DESCRIPTION.

    Returns
    -------
    dict
        DESCRIPTION.
    '''
    
    for i in products:
        if i['code']==code.strip().lower():
            return i
    
    return None
    
#print(find_product(products, "  P1")) 


def add_to_cart_1(products:list, cart:list, code:str)->list:
    '''
    SUMMARY.
    list mahsoolat va list kharid va code mahsool ra be onvane voroodi daryaft mikonad
    dar soorati ke mahsool mojood va mojoodiye an bishtar az sefr bashad 
    mahsool ra be sabade kharid ezafe mikonad
    va list jadid mahsoolat va list kharid ra barmigardanad

    Parameters
    ----------
    products : list
        DESCRIPTION.
    cart : list
        DESCRIPTION.
    code : str
        DESCRIPTION.

    Returns
    -------
    list
        DESCRIPTION.
    '''
    for i in products:
        if i["code"]==code and i["stock"]>0:
            cart.append(i)
            return cart
            
        
#print(add_to_cart_1(products, cart, "p1"))        


def add_to_cart_2(products:list, cart:list, code:str)->list:
    for i in products:
        if i["code"]==code and i["stock"]>0:
            i["stock"]-=1
            return products
            
            
            
#print(add_to_cart_2(products, cart, "p1"))            
            
            
def add_to_cart_3(products:list, cart:list, code:str):
    for i in products:
        if i["code"]==code and i["stock"]>0:
            i["stock"]-=1
            cart.append(i)
            return products,"*********",cart
            
            
                        
            
            
#print(add_to_cart_3(products, cart, "p1"))            
            
            
            
            
            
            