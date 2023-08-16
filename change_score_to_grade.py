import os
os.system('cls')
student_mark = {}
number_of_students = int(input("Enter the total number of students  :  "))
for i in  range (0,number_of_students):
    name = input(f"Enter the name of student {i+1}  : ")
    mark = int(input(f"Enter the mark of {name}"))
    student_mark[name] = mark

for student in student_mark:
    if(student_mark[student]>90):
        student_mark[student] = "O"
    elif(student_mark[student]>80):
        student_mark[student]= "A"
    elif(student_mark[student]>70):
        student_mark[student]="B"
    elif(student_mark[student]>60):
        student_mark[student]="C"
    elif(student_mark[student]>50):
        student_mark[student]="D"
    else:
        student_mark[student]="F"
        
print(student_mark)
    