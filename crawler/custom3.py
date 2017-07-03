
from smtplib import SMTP, SMTPAuthenticationError, SMTPException


host = "smtp.gmail.com"
port = 587
username = ""
password = ""
from_email = username
to_list = [""]

password_wrong = SMTP(host,port)
password_wrong.ehlo()
#Start Encryption
password_wrong.starttls()

#Authentication try/except block 
try:
    password_wrong.login(username,"wrong password!")
    password_wrong.sendmail(from_email, to_list, "hello there this is an email message")
except SMTPAuthenticationError:
    print("Could not login")
except:
    print("an error occured")


#Close connection
password_wrong.quit()



