products =[ 
    {'code': 'z1', 'name': 'zara cloth 121', 'price': 30}, 
    {'code': 'z2', 'name': 'zara shooes 100', 'price': 45}, 
    {'code': 'z3', 'name': 'zara cloth 451', 'price': 35}, 
    {'code': 'z4', 'name': 'zara shooes 300', 'price': 55}, 
    {'code': 'z5', 'name': 'zara shooes 231', 'price': 60}, 
    {'code': 'z6', 'name': 'zara bag 400', 'price': 110}, 
    {'code': 'z7', 'name': 'zara bag 500', 'price': 95} 
]

def gheymat_mahsool(products,code):
    for i in products:
        if i["code"]==code.strip().lower():
            return i["price"]
    return  "not found"

#print(gheymat_mahsool(products, "a"))
#print(gheymat_mahsool(products, "z1"))

def name_mahsool(products,code):
    for i in products:
        if i["code"]==code.strip().lower():
            return i["name"]
    return  "not found"

#print(name_mahsool(products, "a"))
#print(name_mahsool(products, "z1"))



def tuple_mahsool(products,code):
    for i in products:
        if i["code"]==code.strip().lower():
            return tuple(i.values())
    return  "not found"



#print(tuple_mahsool(products, "a"))
#print(tuple_mahsool(products, "z1"))






