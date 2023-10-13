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
- install fastapi : <pip install fastapi[all]>
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
- search in fastapi documentation for SQL relational Databases and follow the steps 
- instsall email validator if not already installded to validate emails: <pip install pydantic[email]>
- install passlib to handle password hashes(password encryption) <pip install passlib[bcrypt]>
- install python-jose[cryptography] to manage JWT encryption mechanisymn <pip install python-jose[cryptography]>
- install python multipart to handle OAuths Forms <pip install python-multipart>, no need to import
- to load env-variables, create a .env file and paste all the variables in
- install pydantic-settings(if not installed): <pip install pydantic-settings>
- import BaseSettings from pydantic_settings and extend it
- install python-dotenv if not installed and load it after Settings class <pip install python-dotenv>
- a composite key is a primary key that spans multiple columns, this helps have two columns that always has different values

- install Alembic t Migrate/Modify Databases. this tool will help manage databases alteration so that we dont need to delete tables before updating those <pip install alembic>
-initialise a new script directory for alembic: <alembic init <filename(alembic)>>
- use <alembic revison autogenerate "msg"> to add a revision automatically from the models created or updated with the sqlalchemy model creation class"

- importing CORS Dependency to manage domain restrictions <from fastapi.middleware.cors import CORSMiddleware>
- complete documentation for CORS in Fastapi



****************These are query methods to communicate with mysql manually without ORM************************
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'admin',
    'database': 'python_api',
    'port': '3308'
}
try:
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary= True)
except mysql.connector.Error as err:
    print(f"Error: {err}")


def get_posts():
    get_query = "SELECT * FROM  posts"
    cursor.execute(get_query)
    return cursor.fetchall()

def get_post_by_id(id: int):
    get_query = f"SELECT * FROM  posts WHERE id = {id}"
    cursor.execute(get_query)
    return cursor.fetchall()

def create_new_post(post:Post):
    post_query = "INSERT INTO posts (title, content, published) VALUES (%s,%s,%s)"
    values = (post.title, post.content, post.published)
    cursor.execute(post_query, values)
    return cursor.rowcount > 0

def delete_post(id: int):
    delete_query = "DELETE FROM posts WHERE id = %s"
    values = (id,)
    cursor.execute(delete_query, values)
    return cursor.rowcount > 0

def update_post(id: int, post: Post):
    update_query = "UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s"
    values = (post.title, post.content, post.published, id)
    cursor.execute(update_query, values)
    return cursor.rowcount > 0

****************end***********************************




************************JOINS***************************************
1. INNER JOIN
The INNER JOIN keyword selects records that have matching values in both tables.
<sql>
SELECT columns
FROM table1
INNER JOIN table2
ON table1.column_name = table2.column_name;

<to count the number of entries from the filter based on a col_name>
SELECT columns, COUNT(col_name)
FROM table1
INNER JOIN table2
ON table1.column_name = table2.column_name;


2. LEFT JOIN (or LEFT OUTER JOIN)
The LEFT JOIN keyword returns all records from the left table (table1), and the matched records from the right table (table2). The result is NULL from the right side if there is no match.
<sql>
SELECT columns
FROM table1
LEFT JOIN table2
ON table1.column_name = table2.column_name;


3. RIGHT JOIN (or RIGHT OUTER JOIN)
The RIGHT JOIN keyword returns all records from the right table (table2), and the matched records from the left table (table1). The result is NULL from the left side when there is no match.
<sql>
SELECT columns
FROM table1
RIGHT JOIN table2
ON table1.column_name = table2.column_name;


4. FULL JOIN (or FULL OUTER JOIN)
The FULL JOIN keyword returns all records when there is a match in either the left (table1) or the right (table2) table records.
<sql>
SELECT columns
FROM table1
FULL JOIN table2
ON table1.column_name = table2.column_name;


5. CROSS JOIN
The CROSS JOIN keyword returns the Cartesian product of the two tables, i.e., it combines each row from the first table with every row from the second table.
<sql>
SELECT columns
FROM table1
CROSS JOIN table2;

*****************************END********************************************

- use this command to copy all the installed packages to a folder <pip freeze > requirements.txt>
- use this command to automatically install all the packages from a requirement file in a new python environment: <pip install -r requirements.txt>

- use HEROKU to deploy your application for free
- create an account there
- install Heroku cli on your machine from Heroku website
- log in to Heroku <heroku login>, it prompts a window to login
- create an app <heroku create <app-name(unique)>>
- a new remote is created called heroku in github(we now have origin and heroku)
- use <git push heroku main> to push application to heroku
- create a new file called Procfile to specify the command you want to run for your app to start <Procfile> without extension and with capital letter
enter this command to start the app( for our case):
<web: uvicorn app.main:app --host=0.0.0.0  --port=${PORT:-5000} >
- save and push back to heroku
go on heroku platform to launch your application
- use <heroku logs> to view logs if there are issues
- search for heroku sql(postgres or mysql) ttutorial to see how to create a mysql isntance in heroku
- go to heroku dashboard and search for the new sql instance and and configure the connection settings to your database <11:48>
-dont do alembic revisions in production environment, do it in developpment environemt and push it to to heroku main.
- after starting the app, you have to run the alembic commands to upgrade the actual database situation in heroku mysql database
- installing actuall tables in heroku: <heroku run "alembic upgrade head">
- you can use the database infos in heroku to connect to your database from your local device


*************************Docker*****************************
- building a docker container to store the app
- install docker from web
- create a file called <Dockerfile> without extension
- add in all necessary configuration for build
- build container <docker build -t docker_python_api_project .>
- if a change is made only in code then just run the last command in dockerfile
- if any new package is added in requirement file then run the 3 last commands
- docker-compose can be used to run the containers, instead of just entering <docker run>
- to run containers in docker yaml file so we are not directly connected to it: <docker-compose  up -d>
- this are the two ways to pass in environemt file:
****************************************************
env_file:
    - ./.env

    <or>

environment:
    - DATABASE_HOSTNAME=local
    - DATABASE_PASSWORD=adm
    - DATABASE_USERNAME=ro
    - DATABASE_PORT=3
    - DATABASE_NAME=p
    - SECRET_KEY=ghfgh5fghfg65j
    - ALGORITHM=HS2
    - ACCESS_TOKEN_EXPIRE_MINUTES=30
*****************************

- stop all containers <docker-composer down>
- view all containers: <docker-compose ps -a>
- open a specific container in shell mode in docker: <docker exec -it <container-name> bash>
- binding docker files with local files: 
  volumes:
    <localpath>:<dockerpath>
- create a new repository in your docker account if you want to save your appp in a docker
- to login to the docker account <docker login> and follow steps
- rename your image to push it to repository: <docker tag [image_name] [new_user_name(docker_username/repository_name:tag(optional))]>
- use <docker push <image-name>> to push image to your repository after login in docker

*************************End*****************************

**********************Testing***************************
- install test package pytest <pip install pytest>
- import Testclient from fastapi <from fastapi.testclient import TestClient>
- you can specify what file to test: <pytest -n -s path//to//file.py>
- to disable warning: <pytest --disable-warnings>
- pass the <-x> flag if you want pytest to stop after the first test failure
- using independant database for test purpose: <15:27>