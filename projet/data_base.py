# Python file to access and read our inginious database.
# Authors : Arys Simon, Alsteens Louis, El Ouilinti Aymen.

import sqlite3

#Pour pouvoir utiliser la base de données depuis le fichier de unittest.
import os.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(BASE_DIR, "inginious.sqlite")


#-------------------------
#Graphique cours LSINF1252
def nbr_de_chaque_result():
    """
    @pre: /
    @post: Retourne une liste contenant le nombre de timeout, success, overflow, killed, failed, crash
    """

    conn = sqlite3.connect(database_path)
    # Le curseur permettra l'envoi des commandes SQL
    cursor = conn.cursor()
    timeout = 0
    success = 0
    overflow = 0
    killed = 0
    failed = 0
    crash = 0
    # Augmenter les variables correspondantes
    for row in cursor.execute("SELECT course, result from submissions"):
        # Sélectionner seulement le cours LSINF1252
        if row[0] == 'LSINF1101-PYTHON':
            if row[1] == 'timeout':
                timeout += 1
            elif row[1] == 'success':
                success += 1
            elif row[1] == 'overflow':
                overflow += 1
            elif row[1] == 'killed':
                killed += 1
            elif row[1] == 'failed':
                failed += 1
            elif row[1] == 'crash':
                crash += 1

    conn.close()

    return [timeout, success//25, overflow, killed, failed//50, crash]




#---------------------------------
#Graphique cours LSINF1101-PYTHON
def nbr_etudiants_nbr_essais_moyens():
    """
    @pre : /
    @post: Retourne un tuple contenant les listes des données des axes x et y du futur graphique.
    """
    nbr_essais_moyen_par_etudiants = {"0" : 0, "1" : 0, "2" : 0, "3->4" : 0, "5->6" : 0, "7->8" : 0, "9->10" : 0, "11->15" : 0, "16->20" : 0, "21->29" : 0, "30+" : 0}
    essais_par_etudiant = {}     # {'nom' : (essais_totaux, tâches_réalisées) }, afin de faire la moyenne par la suite

    # Accès à la base de données
    conn = sqlite3.connect(database_path)
    # Le curseur permettra l'envoi des commandes SQL
    cursor = conn.cursor()

    # Remplir le dictionnaire avec le nombre d'essais totaux et le nombres de tâches réalisées.
    for row in cursor.execute("SELECT course, username, tried from user_tasks"):
        # Sélectionner seulement le cours LSINF1101-PYTHON
        if row[0] == 'LSINF1101-PYTHON':
            current = essais_par_etudiant.get(row[1], (0, 0))
            current = (current[0]+row[2], current[1]+1)
            essais_par_etudiant[row[1]] = current

    conn.close()

    for essais_et_taches in essais_par_etudiant.values():
        # Faire la moyenne
        result = essais_et_taches[0]/essais_et_taches[1]

        # Ajouter 1 dans la tranche correspondante
        if result < 0.5:
            nbr_essais_moyen_par_etudiants["0"] = nbr_essais_moyen_par_etudiants.get("0", 0) +1
        elif result <= 1.5:
            nbr_essais_moyen_par_etudiants["1"] = nbr_essais_moyen_par_etudiants.get("1", 0) +1
        elif result <= 2.5:
            nbr_essais_moyen_par_etudiants["2"] = nbr_essais_moyen_par_etudiants.get("2", 0) +1
        elif result <= 4.5:
            nbr_essais_moyen_par_etudiants["3->4"] = nbr_essais_moyen_par_etudiants.get("3->4", 0) +1
        elif result <= 6.5:
            nbr_essais_moyen_par_etudiants["5->6"] = nbr_essais_moyen_par_etudiants.get("5->6", 0) +1
        elif result <= 8.5:
            nbr_essais_moyen_par_etudiants["7->8"] = nbr_essais_moyen_par_etudiants.get("7->8", 0) +1
        elif result <= 10.5:
            nbr_essais_moyen_par_etudiants["9->10"] = nbr_essais_moyen_par_etudiants.get("9->10", 0) +1
        elif result <= 15.5:
            nbr_essais_moyen_par_etudiants["11->15"] = nbr_essais_moyen_par_etudiants.get("11->15", 0) +1
        elif result <= 20.5:
            nbr_essais_moyen_par_etudiants["16->20"] = nbr_essais_moyen_par_etudiants.get("16->20", 0) +1
        elif result <= 29.5:
            nbr_essais_moyen_par_etudiants["21->29"] = nbr_essais_moyen_par_etudiants.get("21->29", 0) +1
        else:
            nbr_essais_moyen_par_etudiants["30+"] = nbr_essais_moyen_par_etudiants.get("30+", 0) +1

    datas = [[], []]
    for x,y in nbr_essais_moyen_par_etudiants.items():
        datas[0].append(x)
        datas[1].append(y)
    return datas





#-------------------------
#Graphique cours LELP1402
def nbr_reussis_nbr_rates():
    """
    @pre : /
    @post: Retourne une liste contenant les données de l'axe y du futur graphique.
    """
    # Accès à la base de données
    conn = sqlite3.connect('inginious.sqlite')
    # Le curseur permettra l'envoi des commandes SQL
    cursor = conn.cursor()
    reussis = 0
    rates = 0
    # Augmenter les deux variables avec le nombre de réussis et de ratés
    for row in cursor.execute("SELECT course, succeeded from user_tasks"):
        # Sélectionner seulement le cours LEPL1402
        if row[0] == 'LEPL1402':
            if row[1] == 'true':
                reussis += 1
            else:
                rates += 1

    conn.close()

    return [reussis, rates]
