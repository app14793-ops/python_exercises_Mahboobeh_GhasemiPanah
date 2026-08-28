'''Method  Description
clear() Removes all the elements from the dictionary
copy()  Returns a copy of the dictionary
fromkeys()  Returns a dictionary with the specified keys and value
get()   Returns the value of the specified key
items() Returns a list containing a tuple for each key value pair
keys()  Returns a list containing the dictionary's keys
pop()   Removes the element with the specified key
popitem()   Removes the last inserted key-value pair
setdefault()    Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()    Updates the dictionary with the specified key-value pairs
values()    Returns a list of all the values in the dictionary
'''




#clear()              #tamame element haye dictionary ra pak mikonad


'''
my_dict={"name":"Mahboobeh","family_name":"Ghasemi","age":36,}
my_dict.clear()
print(my_dict)               #{}
'''



#copy()                  #tozih:yek copy az dictionary barmigardanad

'''

my_dict={"name":"Mahboobeh","family_name":"Ghasemi","age":36,}
copy_dict=my_dict.copy()
print(copy_dict)               #{'name': 'Mahboobeh', 'family_name': 'Ghasemi', 'age': 36}

'''



#fromkeys()              #yek ditionary barmigardanad ba haman key va value ke behesh dadim
                         #done done element haye key ra barabare meghdare value gharar midahad

'''
x=("name","age")
y=(0)

print(dict.fromkeys(x,y))    # {'name': 0, 'age': 0, 'city': 0}



x=("name","age")
y=("Mahboobeh",36)
print(dict.fromkeys(x,y))      #print(dict.fromkeys(x,y))
'''




#get()                         #tozih:behesh key midim value barmigardanad


'''
my_dict={'name': 'Mahboobeh', 'family_name': 'Ghasemi', 'age': 36}
print(my_dict.get("name"))          #Mahboobeh

'''



#items()                       #yek view object az key value haye dict barmigardanad
                              #ke key value ha be surat tuple dar yek list gharar darand
                              #har taghiri dar dict etefagh bioftad dar dict.items()
                          #ham emal mishavad
'''

my_dict={'name': 'Mahboobeh', 'family_name': 'Ghasemi', 'age': 36} 
print(my_dict.items())         #dict_items([('name', 'Mahboobeh'), ('family_name', 'Ghasemi'), ('age', 36)])

   
'''





#keys()                         #tamame key haye dict ra dar ghalebe yek list barmigardanad


'''

my_dict={'name': 'Mahboobeh', 'family_name': 'Ghasemi', 'age': 36}
print(my_dict.keys())             #dict_keys(['name', 'family_name', 'age'])

'''

#pop()                        #tozih: key e ra behesh midim az dict hazf mikonad


'''
my_dict={'name': 'Mahboobeh', 'family_name': 'Ghasemi', 'age': 36}
my_dict.pop("age")
print(my_dict)                   #{'name': 'Mahboobeh', 'family_name': 'Ghasemi'}

'''
  
#popitem()                        #akharin chizi ke be dict ezafe shode ra hazf va barmigardanad


'''

my_dict={'name': 'Mahboobeh', 'family_name': 'Ghasemi', 'age': 36}
my_dict["city"]="shiraz"
print(my_dict)

print(my_dict.popitem())                 #('city', 'shiraz')

'''





   
#setdefault()                             #value e key e ra ke behesh dadim barmigardanad
                                          #dar soorati ke key dar dict vojud nadasht 
'''                                          #key va value ra be dict ezafe mikonad


my_dict={'name': 'Mahboobeh', 'family_name': 'Ghasemi'}
print(my_dict.setdefault("name"))           #Mahboobeh


my_dict={'name': 'Mahboobeh', 'family_name': 'Ghasemi'}
print(my_dict.setdefault("name","sara"))        #Mahboobeh



my_dict={'family_name': 'Ghasemi'}
print(my_dict.setdefault("name","sara"))  #sara

print(my_dict)       # {'family_name': 'Ghasemi', 'name': 'sara'}



'''




#update()                               #tozih: ba key va value e ke behesh midim dict ra
                                       # update mikonad
                                       
'''                                       
                                     
my_dict={'name': 'Mahboobeh', 'family_name': 'Ghasemi'}
my_dict.update({"city": "shiraz"})
print(my_dict)                            #{'name': 'Mahboobeh', 'family_name': 'Ghasemi', 'city': 'shiraz'}

'''







    
#values()                            #tozih:value ha ra be surate yek list barmigardanad


'''
my_dict={'name': 'Mahboobeh', 'family_name': 'Ghasemi', 'age': 36}
print(my_dict.values())                 #dict_values(['Mahboobeh', 'Ghasemi', 36])
 
'''


























