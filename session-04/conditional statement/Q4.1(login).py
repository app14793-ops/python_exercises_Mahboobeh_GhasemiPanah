'''
Q1----- Login 

az User , usernamesh ro begirid va passwordesh ro ham begirid , agar
username barabar bashe ba admin va password bashe 1234 nenevesidi Login ba moafaghiat
anajm shod, agar na , benevisid password ya username ghalat hast.

'''


username=input("username ra vared konid: ")
password=input("password ra vared konid: ")

if username=="admin" and password=="1234":
    print("login ba movafaghiyat anjam shod")
else:
    print("username ya password eshtebah ast!")        



