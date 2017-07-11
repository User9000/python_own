import csv
import tempfile
import shutil
                             
file_name = "data.csv"                        
                                   
temp_file = tempfile.NamedTemporaryFile(delete=False)                 
print(temp_file)        
                                                   
with open(file_name, 'rb+') as csv_file, temp_file:
    reader = csv.DictReader(csv_file)             
    fields = ['id','name','email','amount','sent']       
    writer = csv.DictWriter(temp_file, fieldnames=fields)
    for row in reader:
        print(row)                         
        writer.writerow({'id': row['id'],})
    shutil.move(temp_file.name,file_name)
         
print(temp_file.name)