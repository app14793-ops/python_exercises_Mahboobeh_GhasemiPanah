def order():
    foods={"pizza":1000,"burgur":800,"pasta":1200}
    order=[]
    while True:
        print(foods)
        o=input("esme ghaza re vared konid: ")
        if o.strip().lower() in foods.keys():
           order.append(o)
        elif o=="order":
            return order
            break
        else:
            print("dar menu mojood nist!\n","barye payane sefaresh order ra vared konid")
            
            
            
print(order())        