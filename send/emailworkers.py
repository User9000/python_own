################################################
###
###             Email classs to send email from a gmail account
###                                         
################################################

from smtplib import SMTP, SMTPAuthenticationError, SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#####connection to send email
host = "smtp.gmail.com"
port = 587
username = "email"
password = "passwor"
from_email = username
to_list = ["emails to send"]



import datetime

class MessageUser():
    user_details = []
    messages = []
    email_messages = []
    base_message = """ Hi {name}

Thank you for your purchase on {date}.
We hope you are excited about  using it. Just as a reminder
the purchase total was ${total}
Have a great one!

Team NONAME  
"""

    def add_user(self,name,amount, email=None):
        detail = {
            "name" :name,
            "amount": amount,
        }
        today = datetime.datetime.now()
        date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        detail['date'] = date_text
        if email is not None:
            detail['email'] = email

        self.user_details.append(detail)

    def get_details(self):
        return self.user_details

    def make_messages(self):
        if len(self.user_details) > 0:
            for detail in self.get_details():
              name = detail["name"]
              amount = detail["amount"]
              date = detail["date"]

              message = self.base_message
              new_msg = message.format(
                    name = name,
                    date = date,
                    total = amount,

              )
              user_email = detail.get("email")
             
              if user_email:
                    user_data = {
                        "email": user_email,
                        "message": new_msg
                    }
                    self.email_messages.append(user_data)
              else:
                    self.messages.append(new_msg)
                
              #self.messages.append(new_msg)
            return self.messages
        return []

    def send_email(self):
        self.make_messages()
        if len(self.email_messages) > 0:
            for detail in self.email_messages:
                user_email = detail['email']
                user_message = detail['message']
                #SEND EMAIL
                try:
                    email_conn = SMTP(host,port)
                    email_conn.ehlo()
                    #Start Encryption
                    email_conn.starttls()
                    ###login information
                    email_conn.login(username,password)
                
                    ####Add information to email#######
                    the_msg = MIMEMultipart("alternative")
                    the_msg['Subject'] = "Billing update!"
                    the_msg["From"] = from_email
                    the_msg["To"] = user_email
                    
                    part_1 = MIMEText(user_message,'plain')
                    
                    the_msg.attach(part_1)
                    #the_msg.attach(part_2)
                    email_conn.sendmail(from_email, [user_email], the_msg.as_string())
                    email_conn.quit()
                    
                except SMTPException:
                    print("Error sending message")
                    




            return True
        return False

obj = MessageUser()
obj.add_user("Justin", 123.32, email ='cla.pythontester@gmail.com')
obj.add_user("John", 94.23, email ='cla.pythontester@gmail.com')
obj.add_user("Sean", 93.23, email ='cla.pythontester@gmail.com')
obj.add_user("Emilee", 193.23, email ='cla.pythontester@gmail.com')
obj.add_user("Marie", 13.23, email ='cla.pythontester@gmail.com')
obj.get_details()
