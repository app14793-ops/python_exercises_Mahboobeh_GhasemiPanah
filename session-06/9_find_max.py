def find_max(my_list):
    max=0
    for num in my_list:
        if num>max:
            max=num
    return max        

my_list=[]
while True:
    a=input("enter number:")
    if a.isdigit():
        my_list.append(int(a))
    elif a=="exit":
            break
    else:
        print("faghat adad vared konid :\n baraye etmam exit vared konid: ")
        
        
print(find_max(my_list))        