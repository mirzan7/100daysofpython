import random

def draw_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        print("You went over 21. You lost")
    elif computer_score == 0:
        print("You lost. Computer has blackjack")
    elif user_score == 0:
        print("You won with a blackjack.")
    elif user_score == computer_score:
        print("Draw")
    elif user_score > 21:
        print("You lost")
    elif computer_score > 21:
        print("you won")
    elif user_score > computer_score:
        print("You won.")
    else:
        print("Computer won")

def play_game():
    user_cards = []
    computer_cards = []
    for number in range(2):
        user_cards.append(draw_card())
        computer_cards.append(draw_card())
  
    game_end = False
    while not game_end:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
    
    print(f"   Your cards: {user_cards}, your score: {user_score}.")
    print(f"   Computer's first card: {computer_cards[0]}")
    
    get_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if get_card == "y".lower():
        user_cards.append(draw_card())
  
    else:
        game_end = True
        while computer_score < 17:
            computer_cards.append(draw_card)
  
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


play = input("Do you want to play a game of  blackjack. Type y or n: ").lower()
while play == "y":
    play_game()