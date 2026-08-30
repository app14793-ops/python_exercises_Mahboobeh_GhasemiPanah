'''
Q12---- Gereftane mahsool

ba estefade az halgheye for , yek systemi benevisid , ke 5 bar az karbar esme yek
mahsool begire (masalan zara, nike ,..) va agar toole oon mahsool kamtar az 6 bashad
dakhele yek listi bename sabade_kharid berizad.

'''
sabade_kharid=[]
for i in range(5):
    print("baraye",i+1,"omin bar...")
    mahsool=input(" esme mahsool ra vared kon: ")
    if len(mahsool)<6:
        sabade_kharid.append(mahsool)
print("sabade kharid:",sabade_kharid)



        
        