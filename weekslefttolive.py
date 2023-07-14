age = int (input ("enter your age"))
year = 90 - age
month = (90 * 12) - (age * 12)
week = ( ( 90 * 365 ) / 7 ) - ( ( age * 365 ) / 7 )
day = 90 * 365 - age * 365
print(f"In years  = {year} left \n In months = {month} left \n In weeks = {round(week)} left \n In days = {day} left ")