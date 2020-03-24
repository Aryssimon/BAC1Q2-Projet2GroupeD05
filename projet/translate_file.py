#Python file containing the functions designed to read and process files.
# Authors : Arys Simon, Alsteens Louis, El Ouilinti Aymen.

def file_to_graph(filename):
    """
    @Pre  - filename le nom d'un fichier avec son extension. exemple: 'covid19.csv'
    @Post - un tuple contenant une liste des dates et une listes des cas correspondants. exemple : (['01/01/2020', '...'], [12345, ...])
    """
    dates = []
    confirmed_cases = []

    try:
        with open(filename) as file:
            liste_cas = file.read().strip().split(',')
    except OSError:
        return ('file_not_found', -1)

    #Trouver le premier élément contenant '\n' car il contient la date, l'élément suivant est le nombre de cas totaux à cette date.
    for x in range(168, len(liste_cas)-168):
        if not liste_cas[x].isalpha():
            if '\n' in liste_cas[x]:
                splitted = liste_cas[x].split("\n")
                dates.append(splitted[-1])
                confirmed_cases.append(liste_cas[x+1])

    return (dates, confirmed_cases)
