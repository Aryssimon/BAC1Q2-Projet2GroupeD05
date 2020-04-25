import sqlite3
# Accès à la base de données
conn = sqlite3.connect('inginious.sqlite')
# Le curseur permettra l'envoi des commandes SQL
cursor = conn.cursor()
reussis = 0
rates = 0
# Remplir le dictionnaire avec le noombre d'essais totaux et le nombres de tâches réalisées.
for row in cursor.execute("SELECT course, succeeded from user_tasks"):
    # Sélectionner seulement le cours LEPL1402
    if row[0] == 'LEPL1402':
        if row[1] == 'true':
            reussis += 1
        else:
            rates += 1

conn.close()
