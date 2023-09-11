import pandas

data = pandas.read_csv("weather_report.csv")
# temperature = data["temp"].to_list()
# print(data[data.temp == data.temp.max()] )
# monday = data[data.day == "monday"]
# monday_temperature = int(monday.temp)
# monday_temp_f = monday_temperature * 9/5 + 32
# print(monday_temp_f)

# create dataframe from scratch
data_dic = {
    "students":["amy","james","angela"],
    "scores":[76,56,65]
}
new_data = pandas.DataFrame(data_dic)
new_data.to_csv("mark_list.csv")
