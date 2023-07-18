height = int(input("Enter your height in cm :"))
age = int(input("Enter your age"))
if height >= 120 :
    if(age>=18):
        print("Your are eligible to ride, and rate = $12")
    else:
        print("your are eligible to ride, and the rate = $7")
else:
    print("Your are not eligibible to ride ")