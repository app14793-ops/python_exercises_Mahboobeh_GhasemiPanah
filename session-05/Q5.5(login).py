'''
5 - Login system --> az user , username va password begire, username = admin va password = 1234 hast , 
ta zamani ke user dorost username o password ro vared nakrde hey bege 'username ya password ghaalt mibashad'
 agar doros vared krd benevise : ba moafaghiat vared shodid
'''


u="admin"
p="1234"
while True:
    username=input("username khod ra vared konid: ")
    password=input("password khod ra vared konid: ")
    if username==u and password==p:
        print("--------\nlogin ba movafaghiyat anjam shod\n--------")
        break
    print("--------\nusername ya password ghalat mibashad\ndobare vared konid\n--------")  