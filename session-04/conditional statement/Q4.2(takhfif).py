'''
Q2----- Takhfif
az user gheymate kala ro begirid , age gheymate kala bishtar az 1 milion toman bashad
20% takhfif, agar gheymate kala beyne 500,000 ta 1 million toman bashe , 15 darsad takhfif 
agar gheymate kala zire 500 hezar toman bashad, 10% takhfif emal konid va dar nahayat
gheymate bad az takhfif ro b user neshan dahid
'''


gheymat=int(input("gheymate kala ra vared konid: "))
if gheymat>=1000000:
    print("gheymate bad az takhfif=",(gheymat*80)//100)
elif gheymat>=500000:
    print("gheymate bad az takhfif=",(gheymat*85)//100)    
elif gheymat>0:
    print("gheymate bad az takhfif=",(gheymat*90)//100) 
    
    