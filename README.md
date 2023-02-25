Install pip dependecies : 

```
django
uvicorn
fastapi
pymysql
tailwind
django_browser_reload
"python-jose[cryptography]"
passlib
```

launch server with :

```
cd projet_fil_rouge_api
uvicorn mainApi:app --reload
```

Swagger docs on :

http://localhost:{your_port}/docs

launch tests with :

```
pytest
```



