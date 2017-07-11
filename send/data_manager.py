
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
