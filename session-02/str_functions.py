
'''
Method	Description
capitalize()	+          Converts the first character to upper case
casefold()++		           Converts string into lower case
center()	 ++          	Returns a centered string
count()+		           Returns the number of times a specified value occurs in a string
encode()	++	           Returns an encoded version of the string
endswith()++	           	Returns true if the string ends with the specified value
expandtabs()++           	Sets the tab size of the string
find()+	           	Searches the string for a specified value and returns the position of where it was found
format()	++	           Formats specified values in a string
format_map()	++	           Formats specified values from a dictionary in a string
index()	++	           Searches the string for a specified value and returns the position of where it was found
isalnum()++		           Returns True if all characters in the string are alphanumeric
isalpha()	++           	Returns True if all characters in the string are in the alphabet
isascii()	  ++         	Returns True if all characters in the string are ascii characters
isdecimal()	    ++       	Returns True if all characters in the string are decimals
isdigit()		  ++         Returns True if all characters in the string are digits
isidentifier()	++           	Returns True if the string is an identifier
islower()	++	           Returns True if all characters in the string are lower case
isnumeric()	++	           Returns True if all characters in the string are numeric
isprintable()	++	           Returns True if all characters in the string are printable
isspace()	++	           Returns True if all characters in the string are whitespaces
istitle()	++	           Returns True if the string follows the rules of a title
isupper()	++	           Returns True if all characters in the string are upper case
join()++		           Converts the elements of an iterable into a string
ljust()	++	           Returns a left justified version of the string
lower()	+	           Converts a string into lower case
lstrip()	 +          	Returns a left trim version of the string
maketrans()	++	           Returns a translation table to be used in translations
partition()	++	           Returns a tuple where the string is parted into three parts
replace()+		           Returns a string where a specified value is replaced with a specified value
rfind()	++	           Searches the string for a specified value and returns the last position of where it was found
rindex()	++	           Searches the string for a specified value and returns the last position of where it was found
rjust()		++           Returns a right justified version of the string
rpartition()++		           Returns a tuple where the string is parted into three parts
rsplit()	++	           Splits the string at the specified separator, and returns a list
rstrip()+		           Returns a right trim version of the string
split()++		           Splits the string at the specified separator, and returns a list
splitlines()	++	           Splits the string at line breaks and returns a list
startswith()	++	           Returns true if the string starts with the specified value
strip()	+	           Returns a trimmed version of the string
swapcase()++		           Swaps cases, lower case becomes upper case and vice versa
title()	+	           Converts the first character of each word to upper case
translate()	 ++          	Returns a translated string
upper()+		           Converts a string into upper case
zfill()	++	           Fills the string with a specified number of 0 values at the beginning
'''

# casefold()       tozih: horuf bozorge dar reshte ra be horuf koochak tabdil mikonad

'''name="Mahboobeh"
new_name=name.casefold()
print(new_name)'''


#center()        tozih:2 ta vorudi migire,yek adad va yek character va ye reshte dorost mikone 
                # be tool on adad ke goftim be tori ke  string ma vasatesh bashe
                #va atrafesh charactor i ke goftim
                # va defult esh space hast
'''name="Mahboobeh"
new_name = name.center(20,"$")
print(type(new_name))  
print(new_name)	#$$$$$Mahboobeh$$$$$$  '''




#encode()       #tozih:2 ta voroodi migire,yeki model encode kardan ,
                 #ke default utf-8 hast
                 #yeki ham inke age natoonesti chizi ri incode koni che karesh koni,
                 #masalan be jash backslash bezari ya sarfe nazar koni ya tozih bedi ya ...
                 

'''name="Måhboobeh"
new_name=name.encode()
print(new_name)   #b'M\xc3\xa5hboobeh'



name="Måhboobeh"
new_name=name.encode(encoding="ascii",errors="namereplace")
print(new_name)   #b'M\\N{LATIN SMALL LETTER A WITH RING ABOVE}hboobeh'

'''


#endswith()       tozih: barasi mikonad ke aya reshte ba meghdare morede nazari 
                  #ke ma be onvane voroodi behesh dadim tama shode ya na 
                 # va True ya False barmigardanad

'''name="Mahboobeh"
new_name=name.endswith("h")
print(new_name) #True

name="Mahboobeh"
new_name=name.endswith("b")
print(new_name)  #False
'''


#startswith()	     tozih: barasi mikonad ke aya reshte ba meghdare morede nazari 
                  #ke ma be onvane voroodi behesh dadim shoroo shode ya na 
                 # va True ya False barmigardanad
