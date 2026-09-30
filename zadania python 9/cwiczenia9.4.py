import csv
from datetime import datetime

now = datetime.now()

with open("raport.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(["ID", "user", "status","data"])
    writer.writerow([1,"Jan","open", now])
    writer.writerow([2,"Anna", "open", now])
    writer.writerow([3,"Adam", "closed", now])