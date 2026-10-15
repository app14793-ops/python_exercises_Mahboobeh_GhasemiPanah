'''

Optional 1 : Tabe ei besazid bename even_numbers ke vorodi yek adad bename n daryaft kone
va ba estefade iz dastoore yield , adade zoj ro az 2 ta n yeki yeki tolid kone

sepas yek geenrator besazido dakhele yek moteghayer gahrar dahid va ba next()
 3 meghdare aval ro namayesh dahid
 
'''



def numbers(n):
    for i in range(2,n+1,2):
        yield i
        
my_generator=iter(numbers(12))



print(next(my_generator))   

print(next(my_generator))   

print(next(my_generator))  