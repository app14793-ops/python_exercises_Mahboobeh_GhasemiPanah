'''

Q10----Tbadil celsius be fahrenheit

Ma yek dade darim az sensore yek karkhane ke dama ro be Celsius neveshte ast.

yek liste jadid besazid va in list bayaad adade farenheite ghabli ha bashad

formule tabdil : Farenheit = Celsius * 1.8 + 32

'''

celsius=[20,22,26,30,21]
fahrenheit=[]
for a in celsius:
    fahrenheit.append(a * 1.8 + 32)
print("fahrenheit is ",fahrenheit)    