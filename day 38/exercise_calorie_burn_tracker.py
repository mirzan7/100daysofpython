import requests
from datetime import datetime
import csv

website_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/0=/myWorkouts/workouts"
APP_ID = "="
API_KEY = "="
GENDER = "male"
WEIGHT_KG = "93"
HEIGHT = "192"
AGE = "21"

exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
exercise_text = input("What exercise did you do today: ")

exercise_parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=website_endpoint, json=exercise_parameters, headers=exercise_headers)
response.raise_for_status()
result = response.json()
print(result)

# exercise = result['exercises'][0]['name']
# print(exercise)

today = datetime.today().strftime("%d/%m/%y")
now_time = datetime.now().strftime("%X")

for exercise in result['exercises']:
    Date = today
    Time = now_time
    Exercise = exercise['name']
    Duration = exercise['duration_min']
    Calories = exercise['nf_calories']
    data = [today, Time, Exercise, Duration, Calories]
    print(data)
    with open("MyWorkouts.csv", 'a')as workout_file:
        csv_writer = csv.writer(workout_file)
        csv_writer.writerow(data)

with open("MyWorkouts.csv", 'r')as workout_read:
    for row in workout_read:
        print(row)
    # sheet_response = requests.post(url=sheet_endpoint, json=sheet_input)
    # print(sheet_response.text)

