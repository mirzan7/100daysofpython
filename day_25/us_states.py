import pandas
from turtle import Turtle, Screen

number_of_state_found = 0
guessed_state = []
missing_state = []
t = Turtle()
t.penup()
t.hideturtle()
screen = Screen()
screen.bgpic("blank_states_img.gif")
data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
while number_of_state_found < 50:
    n = number_of_state_found+1
    user_input = screen.textinput(f"{n}/50 states left","Enter the name of the state :").title()
    if user_input == "Exit":
        for state in all_states:
            if state not in guessed_state:
                missing_state.append(state)

        break
    if user_input in all_states:
        guessed_state.append(user_input)
        state_data = data[data["state"].isin([user_input])]
        new_x = int(state_data["x"])
        new_y = int(state_data["y"])
        t.goto(new_x, new_y)
        t.write(user_input)
        number_of_state_found += 1

df = pandas.DataFrame(missing_state)
df.to_csv("missing_state.csv")
