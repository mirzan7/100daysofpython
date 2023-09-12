import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census.csv")
# temperature = data["temp"].to_list()
# print(data[data.temp == data.temp.max()] )
# monday = data[data.day == "monday"]
# monday_temperature = int(monday.temp)
# monday_temp_f = monday_temperature * 9/5 + 32
# print(monday_temp_f)

# create dataframe from scratch
# data_dic = {
#  "students":["amy","james","angela"],
#  "scores":[76,56,65]
# }
# new_data = pandas.DataFrame(data_dic)
# new_data.to_csv("mark_list.csv")
gray_squirel_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirel_count = len(data[data["Primary Fur Color"] == "Black"])
red_squirel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(gray_squirel_count)
print(black_squirel_count)
print(red_squirel_count)
data_dic ={
    "Fur color": ["gray","black","red"],
    "count": [gray_squirel_count,black_squirel_count,red_squirel_count]
}
df = pandas.DataFrame(data_dic)
df.to_csv("color_count.csv")
