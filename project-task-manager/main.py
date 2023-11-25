from list_operation import ListOperation
from pprint import pprint

list_operation = ListOperation()
#list_operation.add_new_task()
list_operation.get_task_details()
#list_operation.task_completed("gate preperation")
#list_operation.delete_task("gate preperation")
keyword = input("Column name : ")
search_item = input("Item to be searched : ")
list_operation.search_for_task(keyword, search_item)
