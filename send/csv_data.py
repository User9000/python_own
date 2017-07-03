

"""
with open('data.csv',"w+") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["COL1","COL2"])
    writer.writerow(["Data 1", "Data 2"])


with open('data.csv', "a") as csvfile:   
    writer = csv.writer(csvfile)
    writer.writerow(["Data 3", "Data4"])

with open('data.csv', "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

#### Working with csv files as they were json files.
with open('data.csv', "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

with open('data.csv', "w") as csvfile:   
    fieldnames = ["id","title"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"id":123, "title":"New title"})

with open('data.csv', "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)


def get_length(file_path):
    return 1
"""

import csv 
import shutil
from tempfile import NamedTemporaryFile


def get_length(file_path):
    with open("data.csv") as file:
        reader = csv.reader(file)
        reader_list = list(reader)
        #print(reader_list)
        return (len(reader_list))


def append_data(file_path,name, email):
    fieldnames = ['id', 'name','email']
    #length/the number of the rows
    next_id = get_length(file_path)
    with open(file_path, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #writer.writeheader()
        writer.writerow({
            "id": next_id,
            "name": name,
            "email": email,
        })
    
append_data("data.csv", "Justin", "test1@gmail.com")

filename = "data.csv"
temp_file = NamedTemporaryFile(delete=False)

with open(filename,"rb") as csvfile, temp_file:
    reader = csv.DictReader(csvfile)
    filename = ['id','name','email','amount', 'sent']
    writer = csv
