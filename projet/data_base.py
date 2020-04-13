# Python file to access and read our inginious database.
# Authors : Arys Simon, Alsteens Louis, El Ouilinti Aymen.

import sqlite3

def get_datas(cours):
    """
    @pre : <cours> string contenant: 'LSINF1252', 'LSINF1101-PYTHON' ou 'LEPL1402'.
    @post: Retourne un dictionnaire contenant des tranches de nombre d'essais et le nombre d'étudiants associé.
    """
    nbr_essais_moyen_par_etudiants = {"0" : 0, "1" : 0, "2" : 0, "3->4" : 0, "5->6" : 0, "7->8" : 0, "9->10" : 0, "11->15" : 0, "16->20" : 0, "21->29" : 0, "30+" : 0}
    essais_par_etudiant = {}     # {'nom' : (essais_totaux, tâches_réalisées) }

    # Accès à la base de données
    conn = sqlite3.connect('inginious.sqlite')
    # Le curseur permettra l'envoi des commandes SQL
    cursor = conn.cursor()

    # Remplir le dictionnaire avec le noombre d'essais totaux et le nombres de tâches réalisées.
    for row in cursor.execute("SELECT course, username, tried from user_tasks"):
        # Sélectionner seulement le cours passé en argument
        if row[0] == cours:
            current = essais_par_etudiant.get(row[1], (0, 0))
            current = (current[0]+row[2], current[1]+1)
            essais_par_etudiant[row[1]] = current

    conn.close()

    for essais_et_taches in essais_par_etudiant.values():
        # faire la moyenne
        result = essais_et_taches[0]/essais_et_taches[1]

        #Ajouter 1 dans la tranche correspondante
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


    return nbr_essais_moyen_par_etudiants
