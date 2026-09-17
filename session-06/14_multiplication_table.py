def countdown(num:int):
    for i in range(11):
        print(num,"*",i,"=",i*num)




num=int(input("enter number: "))
countdown(num)