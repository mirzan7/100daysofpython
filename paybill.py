import random as rmd
names = []
numb = int(input("Enter the number of customers :"))
for i in range(numb):
    name = input(f"name {i+1}")
    names.append(name)
random_number = rmd.randint(0,numb)
print(f"{names[random_number]} has to pay the bill")