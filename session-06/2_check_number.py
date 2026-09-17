def even_or_odd(num:int)->str:
    '''
    adad ba type int ra be onvane voroodi migirad
    va moshakhas mikonad ke zoj ast ya fard
    '''
    if num%2==0:
        return "even"
    else:
        return "odd"
    
    
    
    
def even_or_odd2(num:int)->bool:
    if num%2==0:
        return True
    else:
        return False    
    
    
    
    
    
def positive_or_negative_or_zero(num:int)->str:
    if num>0:
        return "positive"
    elif num<0:
        return "negative"
    else:
        return "zero"
    
    
    
num=int(input("enter number: "))
print(even_or_odd(num))
print(even_or_odd2(num))
print(positive_or_negative_or_zero(num))    