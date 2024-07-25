# Tutorial for launching the db and server using python, psql and flask-sqlalchemy

- To start the database, open a terminal and run the following command:
  - your_username and your_db correspond to the username you create with psql. The code in line 9 of app.py is for that same purpose

```
    psql -U your_username -h localhost -d your_db
```

- Create a file named "editable.py" in the Backend folder and give it the following function:

```
    def return_db_name():
        return 'postgresql+psycopg2://your_username:password@localhost:5432/your_db'
```

- Go to the folder called Backend from the terminal and run the following sequence of commands:

```
    virtualenv venv
    source venv/bin/activate
    pip install -r requeriments.txt
    python app.py
```

- To start the front end page, go to the folder called Frontend, and start yet another terminal:

```
    python3 -m http.server
```

- If you want to start front end in a specific port, specify it after http.server
