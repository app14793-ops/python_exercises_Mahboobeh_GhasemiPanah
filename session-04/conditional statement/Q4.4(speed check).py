'''
Q4----Speed check

az karbar yek sorate mashin begirid

agar bish az 120 bashe benevsiid khatarnak , agar beyne 80 ta 120 bashe 
beneisid sorate ziad, agar beyne 80 ta 0 bashe benevsidi sorate noraml
agar zire 0 bashe benevsidi mashin dar halate istade hast.

'''
sorat=int(input("sorate mashin ra vared konid: "))
if sorat>=120:
    print("khatarnak")
elif sorat>=80:
    print("sorate ziyad")
elif sorat>0:
    print("sorate normal")
else:
    print("mashin dar halate istade ast")    
    