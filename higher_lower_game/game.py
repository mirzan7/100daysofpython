import random
from data import data

def get_random_choice():
    return random.choice(data)

def formal_data(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"name {name}, a {description}, from {country}"

def compare_follower(choice,other_option):
    if(choice['follower_count'] > other_option['follower_count']):
        return 0
    else:
        return 1

print("lets play higher or lower game  !!!")
choice_result = False
compareB = get_random_choice()
score =0
while(choice_result is not True):
    compareA=compareB
    compareB = get_random_choice()
    if(compareA == compareB):
        compareB = get_random_choice()
    print(f"compare A {formal_data(compareA)}")
    print("vs")
    print(f"compare B {formal_data(compareB)}")
    choice = input("which is higher ?  ")
    result = 0
    if choice.lower() == 'a':
        result = compare_follower(compareA,compareB)
    else:
        result = compare_follower(compareB,compareA)
    if (result==1 ):
        print(f"you loose, your final score is {score}")
        choice_result = True
    else:
        score+=1
        print(f"you won !!!your score is {score}")
    