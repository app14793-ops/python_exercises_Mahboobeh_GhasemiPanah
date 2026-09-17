def average(my_list):
    sum=0
    count=0
    for num in my_list:
        sum+=num
        count+=1
    return sum/count        




my_list=[]
while True:
    a=input("enter number:")
    if a.isdigit():
        my_list.append(int(a))
    elif a=="exit":
            break
    else:
        print("faghat adad vared konid :\n baraye etmam exit vared konid: ")
        
        
print(average(my_list)) 