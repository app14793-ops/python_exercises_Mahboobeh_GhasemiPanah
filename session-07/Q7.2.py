'''

2- yek dictionary az mahsolato mojodi ro darid , in ro 
be soorate vorodi yek atbe migire 
va do khoroji mide, do ta list mide ke yeki list esme 
mahsolati hast ke
mojodi darand , yeki list mahsolati ke mojodi 
nadaand 
inventory = { 
    "apple": 20, 
    "banana": 5, 
    "orange": 0, 
    "milk": 12, 
    "bread": 0 
} 

'''

def separate_products_by_availability(my_dict):
    availabe_products=[]
    unavailabe_products=[]
    for product,stock in my_dict.items():
        if stock==0:
            unavailabe_products.append(product)
        else:
            availabe_products.append(product)
    
    return availabe_products,unavailabe_products


inventory = { 
    "apple": 20, 
    "banana": 5, 
    "orange": 0, 
    "milk": 12, 
    "bread": 0}

availables,unavailables = separate_products_by_availability(inventory)
print("available products= ",availables)
print("unavailable products= ",unavailables)





'''
khorooji:
    
available products=  ['apple', 'banana', 'milk']
unavailable products=  ['orange', 'bread']


'''