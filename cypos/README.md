CyPOS-CS309
-----------
Annie Steenson
George Zachariades
Jens Petersen
Rockie Brooks

Directories
-----------
Base app: Contains all base files
CyPos: Project folder, contains settings.py and routing and templates
Public: old html/css/js files from NodeJS project

LearnPythonSyntax.py
--------------------
Is a python file to learn the syntax.. 
self explanatory in the name

Run Server Command:
-------------------
python manage.py runserver
localhost:8000

Run Python Script in Django Shell:
----------------------------------
python manage.py runscript <script>(without .py)

Dependencies
------------
Install: 

    pip install requirements.txt
    
List all: 

    pip list
    

Migrate/Update Database Commands:
---------------------------------
Generates migration files: 

    python manage.py makemigrations
    
Runs all migration files that have not been ran: 

    python manage.py migrate 
    
See all migrations: 

    python manage.py showmigrations
    
    
Administrative Account:
-----------------------
python manage.py createsuperuser

    username: grp17
    email: lilannie@iastate.edu
    password: cs309
Access Admin Interface:

    localhost:8000/admin
    
Querying Data with Django ORM:
------------------------------
Open Python Shell:

    python manage.py shell
Import Model:

    from base.models import Users
List all:

    Users.objects.all()
Get all records in an array:

    users = Users.objects.all()
    user = users[0]
Access attributes of a model:

    user.firstname
    user.lastname
    user.email
Get on record from a table where: (Can throw various exceptions)

    Users.objects.get(id=1)
Get all records from a table where: (returns an array of objects)

    Users.objects.filter(name="annie")
    Users.objects.filter(name="annie")[0].id
Get all records from a table where not: (returns an array of objects)

    Users.objects.exclude(name="annie")
    Users.objects.exclude(name="annie")[0].id
    
Template Syntax 
--------------- 
{{ variable }}
{% tag %}
{{ variable|filter }}