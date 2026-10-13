'''

3- Yek tabe benvisid ke yek listi az karmandan ba etelaatesho migire


employees = {
    "E01": {
        "name": "Ali",
        "age": 28,
        "salary": 3000
    },

    "E02": {
        "name": "Sara",
        "age": 32,
        "salary": 4500
    },

    "E03": {
        "name": "Reza",
        "age": 25,
        "salary": 2800
    }
}


- balatarin hoghogh ro harki migire esmesho pas bedde
- kamtarin hogh ro harki migire esmesho pas bede
- yek listi az esme afradi k hoghoghe bish az 3000 migiran pas bede
- do vorodi begire tabe, yeki in dictionary (employees) yeki ye adad ke bedre liste esme afradi ke hoghoghe bishtar az oon adad ro migiran ro pas bede
- miangine kole hoghogh haro pas bede

'''


def analyze_employee_salaries(my_dict):
    info_list=list(my_dict.values())
    print(info_list[0]["salary"])
    highest_salary=info_list[0]["salary"]
    lowest_salary=info_list[0]["salary"]
    for i in info_list:
        if i["salary"]>=highest_salary:
            highest_salary=i["salary"]
            highest_paid_employee=i["name"]
            
    for i in info_list:
        if i["salary"]<=lowest_salary:
            lowest_salary=i["salary"]
            lowest_paid_employee=i["name"]
            
            
    above_3000=[]        
    for i in info_list:
        if i["salary"]>=3000:
            above_3000.append(i["name"])
            
            
            
    return highest_paid_employee,lowest_paid_employee,above_3000





def above_this_number(my_dict:dict,numb:float):
    info_list=list(my_dict.values())
    above_numb=[]        
    for i in info_list:
        if i["salary"]>=numb:
            above_numb.append(i["name"])
            
    return above_numb        
    
          
def average_salaries(my_dict):
    info_list=list(my_dict.values())
    total_sum=[]
    for i in info_list:
        total_sum.append(i["salary"])
    print(total_sum)
    return sum(total_sum)/len(total_sum)    
employees = {
    "E01": {
        "name": "Ali",
        "age": 28,
        "salary": 3000
    },

    "E02": {
        "name": "Sara",
        "age": 32,
        "salary": 4500
    },

    "E03": {
        "name": "Reza",
        "age": 25,
        "salary": 2800
    }
}


print(analyze_employee_salaries(employees))
print(above_this_number(employees,1000))
print(above_this_number(employees,2000))
print(above_this_number(employees,3000))
print(above_this_number(employees,4000))

print(average_salaries(employees))
