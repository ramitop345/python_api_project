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
