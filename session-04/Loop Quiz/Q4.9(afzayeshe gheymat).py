'''
Q9----Afzayeshe gheymat
yek listi darim az gheymate mahsol haye yek foroshgah , yek liste jadid besazid
ke tamame gheymate mahsoolat ro 10% afzayesh dahad.
'''

gheymat=[200,150,450,800,950]
afzayeshe_gheymat=[]
for a in gheymat:
    afzayeshe_gheymat.append(a+((a*10)//100))
print(afzayeshe_gheymat)    