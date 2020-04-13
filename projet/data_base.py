# Python file to access and read our inginious database.
# Authors : Arys Simon, Alsteens Louis, El Ouilinti Aymen.

import sqlite3

def get_datas(cours):
    """
    @pre : <cours> string contenant: 'lsinf1252', 'lsinf1101-python' ou 'lepl1402'.
    @post: Retourne un dictionnaire contenant les cours et le nombre d'essais.
    """
    # Accès à la base de données
    conn = sqlite3.connect('inginious.sqlite')
    # Le curseur permettra l'envoi des commandes SQL
    cursor = conn.cursor()

    nbr_essais_par_cours = {}

    for row in cursor.execute("SELECT course, tried from user_tasks"):
        nbr_essais_par_cours[row[0]] = nbr_essais_par_cours.get(row[0], 0) + row[1]

    conn.close()

    return nbr_essais_par_cours

print(get_datas())