'''
name="Mahboobeh"
new_name=name.startswith("M")
print(new_name) #True

name="Mahboobeh"
new_name=name.startswith("b")
print(new_name)  #False
'''

#expandtabs()       #tozih:tab haee ke dar reshte hast ra be 8 space tabdil mikonad 
                    #ama agar masalan 2 ra be onvane vorudi behesh bedim tab ra be 2 space 
                    #tabdil mikonad

'''
name="M\ta\th\tboobeh"
new_name=name.expandtabs(8)
print(new_name)     #M       a       h       boobeh


name="M\ta\th\tboobeh"
new_name=name.expandtabs(2)
print(new_name)    #M a h boobeh

'''


#format()        #tozih:dakhele reshte mitavanim {} begozarim va bad ba estefade az 
                 #tabe format har bar chizi ra ke mikhahim behesh ezafe konim
                 #agar dakhele {} chizi benevisim bayad haman ra be onvane voroodi be format bedahim 
                 #agar index begozarim digar niyazi be nevashtane index nist az avalin {}
                 #shoro be jay gozari mikonad 
                 #v agar hichi nanevisim baz ham be tartib az avalin {} jaygozari mikonad

'''
text="my name is {name}"
new_name=text.format(name="Mahboobeh")
print(new_name)    #my name is Mahboobeh

text="my name is {0},I am {1} years old"
new_name=text.format("Mahboobeh",36)
print(new_name)    #my name is Mahboobeh,I am 36 years old

text="my name is {},I am {} years old"
new_name=text.format("Mahboobeh",36)
print(new_name)    # my name is Mahboobeh,I am 36 years old

'''


#format_map()      #tozih: mesle format hast vali faghat dictionary ra be onvane voroodi migirad 
                    #va value har key ra jaygozari mikonad
                    #hatman dar reshte bayad maghadir key ha dar {} bashad                    

'''
my_dict = {"name":"Mahboobeh","age":36}
text="my name is {name},I am {age} years old"
print(text.format_map(my_dict))   #my name is Mahboobeh,I am 36 years old
'''


#index()           #tozih : index avalin character i ra ke peyda mikonad bar migardanad
                    #dar soorati ke character nabashad erroir midahad
                    #hamchenin mitavan behesh ebteda va enteha dad
'''
name="Mahboobeh Ghasemi Panah"
print(name.index("a"))   #1 
'''


#rindex()             #mesle index faghat az akhar index peyda mikonad
'''
name="Mahboobeh Ghasemi Panah"
print(name.rindex("a"))  #21
'''



#isalnum()         #tozih:dar soorati ke hameye charecter ha az a-z ya az 0-9 
                   #basahnd True barmigardanad
                   #dar soorati ke space ya @ ya $ ya ... bashad False barmigardanad

 	
'''name="Mahboobeh69"
print(name.isalnum())  #True	 

name="Mahboobeh69@"
print(name.isalnum())   #False 
'''   

  
#isalpha()	     #tozih: True dar soorati ke hamash alphabet bashad  a-z    

  	
#isascii()        #tozih:  True dar soorati ke hamash ascii bashad	a-z


#isdecimal()      #tozih: True dar soorati ke hamash desimal bashad	0-9 

  	
#isdigit()	     #tozih:   True dar soorati ke hamash digit bashad




#isidentifier()	 #tozih:   True dar soorati ke hamash identifier bashad 
                  #yani a-z ya 0-9 ya underscore bashad  
                  #dar soorati ke ba adad shro shavad ya space dashte bashad false barmigardanad
                  
'''name="Mahboobeh69"
print(name.isidentifier())     #True            
                  
name="69Mahboobeh"
print(name.isidentifier())     #False
'''




# lower()         #tozih: reshte ee barmigardanad ke hameye charecter ha horuf koochak bashad


'''
name="69Mahboobeh"
print(name.lower())   #69mahboobeh
'''
        
#isnumeric()	    ##tozih: True dar soorati ke hamash numeric bashad	0-9 	 

'''
text = "1.5"
print(text.isnumeric())     #False   be khater .
'''
 
   
#isprintable()		#tozih: True dar soorati ke hameye charecter ha ghabel chap
                    #shodan bashand masalan \n \t dar reshte bashad false barmigardanad
 
'''
name="69Mahboobeh"
print(name.isprintable())    #True

                
name="69\nMahboobeh"
print(name.isprintable())   #False 
'''               
                    
                    
#isspace()          #tozih: True dar soorati ke hameye charecter ha  space bashand

