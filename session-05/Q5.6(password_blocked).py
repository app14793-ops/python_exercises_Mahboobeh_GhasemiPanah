'''
6 - hamin login system ro hbenevisind be sharti ke agar bish az 3 bar ehstebah vared kard , 
begid account ghofl shode va dige nazarid username ya password bezane va ende program
'''

u="admin"
p="1234"
for i in range(3):
    username=input("username khod ra vared konid: ")
    password=input("password khod ra vared konid: ")
    if username==u and password==p:
        print("login ba movafaghiyat anjam shod")
        break
    elif i==2:
        print("account ghofl shode!")
        break
    print("username ya password eshtebah ast!")
    print("baraye bar ",i+2,"om vared konid...")    