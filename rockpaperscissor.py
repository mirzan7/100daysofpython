import random
choice = int(input("What do you choose ? \n 0 for rock\n 1 for paper\n 2 for kathrika \n\n\t\t\t"))
number_to_string = {0:"rock", 1:"paper", 2:"scissor"}
computer_choice = random.randint(0,2)
if(choice == 0 and computer_choice == 1):
    print(f"computer chose  {number_to_string[1]}  Lost ......\;;/")
elif(choice == 1 and computer_choice == 2):
    print(f"computer chose  {number_to_string[2]}Lost ......\;;/")
elif(choice == 2 and computer_choice == 0):
    print(f"computer chose  {number_to_string[0]}Lost ......\;;/")
else:
    print("Won...........\''/")