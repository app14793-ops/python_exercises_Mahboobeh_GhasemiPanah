def calculate_grade(grade):
    if grade>=90:
        return "A"
    elif grade>=80:
        return "B"
    elif grade>=70:
        return "C"
    elif grade>=60:
        return "D"
    else:
        return "F"


while True:
    grade=int(input("enter your grade: "))
    if grade in range(101):
        print(calculate_grade(grade))
        break
    else:
        print("grade must be between 0 and 100")