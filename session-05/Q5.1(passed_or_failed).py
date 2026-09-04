'''
1 - Yek listi az nomreye daneshjooha darim , varede in list beshe va daneshjoohaye failed va pass ro dar biare

scores = [20,17,9 , 13, 7 , 20 , 18 , 3 , 1 , 14]

'''

scores = [20,17,9 , 13, 7 , 20 , 18 , 3 , 1 , 14]
passed=[]
failed=[]
for i in scores:
    if i>=10:
        passed.append(i)
    else:
        failed.append(i)

print("scores: ", scores)        
print("passed: ",passed)
print("failed: ",failed)        
        