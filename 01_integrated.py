#Do the import.
from jinja2 import Template

#Template declaration.
template = "Linux {{name}} is a {{type}} distribution with extensive {{kind}} software."

#Integated data. Compare this to 02_read_from_file.py adaptation inside templated folder.
data = {
    "name": "system",
    "type": "modular",
    "kind": "userland",
}

#Process and print.
j2_template = Template(template)
print(j2_template.render(data))

