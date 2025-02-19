import tabulate

list1 = {{"Alex",10}, {"Bob", 12}, {"Clarkes",13}, {"Dawar",44, "Mumbai"}, {"Martin", 15}}

print(tabulate.tabulate(list1, headers={"Name", "Age"}))

