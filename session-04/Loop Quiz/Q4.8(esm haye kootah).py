'''
Q8---- Esm haye kootah

Yek listi az user ha darim, berid va tedade afradi ke dar in list 

andazeye esmeshon kamtar az 5 hast ro beshmorid.


users=['ali','vahid','mohammadreza','hamidreza','gholamreza','amir','sara','maryam']
'''

users=['ali','vahid','mohammadreza','hamidreza','gholamreza','amir','sara','maryam']
count=0
for a in users:
    if len(a)<5:
        count=count+1
print(count,"ta esm ba andazeye kam tar az 5 vojood dare")
    