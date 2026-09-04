'''
2 - yek listi az nomre haye daneshjoha va esmashon dairm, dar enteha faghat esme daneshjohaei ke pass shodan ro neshon bede (optional : onaro rank bandi ham kone)
    
students = ['ali','vahid','sara','hamid','reza','elham','mohsen','zahra','paniz','parmida']
scores = [20,17,9 , 13, 7 , 20 , 18 , 3 , 1 , 14]


'''


students = ['ali','vahid','sara','hamid','reza','elham','mohsen','zahra','paniz','parmida']
scores = [20,17,9 , 13, 7 , 20 , 18 , 3 , 1 , 14]

passed=[]
r=[]
for name,s in zip(students,scores):
    if s>=10:
        passed.append(name)
        r.append(s)
print("--------befor ranking--------")        
print(passed)
print(r)
o=0
o1=0
for i in range(len(r)):
    a=r[i]
    for j in range(len(r)):
        if a>r[j]:
            o=r[i]
            r[i]=r[j]
            r[j]=o
            o1=passed[i]
            passed[i]=passed[j]
            passed[j]=o1
print("--------after ranking--------")                   
print(passed)            
print(r)