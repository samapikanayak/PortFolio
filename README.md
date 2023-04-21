# Study for Electricity Board

The project is a web application built using the Django web framework. The application allows users to view all the users to create and update their own portfolio. But superadmin can see all portfolios.

# Installation
1. create a folder for the project
2. create a virtualenv and activate it to install all the requiirements and dependancies to run the project
commands:- python3 -m venv venv (to install)
to activate the venv:- 
source venv/bin/activate (for linux or mac)
venv\Scripts\activate (for windows)
to deactivate the virtualenv command:- deactivate
3. Install the required packages using pip install -r requirements.txt.
4. Run the migrations using python manage.py migrate.
5. Create a superuser using python manage.py createsuperuser. one existing superuser is admin userId:-admin and password:- admin
6. Run the server using python manage.py runserver.
7. to test the apis command:- python manage.py test portfolioapp.tests

# Usage
To use the only backend application, follow these steps:
    Navigate to the project's URL in your postman or thunder client.
    Login and get token. Use access token to authorise
    Create, edit, or delete any items as desired.
# postman collection
    I have attached here my postman collection file as well as in the mail
