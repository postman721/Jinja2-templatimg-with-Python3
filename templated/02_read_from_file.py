#Do the imports.
from jinja2 import Template
from readme import *
from readme2 import *

#####################
#First file.
#####################

#Template declaration.
template = "Linux {{name}} is a {{type}} distribution with extensive {{kind}} software."

#Process and print -> Notice that data points to resource inside readme.py.
j2_template = Template(template)
print(j2_template.render(data))

print("")

#####################
#Second file.
#####################

#Template declaration.
template2 = "Coding with {{language}} is a {{mood}} way to {{action}}."

#Process and print.
j2_template = Template(template2)
print(j2_template.render(data2))

###########################
#Write to  data.txt file
###########################
x=j2_template.render(data2)

#Write data2 to file
with open('data.txt', 'a') as file:
    file.write(x)


print("")

print ("And I am just a standard print calling from the end of 02_read_from_file.py and verifying success.")
print ("Appended to data.txt.")
