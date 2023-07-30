import random
random_list = ["apple","orange","watermelon","lemon"]
word = []
life = 5
count = 0
chosen_word = random.choice(random_list)
print(chosen_word)
for letter in chosen_word:
    word += "_"
while count <= len(chosen_word):
    guess = input("Guess the letter   :")
    for i in range(len(chosen_word)):
        if (chosen_word[i]==guess):
            word[i] = guess
            count+=1
    print(word)
    
            
    
    