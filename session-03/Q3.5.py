'''
q3.5. az karbar esme product ro begire berize to zarf

gheymatesho begire berize too zarf

code takhfif begire

age code takhfif barabar bood ba z14

20% az gheymat kam kone nmaayesh bede
bege gheymate nahaei ine 


q3.5.2. --> ag code takhfif eshtebah zad --> bege 
ghalat zadid

q3.5.3 --> ag ghalat zad, bege yekbar dg mitoni emtehan kone
ag doros zad anjam bde (takhfif) ag na --> bege block shodid

'''


product_name=input("esme mahsool ra vared konid: ")
price=int(input("ghetmate mahsool ra vared konid: "))
code_takhfif=input("code takhfif ra vared konid: ")

if code_takhfif.lower().strip()=="z14":
   
    print("code takhfifi emal shod,gheymate nahaee",product_name ,"=", (price*80)/100)
else:
    print("code takhfif eshtebah ast!")
    print("yek bareb digar emtehan konid: ")
    code_takhfif=input("code takhfif ra vared konid: ")
    if code_takhfif.lower().strip()=="z14":
       
        print("code takhfifi dorost ast,gheymate nahaee ",product_name ,"= ", (price*80)/100)
        
    else:
        print("block shodid!!!")
        
        
        
        
        
        
        
        
        
        
