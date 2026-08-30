'''
Q11----Mohasebe Soode foroshe mahsool
ma yek listi darim az gheymate kharide mahsoolat , va yek listi darim az ghyemate foroshe mahsoolat
shoma bayad soode har kodom az mahsoollat ro dar yek liste jodagane hesab konid


buy_prices = [100, 200, 150, 400]
sell_prices = [130, 250, 190, 500]

'''
buy_prices = [100, 200, 150, 400]
sell_prices = [130, 250, 190, 500]
sood=[]
for i in range(len(buy_prices)):
    sood.append(sell_prices[i]-buy_prices[i])
print("list sood :",sood)    


