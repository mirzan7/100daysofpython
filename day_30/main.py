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

# fruits = ["apple", "pear", "orange"]
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("fruit error")
#     else:
#         print(fruit+" pie")
#
# make_pie(4)

facebook_post = [
    {'likes': 21, 'comments': 2}, {'likes': 13, 'comments': 2, 'shares': 1}, {'likes': 33, 'comments': 8, 'shares': 3},
    {'comments': 4, 'shares': 2}, {'comments': 1, 'shares': 1}, {'likes': 19, 'comments': 3}
]
total_likes = 0
for post in facebook_post:
    try:
        total_likes = total_likes+post['likes']
    except KeyError:
        pass

print(total_likes)