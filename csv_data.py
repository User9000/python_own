

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
import codecs
from tempfile import NamedTemporaryFile
import datetime

def read_data(user_id=None, email=None):
    filename = "data.csv"
    items = []
    with open(filename , 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        unknown_user_id = None
        unknown_user_email = None
        for row in reader:
            if user_id is not None:
                if int(user_id) == int(row.get("id")):
                    return row
                else:
                    unknown_user_id = user_id
            if email is not None:
                if str(email) == str(row.get("email")):
                    return row
                else:
                    unknown_user_email = email
        if unknown_user_id is not None:
                return "User id {user_id} not found".format(user_id=user_id)
        if unknown_user_email is not None:
                return "Email {email} not found".format(email=email)
    return None

    
def get_length(file_path):
    with open(file_path) as file:
        reader = csv.reader(file)
        reader_list = list(reader)
        return (len(reader_list))


def append_data(file_path,name, email,amount):
    fieldnames = ['id', 'name','email',"amount","sent","date"]
    #length/the number of the rows
    next_id = get_length(file_path)
    with open(file_path, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if next_id == 0:
           writer.writeheader()
        writer.writerow({
            "id": next_id,
            "name": name,
            "email": email,
            "amount":amount,
            "sent":"",
            "date": datetime.datetime.now(),
        })
    
#append_data("data.csv", "Justin", "test1@gmail.com",12344)
def edit_data(edit_id=None,email=None, amount=None,sent=None):
    #create a temporary file.
    filename = "data.csv"
    # create temp file
    temp_file = NamedTemporaryFile(delete=False)
    with codecs.open('data.csv','rb') as csvfile,temp_file:
        reader = csv.DictReader(csvfile)
        field_names = ["id","name","email","amount","sent","date"]
        writer = csv.DictWriter(temp_file,fieldnames=field_names)
        writer.writeheader()
        for row in reader:
            if edit_id:
                if int(row['id']) == edit_id:
                    row['amount'] = amount
                    row['sent'] = sent
            elif email is not None and edit_id is None:
                if str(row['email']) == str(email):
                    row['amount'] = amount
                    row['sent'] = sent
            
            else:
                pass

            writer.writerow(row)

        shutil.move(temp_file.name , filename)
        return True
    return False  


#edit_data(email="test1@gmail.com", amount=99.99, sent='')
