import csv

with open('vacancy.csv','r') as file:
    data = csv.reader(file)
    companies = {row0:row1:for row in data}

companyname = input("Ввведите компанию")

if companyname in companies:
    print(f"Salary")
    print(f"Work_Type")
    print(f"Company_size")
    print(f"Role")
    print(f"Company")
