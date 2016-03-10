CyPOS
CS 309
Annie Steenson
George Zachariades
Jens Petersen
Rockie Brooks

Run Server Command:
-------------------
python manage.py runserver
localhost:8000

Migrate/Update Database Commands:
---------------------------------
Generates migration files:
    python manage.py makemigrations
Runs all migration files that have not been ran:
    python manage.py migrate 
See all migrations:
    python manage.py migrate --list
    
Administrative Account:
-----------------------
python manage.py createsuperuser
    username: grp17
    email: lilannie@iastate.edu
    password: cs309
Access Admin Interface:
    localhost:8000/admin
