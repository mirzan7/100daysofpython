# new_list = [n*2 for n in range(1,5)]
# print(new_list)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_list = [n*n for n in numbers]
# print(squared_list)
# result = [number for number in numbers if number%2 == 0]
# print(result)

# with open("file1.txt")as file1:
#    file1data = file1.readline()
# with open("file2.txt")as file2:
#     file2data = file2.readline()
# result = [number for number in file1data if number in file2data]

# print(result)
# import random
# names = ['alex', 'beth', 'caroline', 'dave', 'eleanor', 'freddie']
# student_scores = {item: random.randint(1, 100) for item in names}
# print(student_scores)
# passed_students = {student: score for (student, score) in student_scores.items() if score>60}
# print(passed_students)

# sentance = "what is the airspeed velocity of an unladen swallow"
# word_list = sentance.split()
# result = {word: len(word) for word in word_list}
# print(result,end="\n")

# weather_c = {
#    "monday": 12,
 #  "wednesday": 15,
  #  "thursday": 14,
   # "friday": 21,
    # "saturday": 22,
    # "sunday": 24
# }
# weather_f = {day: temp*(9/5)+32 for (day, temp) in weather_c.items()}
#  weather_f = {item: temp*(9/5))+32 for (item, temp) in weather_c.items()}
# print(weather_f)

import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
letter_code = {row.letter: row.code for(index, row) in data.iterrows()}
print(letter_code)
name = input("Enter your name :").upper()
code_name = [(letter,letter_code[letter]) for letter in name]
print(code_name)