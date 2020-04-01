# Python file to access and read our database.
# Authors : Arys Simon, Alsteens Louis, El Ouilinti Aymen.

import sqlite3 as sq

# Accès à la base de données

conn = sqlite3.connect('inginious.sqlite')

# Le curseur permettra l'envoi des commandes SQL
cursor = conn.cursor()

# utilisation de la base de données

# Si on a fait des modifications à la base de données
conn.commit()

# Toujours fermer la connexion quand elle n'est plus utile
conn.close()
