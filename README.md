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

create an env.py file in the [projet_fil_rouge_api](https://github.com/tcosattini/projet_tp_7_api/tree/main/projet_fil_rouge_api) (next to settings.py)
then add into env.py the variable bellow and set it to your mysql config

```python
MYSQL_CONFIG = {
  'ENGINE': 'django.db.backends.mysql',
  'NAME': 'fromagerie_com',
  'USER': 'root',
  'PASSWORD': '',
  'HOST': 'localhost',
  'PORT': '3306',
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
