'''
Q3---- check mouse
ma yek list darim az mahsoolat , va injori hast : 
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]

yek vorodi az karbar begirid va az karbar bekahhdi esme yek mahsol ro bege
agar oon mahsol dakhele in list bashe begid mahsool dar dastress hast , 
agar nabood benevisid dar dastress nist.
'''

products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
product_name=(input("esme mahsool ra vared konid :")).title().strip()

if product_name in products:
    print("mahsool dar dastress hast")
else:
    print("mahsool dar dastress nist")
        