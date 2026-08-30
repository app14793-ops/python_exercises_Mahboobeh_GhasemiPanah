'''
Q5----Adade fard

In mesal az se bakhsh a,b,c tashkil shode
Adade farde beyne 15 ta 115 ro  a)chap konid b)dakhele yek list berizid c)beshmorid

'''
l=[]
count=0
for i in range(16,115):
    if i%2!=0:
        print(i)
        l.append(i)
        
        count=count+1
        
print("list adade farde beyne 15 ta 115 =", l)       
print(count,"ta adade fard beyne 15 ta 115 vojud darad")