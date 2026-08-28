'''Method  Description
append()       Adds an element at the end of the list
clear()         Removes all the elements from the list
copy()      Returns a copy of the list
count()          Returns the number of elements with the specified value
extend()       Add the elements of a list (or any iterable), to the end of the current list
index()        Returns the index of the first element with the specified value
insert()       Adds an element at the specified position
pop()     Removes the element at the specified position
remove()       Removes the first item with the specified value
reverse()    Reverses the order of the list
sort()      Sorts the list
'''



#append()       #tozih:vorudi ra be tahe list ezafe mikonad


'''
l1=["Mahboobeh","Ghasemi",36,+98910000,22800000,"shiraz"]       
print(l1.append(1369))      #None       #emal mikonad khoruji nemidahad
print(l1)                   #['Mahboobeh', 'Ghasemi', 36, 98910000, 22800000, 'shiraz', 1369]
'''




#clear()         tozih:tamame element haye list ra pak mikonad list ra  khali mikonad


'''
l1=["Mahboobeh","Ghasemi",36,+98910000,22800000,"shiraz"] 
l1.clear()
print(l1)                #[]
'''



#copy()              #tozih:yek copy az list barmigardanad


'''
l1=["Mahboobeh","Ghasemi",36,+98910000,22800000,"shiraz"] 
l1_copy=l1.copy()
l1.append("software engineering")  #['Mahboobeh', 'Ghasemi', 36, 98910000, 22800000, 'shiraz', 'software engineering']
print(l1)
print(l1_copy)    #['Mahboobeh', 'Ghasemi', 36, 98910000, 22800000, 'shiraz']
'''

#count()            #tozih:yek adad barmigardanad ke tedad element haee ba value dade shode ast


'''
name=["ali","reza","mohammad","ali"]
print(name.count("ali"))        #2
'''



#extend()                 #tozih:ajzaye iterable e ke be onvane vorudi behesh dadim 
                         #done done be tahe list ezafe mikone

'''
name=["ali","reza","mohammad","ali"]
name.extend(["sara","zahra","maryam"])
print(name)                     #['ali', 'reza', 'mohammad', 'ali', 'sara', 'zahra', 'maryam']

'''


#index()                  tozih:index avalin vorudi ke behesh midim ra barmigardanad


'''
name=['ali', 'reza', 'mohammad', 'ali', 'sara', 'zahra', 'maryam']
print(name.index("ali"))     #0
name.pop(0)
print(name.index("ali"))    # 2
'''

#insert()                     #tozih:yek adad be onvane index migirad va yek element
                             #bad element ra dar jaye khaste shode gharar midahad
                             
'''                             
                             
f=["sib","moiz","gilas","anbe"]    
f.insert(1, 45) 
print(f)                        #['sib', 45, 'moiz', 'gilas', 'anbe']
                             
'''                             


#pop()                      #vorudi ra az list hazf mikonad va an ra barmigardanad


'''

l=["Mahboobeh","Ghasemi",36,+98910000,22800000,"shiraz"]
print(l.pop(3))              #98910000
print(l)                    #['Mahboobeh', 'Ghasemi', 36, 22800000, 'shiraz']  
'''




#remove()                   #avalin element ba meghdari ke ma behesh dadim ra hazf mikonad


'''
name=["ali","reza","mohammad","ali"]
name.remove("ali")
print(name)                  #['reza', 'mohammad', 'ali']

'''


      
#reverse()                    #tozih: tartibe chidemane list rs baraks mikonad


'''
f=["sib","moiz","gilas","anbe"] 
f.reverse()
print(f)                      #['anbe', 'gilas', 'moiz', 'sib']

'''




  
#sort()                          #tozih:list ra ba asase tartibe horufe alefba moratab mikonad
                                #hamchenin adad ra moratab mikonad 
                                #agar horuf bozorg dahtim aval horuf bozorg ra ghara midahad
                                
'''                                

name=['Ali', 'reza', 'Mohammad',16, 'ali',6, 'sara', 'zahra', 'maryam',]
name.sort()
print(name)                       #TypeError: '<' not supported between instances of 'int' and 'str'
 
name=['Ali', 'reza', 'Mohammad', 'ali', 'sara', 'zahra', 'maryam',]
name.sort()
print(name)                      #['Ali', 'Mohammad', 'ali', 'maryam', 'reza', 'sara', 'zahra']


num=[12,56,2,39]
num.sort()
print(num)                       #[2, 12, 39, 56]


'''
                           
