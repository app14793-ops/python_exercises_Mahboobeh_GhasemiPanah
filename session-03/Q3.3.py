'''
q3.3. yek machine hesab besazid , 
yek adade (number1) yek adade number2
yechizi begire operation (jam , tafrigh,taghsim,zarb)
anjam bede print kone
'''

num1=float(input("adad aval ra vared kon: "))
operator=input("amalgar ra vared kon (jam,tafrigh,zarb,taghsim): ")
num2=float(input("adad dovom ra vared kon: "))


if operator.lower().strip()=="jam":
    print(num1+num2)
elif operator.lower().strip()=="tafrigh":
    if num1>num2:
        print(num1-num2) 
    else:
        print(num2-num1)
elif operator.lower().strip()=="taghsim":
    if num2==0:
        print("taghsim bar serf na motabar ast") 
    else:
        print(num1/num2)
       
elif operator.lower().strip()=="zarb":
    print(num1*num2)     
