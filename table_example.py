from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["pokemon", "type"]
table.align = "l"
table.add_row(["pikachu", "electric"])
table.add_row(["squirtle", "water"])
table.add_row(["charmander", "fire"])


print(table)
