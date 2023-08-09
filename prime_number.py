def prime_number(number):
    count = 0
    for i in range (1,number):
        if(number % i == 0):
            count+=1
    if(count<=2):
        print(f"The number {number} is a prime number ")
    else:
        print("the number is not a prime number ")

number = int(input("Enter the number you want to check whether it is prime or not  :"))
prime_number(number)