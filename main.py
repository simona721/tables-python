from tabulate import tabulate


lists = [["Mark", 18], ["Steven", 23], ["Jeff", 45], ["Mary", 56], ["Jane", 21]]

print(tabulate(lists))

print(tabulate(lists, headers=["Name", "Age"], showindex="always", tablefmt="simple_grid"))

table = {"Sport Teams": ["Chelsea", "Aston Villa", "Freiburg", "Nantes", "Juventus", "AC Milano", "Porto", "Braga"],
         "Countries": ["England", "England", "Germany", "France", "Italy", "Italy", "Portugal", "Portugal"]}


print(tabulate(table, headers="keys", tablefmt="simple_outline", showindex="always"))