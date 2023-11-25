import requests
from datetime import date
from pprint import pprint


class ListOperation:

    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/ee4d2cb035b19a9b20407f70f110a318/taskmanager/sheet1"
        self.data = ""

    def add_new_task(self):
        title = input("Insert task title  : ")
        description = input(f"Description about {title}  : ")
        priority = input("Give priority (high/medium/low)  : ")
        date_string = input("Due date : ")
        due_date = date.fromisoformat(date_string)
        data_collection = {
            "sheet1": {
                "title": title,
                "description": description,
                "priority": priority,
                "due_data": due_date,
                "status": "not completed"
            }
        }
        response = requests.post(url=self.sheety_endpoint, json=data_collection)
        print(response.text)

    def get_task_details(self):
        response = requests.get(url=self.sheety_endpoint)
        self.data = response.json()["sheet1"]
        for task in self.data:
            print(f"Title: {task['title']}      Description: {task['description']}      Priority: {task['priority']}        due_date: {task['due_date']}        status: {task['status']}")

    def task_completed(self, title):
        updated_task_data = {
            "sheet1": {
                "task": "completed"
            }
        }

        for row in self.data:
            if row['title'] == title:
                response = requests.put(url=f"{self.sheety_endpoint}/{row['id']}", json=updated_task_data)
                print(response.text)
        self.get_task_details()

    def delete_task(self, title):
        for row in self.data:
            if row['title'] == title:
                response = requests.delete(url=f"{self.sheety_endpoint}/{row['id']}")
                print(response.text)
        self.get_task_details()

    def search_for_task(self, keyword, search_item):
        for row in self.data:
            if search_item == row[keyword]:
                print(f"Title: {row['title']}      Description: {row['description']}      Priority: {row['priority']}        due date: {row['due_date']}        status: {row['task']}")
