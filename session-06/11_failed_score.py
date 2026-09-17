def failed_score(scores):
    for i in scores:
        if i<10:
            j=scores.index(i)
            scores.pop(j)
    
    return scores        


scores=[18, 7, 13, 9, 20, 5]
students=["ali","maryam","reza","sara","zahra"]
print(failed_score(scores))



def failed_score2(scores):
    failed_student=[]
    for i in scores:
        if i<10:
            j=scores.index(i)
            scores.pop(j)
            failed_student.append(students[j])
    
    return scores ,failed_student




print(failed_score2(scores))





def failed_score3(scores):
    
    for i in scores:
        if i<10:
            j=scores.index(i)
            scores.pop(j)
    
    return len(scores)




print(failed_score3(scores))