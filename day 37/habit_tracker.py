import requests
from datetime import datetime

today = datetime.today()
formatted_date_today = today.strftime("%Y%m%d")
print(formatted_date_today)

USER_NAME = "="
TOKEN = "="
pixela_endpoint = "https://pixe.la/v1/users"

pixela_parameters = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=pixela_parameters)
# response.raise_for_status()
# print(response.text)
pixela_graph_parameters = {
    "id": "graph1",
    "name": "number of pages read",
    "unit": "pages",
    "type": "int",
    "color": "shibafu",
}
pixela_headers = {
    "X-USER-TOKEN": TOKEN
}
# pixela_graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
# response = requests.post(url=pixela_graph_endpoint, json=pixela_graph_parameters, headers=pixela_headers)
# print(response.text)
add_pixel_data_parameter = {
    "date": formatted_date_today,
    "quantity": "5"
}
pixela_post_new_pixel_data = f"{pixela_endpoint}/{USER_NAME}/graphs/graph1"
response = requests.post(url=pixela_post_new_pixel_data, json=add_pixel_data_parameter, headers=pixela_headers)
print(response.text)
