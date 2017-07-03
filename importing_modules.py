
##Importing modules
#from email_class import MessageUser, some_random, make_messages

from py_day_mod.make_messages import MessageUser

obj = MessageUser()
obj.add_user("Justin", 123.32, email ='cla.pythontester@gmail.com')
obj.add_user("John", 94.23, email ='cla.pythontester@gmail.com')
obj.add_user("Sean", 93.23, email ='cla.pythontester@gmail.com')
obj.add_user("Emilee", 193.23, email ='cla.pythontester@gmail.com')
obj.add_user("Marie", 13.23, email ='cla.pythontester@gmail.com')
obj.get_details()


print(obj.get_details())






