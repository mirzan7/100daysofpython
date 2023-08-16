def addition(number1,number2):
    return number1+number2
def substraction(number1,number2):
    return number1-number2
def multiplication(number1,number2):
    return number1*number2
def division(number1,number2):
    return number1/number2

decision = True
while(decision == True):
    number1 = int(input("Enter the number 1 : "))
    number2 = int(input("Enter the number 2 : "))
    option = input("+ : addition\n- : substraction\n* : multiplication\n/ : division\n------------>  ")
    if(option == '+'):
        print(addition(number1,number2))
    elif(option == '-'):
        print(substraction(number1,number2))
    elif(option == '*'):
        print(multiplication(number1,number2))
    elif(option == '/'):
        print(division(number1,number2))
    else:
        print('Invalid Option')
    decision = input("Enter 'yes' to continue with another calculation or 'no' to stop  : " )
    if(decision == "yes"):
        decision = True
    else:
        decision = False