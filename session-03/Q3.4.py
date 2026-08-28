'''
q3.4. nomreye daneshjo ro begri eye adadi beyne 0 ta 20

ag 18 - 20 --> A
16 0 18 --> B

14-16 --C
10-14 --> d

<10 --> f (faill)
'''

a=float(input("nomre ra vared kon: "))
if (0<=a<=20):
        if 18<=a<=20:
            print("A")
        elif 16<=a:
            print("B") 
        elif 14<=a:
            print("C")
        elif 10<=a:
            print("D")
        else:
            print("fail")
    
else:
        print("nomre bayad beyne 0 ta 20 bashad!")
