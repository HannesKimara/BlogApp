[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/HannesKimara/Pitcher/blob/master/LICENSE) 

# Blog App
Post Blogs to the BlogApp, read blogs and review relevant blogs

## Getting Started
To clone this repository run in a virtual environment
```bash
$ git clone https://github.com/HannesKimara/BlogApp.git
$ cd BlogApp
$ pip install -r requirements.txt
```
To setup or change MAIL SMTP settings edit the config.py file. The following configs would need changes
```bash
12.    MAIL_SERVER = '<SMTP_CLIENT_SERVER>'
13.    MAIL_PORT = SMTP_CLIENT_PORT

      # Include only one
14.    MAIL_USE_TLS = True or False
14.    MAIL_USE_SSL = True or False
```
Export or set environment variables
On windows powershell run:

```bash
$env:MAIL_USERNAME="<YOUR_SMTP_MAIL_USERNAME>"
$env:MAIL_PASSWORD="<YOUR_MAIL_PASSWORD>"
```

On unix based OS run:
```bash
$ export MAIL_USERNAME="<YOUR_SMTP_MAIL_USERNAME>"
$ export MAIL_PASSWORD="<YOUR_MAIL_PASSWORD>"
```

To start the server run

```bash
$ python manage.py serve
```

## Testing
- To conduct unittest change app factory config to test in manage.py
- Create a testing database and change the SQLALCHEMY_DATABASE_URI in your config 
- RUN `$ python manage.py test`

## Author
This project was created by Hannes Kimara

## Built With
 - Python 3.6
 - Flask 1.1.1
 - Materialize 1.0.0

## License
This is licensed under MIT License Copyright(2020) Hannes Kimara
