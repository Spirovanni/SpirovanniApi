# SpirovanniApi

0. Push an existing repository from the command line

    `git remote add origin https://github.com/Spirovanni/SpirovanniApi.git`

    `git branch -M main`

    `git push -u origin main`

1. Generate virtualenv

    `python -m venv venv`

2. Activate venv

    `source venv/bin/activate`

3. Install required Python packages using pip and requirements.txt  

    `pip install -r requirements.txt`
    
4. Install Django and start database if starting from scratch

    `pip install Django`
    
    `pip install Djangorestframework`
    
    `pip install django-cors-headers`
    
    `django-admin startproject spirovanni .`
    
    `django-admin startapp api`
    
    `python manage.py migrate`
    
4. Create database

    `python manage.py makemigrations`
    `python manage.py migrate`

5. Load initial data to database using Django fixtures

    `python manage.py loaddata fixtures/initial_data.json`

6. Run App

      `python manage.py runserver`
      
7. Creating an admin user
First we’ll need to create a user who can login to the admin site. Run the following command:

    `$ python3 manage.py createsuperuser`

    Enter your desired username and press enter.

    Username: admin
    You will then be prompted for your desired email address:

    Email address: admin@example.com
    The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.

    Password: **********
    Password (again): *********
    Superuser created successfully.
