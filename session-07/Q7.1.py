'''
 
1- yek dictionary aZ mahsoolat darim  
products = { 
'laptab': 1200, 
'phone': 800, 
'tablet': 500, 
'headphone': 150, 
'mouse': 50 
} 
Chandin tabe benevisid ke in dictionary ro besoorate 
vorodi begire 
va - bishtarin gheymat ro pas bede - esme mahsoli ke bishtarin gheymat ro dare pas 
bede - hamin 2 taro baraye **kamtarin** ham anjam 
dahid - jame kole mahsoolat ro pas bede - miangine kole mahsolat ro pas bede


'''



def find_max_price(my_dict):
    max_price=list(my_dict.values())[0]
    for i,j in my_dict.items():
       if j>max_price:
          max_price=j
          
          
    return max_price     
           
def find_product_with_max_price(my_dict):
    max_price=list(my_dict.values())[0]
    max_product=list(my_dict.keys())[0]
    for i,j in my_dict.items():
        if j>max_price:
            max_price=j
            max_product=i
      
    return max_product

    

def find_min_price(my_dict):
    min_price=list(my_dict.values())[0] 
    for i,j in my_dict.items():
        if j<min_price:
            min_price=j
            
      
    return min_price



def find_product_with_min_price(my_dict):
    min_price=list(my_dict.values())[0]
    min_product=list(my_dict.keys())[0]
    for i,j in my_dict.items():
        if j<min_price:
            min_price=j
            min_product=i
      
    return min_product

def calculate_total_price(my_dict):
    total_price=list(my_dict.values())
    total_sum=0
    for i in total_price:
        total_sum+=i
    return total_sum    

def calculate_total_price_with_sum(my_dict):
    total_price=list(my_dict.values())
    return sum(total_price)



def calculate_average_price(my_dict):
    total_price=list(my_dict.values())
    total_sum=0
    count=0
    for i in total_price:
        total_sum+=i
        count+=1
    return total_sum/count

def calculate_average_price_with_sum_and_len(my_dict):
    total_price=list(my_dict.values())
    return sum(total_price)/len(total_price)
    

products = { 
'laptab': 1200, 
'phone': 800, 
'tablet': 500, 
'headphone': 150, 
'mouse': 50 
}
 
#print(list(products.values()))

print(find_max_price(products))
print(find_product_with_max_price(products))
print(find_min_price(products))
print(find_product_with_min_price(products))
print(calculate_total_price(products))
print(calculate_total_price_with_sum(products))
print(calculate_average_price(products))
print(calculate_average_price_with_sum_and_len(products))