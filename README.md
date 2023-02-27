# API projet FROMAGERIE.com

## required

- django
- uvicorn
- fastapi
- pymysql
- tailwind
- django_browser_reload
- "python-jose[cryptography]"
- passlib

## Install pip dependecies

```bash
pip install -r requirements.txt
```

## customize you database settings

add an env.py file in the projet_fil_rouge_api (next to settings.py)
then add the variable bellow and set it to your mysql config

```python
MYSQL_CONFIG = {
    'ENGINE': 'django.db.backends.mysql',
     'NAME': 'database',
     'USER': 'user',
     'PASSWORD': 'password',
     'HOST': 'localhost',
     'PORT': '0000',
 }
```

## launch server with

```bash
cd projet_fil_rouge_api
uvicorn mainApi:app --reload
```

Swagger docs on :

<http://localhost:{your_port}/docs>

launch tests with :

```bash
pytest
```
