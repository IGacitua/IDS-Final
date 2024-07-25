# Tutorial for launching the db and server using python, psql and flask-sqlalchemy

 - Go to the folder called Backend from the terminal and run the following sequence of commands:


```
    virtualenv venv
    source venv/bin/activate
    pip install -r requeriments.txt
    python3 app.py
```

 - To start the database, open another terminal and run the following commands:

```
    (your_username and your_db correspond to the username you create with psql, and the code in line 9 of app.py is for that same purpose)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://username:password@localhost:5432my_db'
    
    psql -U your_username -h localhost -d your_db 
```
  - To start the front end page, go to the folder called Frontend, and start yet another terminal:

```
    python3 -m http.server
```
  - If you want to start front end in a specific port, specify it after http.server