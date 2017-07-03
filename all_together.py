

## All together string substitution by keyword.
###substitituion by argument

import datetime
default_names = ["Justin","john","steve","mario","louis","ryan","scott"]
default_amounts = [120.23,100.45,99.23,90.9,100.12,99.67,98.89]
unf_message =  """ Hi {name}

Thank you for your purchase on {date}.
We hope you are excited about  using it. Just as a reminder
the purchase total was ${total}
Have a great one!

Team NONAME  
"""


############# Factory message #######
def factory_message(names, amounts):
    messages = []
    if len(names) == len(amounts):
        i = 0
        today = datetime.datetime.now()
        date = '{today.month}/{today.day}/{today.year}'.format(today=today)
        for name in names:
            new_name = name.title()
            new_amount = "%.2f"%(amounts[i])
            new_msg = unf_message.format(name = new_name, date = date, total= amounts[i])
            i += 1
            print(new_msg)


factory_message(default_names,default_amounts)

#####################################









