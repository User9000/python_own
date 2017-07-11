

import os

### Get the path of the file in the OS regardless of OS flavor... OS, MAC, Linux
def get_template_path(path):
    file_path = os.path.join(os.getcwd(),path)
    if not os.path.isfile(file_path):
        raise Exception("This is not a valid template path")
    return file_path

#### get the file, and read it
def get_template(path):
    file_path = get_template_path(path)
    return open(file_path).read()

####Format the message
def render_context(template_string, context):
    return template_string.format(**context)

#file_="email_messages.txt"
file_html= "email_message.html"

template = get_template(file_html)
context = {
    "name":'Carlo',
    "date": None,
    "total":None

}

print(render_context(template,context))

