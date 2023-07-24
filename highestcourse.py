student_marks = []
total_no_of_students = int(input("Enter the total number of students   :"))
for i in range (0,total_no_of_students):
    mark = int(input(f"student {i+1} height :"))
    student_marks.append(mark)
max = 0
for i in range(0,total_no_of_students):
    if(student_marks[i]>max):
        max = student_marks[i]
print(f"The highest score is {max} ")