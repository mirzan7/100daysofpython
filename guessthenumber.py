import random
def number_of_guess_assign(choice):
    if(choice.lower() == 'hard'):
        return 5
    elif(choice.lower() == 'easy'):
        return 10
    else:
        print("Invalid input  !!!")
        
print("Hello weelcome guess te nuumber game")
choice = input("do you wand it 'hard'(5 guess) or 'easy'(10 guess)   :")
number_of_guess = number_of_guess_assign(choice)
print(number_of_guess)
random_number = random.randint(0,100)
game_is_on = True
while(number_of_guess > 0):
    guess = int(input(f"Guess the number from 0 - 100 number of guess left {number_of_guess}    :"))
    if(guess == random_number):
        print("You have guessed it correctly !!!")
        break
    elif(guess > random_number):
        print("Too high")
    else:
        print("Too Low")
    number_of_guess -=1
    
    
