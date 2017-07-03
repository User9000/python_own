from smtplib import SMTP


host = "smtp.gmail.com"
port = 587
username = ""
password = ""
from_email = username
to_list = [""]


##Create connection
email_conn2 = SMTP(host,port)
email_conn2.ehlo()
#Start Encryption
email_conn2.starttls()
#Authentication try
email_conn2.login(username,password)
email_conn2.sendmail(from_email, to_list, "hello there this is an email message")
#Close connection
email_conn2.quit()