# Grasmas
Application for running Grasmas gift giving

The goal is to allow users to add their gifts into a database using a website, 
and then to have another web application read the database and display
a Jepoardy-like board for choosing and trading gifts during Grasmas.

## Prerequisites

### Install dependencies
```
pip install -r requirements.txt
```

### Run database migrations
```
python manage.py migrate
```

## Run the program
```
cd grasmas_root 
python manage.py runserver
```
and then go to
`localhost:8000/populate`
followed by `localhost:8000/start`


