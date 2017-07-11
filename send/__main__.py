
#running arguments on terminal, how to pass arguments to terminal?

import argparse
import os
from data_manager import read_data

#where this file exist, find data.csv
#file_item_path = os.path.join(os.getcwd(),"data.csv")

#look in the folder where the package lives and get data.csv
file_item_path = os.path.join(os.path.dirname(__file__),"data.csv")


parse = argparse.ArgumentParser(prog="send")
parse.add_argument("type", type=str, choices = ['view','message'])
parse.add_argument('-id','--user_id',type=int)
parse.add_argument('-e','--email',type=str)

#parse by id
args = parse.parse_args()
#print(read_data(user_id = args.user_id))

#parse by email
print(read_data(email= args.email))

if args.type == "view":
    print(read_data(user_id= args.user_id))
    print(read_data(email = args.email))

elif args.type == 'message':
    print("send message")

