def calculate_age1(year:int)->int:
    '''
    mohasebe sen bar asase sale tavalod
    sale tavalod ra ba type int be onvane voroodi migirad va 
    sen ra ba type int be onvane khoroojo barmigardanad
    '''
    return 2026-year
   
    


#print("your age is: ",calculate_age1(1991))


    


def calculate_age2(year,date_type):
    if date_type=="shamsi":
        return 1405-year
        
    elif date_type=="miladi":
        return 2026-year


#print(calculate_age2(1369,"shamsi"))
#print(calculate_age2(1991,"miladi"))


def calculate_age3(year,date_type="miladi"):
    if date_type=="shamsi":
        return 1405-year
        
    elif date_type=="miladi":
        return 2026-year


#print(calculate_age3(1369,"shamsi"))
#print(calculate_age3(1991))



def calculate_age4(year):
    if year<=1405:
        return 1405-year
    else:
        return 2026-year

#print(calculate_age4(1369))
#print(calculate_age4(1406))











