'''
Optional 2 : tabe ei bename available_products benevisid ke dictionary mahsoolat ro daryaft konad , yani
vorodish yek dictioanry bashe mesle :

products = {
    "laptop": 3,
    "phone": 0,
    "tablet": 5,
    "mouse": 0,
    "keyboard": 2
}

va sepas , faghat name mahsolati ke mojodi anha bsih az sseft hast ro ba estefade az yield yeki yeki tolid konad (yani ye khoroji)

sepas yek geenrator besazido mahsolate mojod ro ba next() done done daryaft koni

'''

def  available_products(my_dict:dict):
    for name,stock in my_dict.items():
        if stock>0:
            yield name
        
products = {
    "laptop": 3,
    "phone": 0,
    "tablet": 5,
    "mouse": 0,
    "keyboard": 2
}

            
my_generator=iter(available_products(products))

print(next(my_generator))

print(next(my_generator))

print(next(my_generator))


'''
khorooji:
    
laptop
tablet
keyboard


'''    


            
            