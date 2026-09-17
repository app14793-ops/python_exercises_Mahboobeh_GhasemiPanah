def calculator(num1,num2,operation):
    if operation=="+":
        return num1+num2
    elif operation=="-":
        if num1>num2:
            return num1-num2
        else:
            return num2-num1
    elif operation=="/":
        if num2!=0:
            return num1/num2
        else:
            return "taghsim bar sefr namotabar ast"
    elif operation=="*":
        return num1*num2
    else:
        return None
    
    
num1=int(input("enter first number: "))
operation=input("enter operation: ") 
num2=int(input("enter second number: ")) 

print(calculator(num1, num2, operation))

  
    