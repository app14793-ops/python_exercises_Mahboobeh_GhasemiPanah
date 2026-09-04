'''
4 - ATM --> yek system ATM sakhte beshe,
 be karbar bege 'Menu : mojoodi, variz, bardasht , khoroj , amaaliate digar' ,
 ta zamani ke karbar mojodi  , variz , bardasht ro entekhab kone baraye harkodom kheyli sade benevise
 'amaliate variz entekhab shod , ya  amaliate felan entekhab shod' bad beporse 'amaliate digar, khoroj' ,
 agar amaliate diagr ro entekhab kard mojadad menu ro neshon bede 'mojoodi , variz,bardasht' , 
 ama agar rooye khoroj zad bege mamnon khoroj ba moafaghiat anajm shod
'''

while True:
    print("Menu : \nmojoodi\nvariz\nbardasht\nkhoroj\namaaliate digar:")
    amaliate=input("amaliate khod ra vared konid: ")
    if amaliate.lower().strip()=="mojoodi":
        print("amaliate mojoodi entekhab shod")
    elif amaliate.lower().strip()=="variz":
        print("amaliate variz entekhab shod")
    elif amaliate.lower().strip()=="bardasht":
        print("amaliate bardasht entekhab shod")
    elif amaliate.lower().strip()=="khorj":  
        break
    
    a=input("amaliate digar ya khorooj: ")
    if a.lower().strip()=="khorooj":
        break