# boilerplate-django

My boilerplate for a quick django head start. Clone the repository, create a virtual environement and activate it. 

### Install the requirements

`pip install -r requirements.txt`

### Create a new .env file for decouple within the base directory (where manage.py exists) and fill your content

`touch .env`

```
SECRET_KEY=dlz1#d7478eb@@5y2mtjl2t0&j-b+o7-+o&ef=8!-3k0#8+x$@
DB_NAME=apoorv
DB_PASSWORD=test123
DB_HOST=somehost
DB_PORT=100
DEBUG=True
```

### Apply the migrations

`python manage.py migrate`

### Create a static directory

`mkdir static`

### Rename the project to your desired choice

`python manage.py rename <new-project-name>`

### Fire up the localhost server

`python manage.py runserver`

