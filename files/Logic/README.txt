Notes for installing and running python and Django

Download and install python 3.5.1
https://www.python.org/downloads/

Download and install pip.py
http://pip.readthedocs.org/en/stable/installing/
--in cmd......
--navigate to where get-pip.py is installed, then
--python get-pip.py
---or simply double click on the file. That should work as well.

Install a virtual environment to run django in
--pip install virtualenv
---pip freeze will show installed items

Opening up new virtual environment
--virtualenv <environment name>
--.\Scripts\activate
   ##this will run the virtual environment
--.\Scripts\deactivate
   ##this will close the virtual environment

Install Django
--pip install django (installs latest version)

Start Django project
--.\Scripts\django-admin.py startproject <name of project>
--<name of project> manage.py ##runs the project

Install pymysql to enable mysql database access for python
--pip install pymysql

Run Django environment
--python manage.py runserver


