# Jinja2-templating-with-Python3


This repository releates to: https://github.com/postman721/flask-restful-jinja2

The purpose here is to clarify Jinja2 capabilites clearly without Flask or Ansible.


### Requirements: Python3 and Jinja2

<b>For Jinja2 on Debian:</b>

		sudo apt-get install python-jinja2 python3-jinja2


<b>Content:</b>

		01_integrated.py == Example with integrated json data.
		
		templated folder == 02_read_from_file.py program that reads variables from two variable files: 
		
		readme.py and readme2.py

02_read_from_file.py also appends readme2.py to a file called data.txt.

<b>Usage:</b>

		python3 01_integrated.py	
		
OR

		python3 02_integrated.py
		
		
Customize readme python files to change/alter template variables.		

![template](https://user-images.githubusercontent.com/29865797/111887140-b4420200-89db-11eb-82df-f2240f828a1f.png)

Based on declared variables, the above (or similar) will get generated.
