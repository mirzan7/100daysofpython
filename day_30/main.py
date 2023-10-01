# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["sfdgg"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something    !!!!!")
# except KeyError as error_message:
#     print("the key is not in the dictionary!!!!!!")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
# height = float(input("height:   "))
# weight = int(input("weight:    "))
# if height>

fruits = ["apple", "pear", "orange"]
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("fruit error")
    else:
        print(fruit+" pie")

make_pie(4)