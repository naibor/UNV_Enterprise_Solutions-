##### Enterprise Solutions Section

create venv
`python3 -m venv venv`
##### activate venv
`source/venv/bin/activate`
##### install requirements
`pip3 install -r requirements.txt`
#### create database:
'NAME': 'enterprise',
'USER': 'enterprise',
'PASSWORD': 'password',

#### load dumped data
location:
data/enterprise.sql
#### 
#### run migrations
`python manage.py makemigrations`
'python manage.py migrate`
`python manage.py runserver`
####
navigate to 
http://127.0.0.1:8000/projects/

#### API
