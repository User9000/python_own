
import csv
import datetime
import shutil
#from tempfile import NamedTemporaryFile
import tempfile

file_name = "data.csv"
#otherfile = "data.csv"
temp_file = tempfile.NamedTemporaryFile(delete=False)
print(temp_file)

with open(file_name) as csv_file, temp_file:
        reader = csv.DictReader(csv_file)
        fieldnames = ['id', 'name', 'email', 'amount', 'sent']
        writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
        #writer.writeheader()
        print(temp_file.name)
        for row in reader:
           print(row)
           writer.writerow({
            "id":row["id"],
            "name":row['name'],
            "email":row['email'],
            "amount":"2323",
            "sent": "",
           })
        
shutil.move(temp_file.name, file_name)
    
#temp_file.close()

