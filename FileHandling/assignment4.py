import csv


with open("students.csv","w",newline="") as f:
    write = csv.writer(f)
    write.writerow(["Name","Subject","Marks"])

    write.writerow(["Arun","Python",76])
    write.writerow(["Arjun","Sql",65])
    write.writerow(["Bhuvan","Cloud",75])
    write.writerow(["Shivu","OS",55])
print("CSv file created Sucessfully")