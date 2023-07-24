student_height = []
total_no_of_students = int(input("Enter the total number of students   :"))
for i in range (0,total_no_of_students):
    height = int(input(f"student {i+1} height :"))
    student_height.append(height)
sum=0
for i in range(0,total_no_of_students):
    sum+=student_height[i]
average_height = sum/total_no_of_students
print(f"{round(average_height,2)} is the average height of the class")
