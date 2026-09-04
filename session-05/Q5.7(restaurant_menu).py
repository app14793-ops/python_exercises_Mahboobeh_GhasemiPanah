'''
7 - yek liste ghaza darim va menuye resturan hast , in list esmesh hast foods , 
aval be karbar hamash namayesh dade beeshe va done done karbar hey entekhab kone, 
har zamani ke karbar nevesht ('order') dige azash esme ghaza porside nashe,
 balke kole list ba estefade az for, besoorate factor behesh namayesh dade besh
'''   
foods=["chelokabab","chelomorgh","chelomahi","cheloghime","kalampolo"]
gheymat=[1200,1500,2000,1000,1000]
order=[]
tedad=[]
print("chelokabab","chelomorgh","chelomahi","cheloghime","kalampolo")
while True:
    
    f=input("esme ghaza ra verd kon: ")
    
    if f.lower().strip() in foods:
        t=int(input("tedad ghaza ra verd kon: "))
        order.append(f)
        tedad.append(t)

    elif  f=="order":
        break
    else:
        print("dar menu mojood nist")
        print("baraye sefaresh *order* bezanid")
print(tedad)
sum=0   
for a in order:
   #print(foods.index(a))
    print(a,"|gheymate vahed: ",gheymat[foods.index(a)],"|tedad: ",tedad[order.index(a)]
          ,"|majmoo: ",(gheymat[foods.index(a)]*tedad[order.index(a)]))
    sum= sum+(gheymat[foods.index(a)]*tedad[order.index(a)])
print("gheymate kol: ",sum)    


'''
kalampolo |gheymate vahed:  1000 |tedad:  2 |majmoo:  2000
chelomahi |gheymate vahed:  2000 |tedad:  5 |majmoo:  10000
chelokabab |gheymate vahed:  1200 |tedad:  3 |majmoo:  3600
gheymate kol:  15600

'''