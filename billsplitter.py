amount = int ( input ("Total amount :"))
discount = int ( input( "discount :"))
split = int ( input("split among :"))
total_amont = float( amount - (amount * (discount/100) ))/ split
print ( amount * (discount/100) )
print (f"The amount to br payed by each is : {round (total_amont,2)}")
