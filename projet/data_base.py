# Python file to access and read our database.
# Authors : Arys Simon, Alsteens Louis, El Ouilinti Aymen.

import sqlite3 as sq

# Accès à la base de données

conn = sqlite3.connect('{{ url_for('static',filename='inginious.sqlite') }}')

# Le curseur permettra l'envoi des commandes SQL
cursor = conn.cursor()

# utilisation de la base de données

# Si on a fait des modifications à la base de données
conn.commit()

# Toujours fermer la connexion quand elle n'est plus utile
conn.close()


id=[]
for row in cursor.execute("SELECT id FROM submissions"):
    id.append(row)

course=[]
for row in cursor.execute("SELECT course FROM submissions"):
    course.append(row)

status=[]
for row in cursor.execute("SELECT status FROM submissions"):
    status.append(row)

submitted_on=[]
for row in cursor.execute("SELECT submitted_on FROM submissions"):
    submitted_on.append(row)

username=[]
for row in cursor.execute("SELECT username FROM submissions"):
    username.append(row)

response_type=[]
for row in cursor.execute("SELECT response_type FROM submissions"):
    response_type.append(row)

grade=[]
for row in cursor.execute("SELECT grade FROM submissions"):
    grade.append(row)

result = []
for row in cursor.execute("SELECT result FROM submissions"):
    result.append(row)

submission=[]
for row in cursor.execute("SELECT submission FROM user_tasks "):
    submission.append(row)

succeeded=[]
for row in cursor.execute("SELECT succeeded FROM user_tasks "):
    succeeded.append(row)

tried=[]
for row in cursor.execute("SELECT tried FROM user_tasks "):
    tried.append(row)

# def get_datas():
    #return [nom, points, jesaispas]
