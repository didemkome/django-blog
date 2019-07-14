# Blog App with Django

Blog application with Django that allows users to create, edit, and delete posts.

## Installation
- [Python](https://www.python.org/downloads/)

- [Pip](https://pip.pypa.io/en/stable/)

After Python Installation we need to install virtualenv, this is not a dependency of Django, but it is advised to create separate virtual environments for different projects. By using virtual environments, applications can run in their own ‘sandbox’ in isolation of other Python applications.

- Install virtual environment: ``` $ python -m virtualenv env ```

- Activate virtual environment:  

On Windows:
``` $ source env\Scripts\activate ```  

On macOS and Linux:
``` $ source env/bin/activate ```  

- Install dependencies: ```$ pip install -r requirements.txt ```  

- Django ``` $ pip install Django ```

## How to run?
Run migrations: ``` $ python manage.py migrate ```  
Run development server: ``` $ python manage.py runserver ```  

## License
This project is licensed under the MIT [MIT](https://choosealicense.com/licenses/mit/) License
