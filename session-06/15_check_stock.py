products = { 
    "iphone": 5, 
    "macbook": 2, 
    "airpods": 0 
}

def check_stock(products:dict,product:str)->bool:
    if product in products:
        if products[product]>0:
            return True
        
    else:
        return False
    
print(check_stock(products, "laptop"))    
print(check_stock(products, "macbook"))   