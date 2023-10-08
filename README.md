# python_api_project
this is a course to learn basics of Python API Project

# steps to follow for setup
- install pyton
- install vsc
- open your project folder in vsc
- install a virtual environment using cli with code: <py -3 -m venv <venv-name>>
- choose python.exe in venv folder als deault interpreter: view->command palette->search 
   python interpreter and type in path
- activate venv in terminal: <venv\Scripts\activate.bat>
- install fastapi : <pip install fastapi>
- go to fastapi.tiangolo.com/tutorial/first-steps/ for first use 
- install uvicorn(if not installed) : <pip install uvicorn>
- install postman to manage your http request froom fastapi
- install pydantic if not installed to validate request 
  data(check in LIB if installed) <pip install pydantic>
- <from typing import optional> to add optional attributes to your post request Body
- import also status, Response and HTTPException from fastAPI to manage http responses

- to access documentation for fastapi(swagger) just add docs after the homepage path

- if you add a new folder to contain your main.py file for example you have to add the __init__.py file in the folder for it to be considered as a package

- if the new folder name is app:
use command <uvicorn app.main:app> to access the fastAPI

 ----------------MYSQL------------------

- install mysql dbms package: <pip install mysql-connector-python>
- connect to Mysql server
-one way is to manually create queries using normal sql commands.

- you can also use an ORM (Object Relational Mapper)
- the most known is SQLALCHEMY
- The ORM helps use classes as Models for our database
- to install sqlalchemy: <pip install sqlalchemy>
