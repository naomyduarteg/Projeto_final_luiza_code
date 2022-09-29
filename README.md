<h1 align='left'> CRUD with Python and MongoDB using FastAPI </h1>

## Motivation <a name="motivation"></a>

This project is a simplified CRUD API REST exercise in Python with MongoDB as the database and using FastAPI. Its main
objective is to create, read, update and delete users, user's addresses and products. The structure of this project is as follows:
<pre>
<code>
├── CRUD_python_mongo
│   │── env
│   ├── routes
│   │     └── api.py
│   ├── src
│   │    ├── __init__.py
│   │    ├── endpoints
│   │    │      ├── __init__.py
│   │    │      ├── products.py
│   │    │      └── users.py
│   │    │
│   │    └── models
│   │           ├── __init__.py
│   │           ├── products.py
│   │           └── users.py
│   ├── __init__.py
│   ├── main.py
 </code>
</pre>
## Instructins <a name="instruction"></a>
1. Clone the folder in the repository:

```
https://github.com/naomyduarteg/Portfolio/CRUD_python_mongo.git
```
2. Create a virtual environement

```
python -m venv <name_of_venv>
```
3. Go to your venv's folder and activate the virtual environement

On Windows:
```
Scripts/activate
```
On Linux/Mac:
```
bin/activate
```
4. Install the required libraries

```
pip install -r requirements.txt
```
5. Go to your MongoDB account https://cloud.mongodb.com/ and create or connect to an existing cluster. Choose "Connect you application" and copy the connection string. Put it on .env at ATLAS_URI and don't forget to change "password" by your password. 

6. Run the API:

```
uvicorn main:app --reload
```

You should see the message "Connected to the MongoDB database!" if everything is working. Copy and go to the address that appears on the terminal when the API runs correctly: http://127.0.0.1:8000. At the docs page, http://127.0.0.1:8000/docs, 
you can test the API. 
It is also possible to verify the collections and documents on MongoDB Compass by connecting using the ATLAS_URI address at the .env directory. This is what you should see at your MongoDB Compass Collections once you create users, addresses and items:
![image](https://user-images.githubusercontent.com/73078250/193099896-1ca937e9-41eb-4746-8914-d0d8e87bd38c.png)
