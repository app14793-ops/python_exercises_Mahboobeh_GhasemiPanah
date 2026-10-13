'''
4- yek tabe benevisid ke yek listi az tuple ha dare o ino be onvane vorodi migirie

sales = [
    ("Ali", "Laptop", 1200),
    ("Sara", "Phone", 800),
    ("Ali", "Phone", 800),
    ("Reza", "Laptop", 1200),
    ("Sara", "Laptop", 1200),
    ("Ali", "Mouse", 50)
]


- yek tabe benvisid  ke khoroji yek dictionary bede ke har fard yek key hast va jolosh jame kharidesho zade
- yek tabe benevisid ke khorojish yek dictionary bede ke key ha esme mahsolat bashe va jolosh tedde foroshe mahsolat
- yek tabe benevsiid ke khoroji ye adad bede ke majhmooe daramade foroshgah hast


'''
def customer_purchases(my_list):
    totla_purchases={}
    for i in my_list:
        if i[0] not in totla_purchases:
            totla_purchases[i[0]]=i[2]
        else:
            totla_purchases[i[0]] += i[2]
    return totla_purchases

def product_sales_count(my_list):
    count={}
    for i in my_list:
        if i[1] not in count:
            count[i[1]]=1
        else:
            count[i[1]]+=1
    return count        

def total_revenue(my_list):
    total_sum=0
    for i in my_list:
        total_sum += i[2]
    return total_sum    


sales = [
    ("Ali", "Laptop", 1200),
    ("Sara", "Phone", 800),
    ("Ali", "Phone", 800),
    ("Reza", "Laptop", 1200),
    ("Sara", "Laptop", 1200),
    ("Ali", "Mouse", 50)
]

print(customer_purchases(sales))
print(product_sales_count(sales))
print(total_revenue(sales))



'''

khorooji: 
    
    
{'Ali': 2050, 'Sara': 2000, 'Reza': 1200}
{'Laptop': 3, 'Phone': 2, 'Mouse': 1}
5250

'''