'''
name="69   Mahboobeh"
print(name.isspace())    #False


name=""
print(name.isspace())     #False


name="   "
print(name.isspace()) 	#True
'''	

           
#istitle()	             #tozih: True dar soorati ke har kalame da reshte 
                         #ba horoof bozorg shoroo shode bashad

'''text="In The Name Of God"	
print(text.istitle())     #True 
'''     


#isupper()                #tozih: reshte ee barmigardanad ke hameye charecter 
                         #ha horuf bozorg bashad
                         
'''
name="MAHBOOBEH"
print(name.isupper())      #True
'''


#join()	                 #in function tamame bakhsh haye yek iterable ra ba ham join mikonad
                          # dar ghalebe yek reshte
                         # va string ma be onvane joda konande estefade vmishavad
'''
text="test"	
t=("mahboobe","Ghasemi","36")           
print(text.join(t))    #mahboobetestGhasemitest36
'''


#ljust()	                  #az samte chap ,charecter i ke behesh dadim ezafe mikone be reshteye ma, 
                          # be tori ke tool reshte jadid barabare adadi bashad ke behesh dadim

'''
name="mahboobeh"
print(name.ljust(20,"@"))            mahboobeh@@@@@@@@@@@
'''

#rjust()                       #az samte  rast  ,charecter i ke behesh dadim ezafe mikone be reshteye ma, 
                          # be tori ke tool reshte jadid barabare adadi bashad ke behesh dadim
                          
'''
name="mahboobeh"
print(name.rjust(20,"@"))        #@@@@@@@@@@@mahboobeh      
'''            





#partition()                    #toZih: dar reshte be donbale meghdari ke behesh dadim migarde
                                #va yek tuple barmigardanad ke az 3 ghesmat tashkil shode
                                #ghabl az reshte 
                                #khode reshte
                                #va bad az an
'''
name="my name is mahboobeh"
print(name.partition("name"))   #('my ', 'name', ' is mahboobeh')
'''



#rfind()	               #tozih: az akhar index charecteri ra ke behesh dadim bar migardanad
                        #agar nabashad -1 
'''                       
                        
name="mahboobeh"
print(name.rfind("o"))   #5

'''


	






#rpartition()                    #mesle tabe partition() hast vali az akhar be donbale
                                #reshte migardad va tuple misazad
                                #avalin az akhar
'''
name="what is your name.my name is mahboobeh"
print(name.rpartition("name"))      #('what is your name.my ', 'name', ' is mahboobeh')
'''



#rsplit()	   #tozih:az akhar ba tavajoh be joda konande
                # va tedadi ke behesh dadim joda mikonad
                
'''
name="My name is Mahboobeh"
print(name.rsplit(" ",1))     #['My name is', 'Mahboobeh']

'''


#split()	               #yek reshte ra be list tabdil mikonad 
                       # ba joda konande e ke ma behesh midim 

'''
                       #va be tedad adadi ke behesh midim tabdil mikone
name="My name is Mahboobeh"
print(name.split())   #['My', 'name', 'is', 'Mahboobeh']


name="My name is Mahboobeh"
print(name.split(" ",1))   #['My', 'name is Mahboobeh']

'''
	           
#splitlines()          #tozih: reshte ra be list tabdil mikonad 
                        #joda konande sare khat ya haman \n hast
		          
'''	

name="My name is\n Mahboobeh"
print(name.splitlines())     #['My name is', ' Mahboobeh']


'''

#swapcase()              #tozih:horuf bozorge reshte ra kuchak va horuf kuchak ra bozorg mikonad

'''
name="MaHbOoBeH"
print(name.swapcase())    #mAhBoObEh

'''


#translate()           #tozih:ba estefade az yek dictionary ke bayad be surat ascii code bashad 
                        #ya ba estefade az yek jadvali ke ba estefade az tabe maketrans() dorost shode bashe
                        #charecter haye string ra avaz mikonad

#maketrans()		        
'''
name="Mahboobeh"
olgoo=name.maketrans("h","k")       
print(name.translate(olgoo) )       #Makboobek

'''


#zfill()	             #be avale reshte sefr ezafe mikone ta vaghti ke tulesh berese be adadi ke ma goftim
                     #age toole khodesh bishtar bashe hich kari nemikone
                     
                     
'''                     
name="Mahboobeh"
print(name.zfill(20))       #00000000000Mahboobeh  
print(name.zfill(5))        #Mahboobeh  
''' 

