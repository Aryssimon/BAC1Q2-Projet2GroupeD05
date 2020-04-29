# Main Python file to run our Website with graphics based on Inginious Database.
# Authors : Arys Simon, Alsteens Louis, El Ouilinti Aymen.

import page_creator
import data_base
from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
def accueil():
    """Retourne le contenu de la page index.html."""
    return render_template('index.html')

@app.route('/selection_graphique')
def selection_graphique():
    """Retourne le contenu de la page graphique.html."""
    return render_template('selection_graphique.html')

@app.route('/auteurs')
def auteurs():
    """retourne le contenu de la page index.html"""
    return render_template('auteurs.html')


#-----Les pages de graphiques Chartjs------

@app.route('/graphique_resultats_lepl1402')
def graphique_resultats_lepl1402():
    """Retourne une page affichant un graphique Chartjs des résultats des soumissions."""
    x = ["Timeout", "Success/25", "Overflow", "Killed", "Failed/50", "Crash"]
    y = data_base.nbr_de_chaque_result('LEPL1402')
    return page_creator.html_page_creator("LEPL1402 : Résultats des soumissions", x, y, 'polarArea', colors_resultats)

@app.route('/graphique_resultats_lsinf1101_python')
def graphique_resultats_lsinf1101_python():
    """Retourne une page affichant un graphique Chartjs des résultats des soumissions."""
    x = ["Timeout", "Success/25", "Overflow", "Killed", "Failed/50", "Crash"]
    y = data_base.nbr_de_chaque_result('LSINF1101-PYTHON')
    return page_creator.html_page_creator("LSINF1101-PYTHON : Résultats des soumissions", x, y, 'polarArea', colors_resultats)

@app.route('/graphique_resultats_lsinf1252')
def graphique_resultats_lsinf1252():
    """Retourne une page affichant un graphique Chartjs des résultats des soumissions."""
    x = ["Timeout", "Success/25", "Overflow", "Killed", "Failed/50", "Crash"]
    y = data_base.nbr_de_chaque_result('LSINF1252')
    return page_creator.html_page_creator("LSINF1252 : Résultats des soumissions", x, y, 'polarArea', colors_resultats)

colors_resultats = """backgroundColor: [
  "#ff0000",
  "#fff200",
  "#09ff00",
  "#00ffff",
  "#1500ff",
  "#f700ff"
],
hoverBackgroundColor: [
  "#c20000",
  "#ebdf00",
  "#07cc00",
  "#00e3e3",
  "#1100cc",
  "#c800cf" """



#--------------------------------------------------------------------------
#----------------Nombre d'étudiants par essais moyens----------------------
#--------------------------------------------------------------------------
@app.route('/graphique_essais_lepl1402')
def graphique_essais_lepl1402():
    """Retourne une page affichant un graphique Chartjs du cours LEPL1402."""
    x_et_y = data_base.nbr_etudiants_nbr_essais_moyens('LEPL1402')
    return page_creator.html_page_creator("LEPL1402 : Nombre d'essais moyens par nombre d'étudiants", x_et_y[0], x_et_y[1], 'bar', colors_essais)

@app.route('/graphique_essais_lsinf1101_python')
def graphique_essais_lsinf1101_python():
    """Retourne une page affichant un graphique Chartjs du cours LSINF1101-PYTHON."""
    x_et_y = data_base.nbr_etudiants_nbr_essais_moyens('LSINF1101-PYTHON')
    return page_creator.html_page_creator("LSINF1101-PYTHON : Nombre d'essais moyens par nombre d'étudiants", x_et_y[0], x_et_y[1], 'bar', colors_essais)

@app.route('/graphique_essais_lsinf1252')
def graphique_essais_lsinf1252():
    """Retourne une page affichant un graphique Chartjs du cours LEPL1402."""
    x_et_y = data_base.nbr_etudiants_nbr_essais_moyens('LSINF1252')
    return page_creator.html_page_creator("LSINF1252 : Nombre d'essais moyens par nombre d'étudiants", x_et_y[0], x_et_y[1], 'bar', colors_essais)

colors_essais = """backgroundColor: [
  "#1E90FF",
  "#1E90FF",
  "#1E90FF",
  "#1E90FF",
  "#1E90FF",
  "#1E90FF",
  "#1E90FF",
  "#1E90FF",
  "#1E90FF",
  "#1E90FF",
  "#1E90FF"
],
hoverBackgroundColor: [
  "#0000ff",
  "#0000ff",
  "#0000ff",
  "#0000ff",
  "#0000ff",
  "#0000ff",
  "#0000ff",
  "#0000ff",
  "#0000ff",
  "#0000ff",
  "#0000ff" """



#----------------------------------------------------
#-------------- Réussis / Ratés----------------------
#----------------------------------------------------

@app.route('/graphique_reussis_rates_lepl1402')
def graphique_reussis_rates_lepl1402():
    """Retourne une page affichant un graphique Chartjs du nombre de réussites et d'échecs pour le cours LEPL1402."""
    x = ["Réussis", "Ratés"]
    y = data_base.nbr_reussis_nbr_rates('LEPL1402')
    return page_creator.html_page_creator("LEPL1402: Nombre d'étudiants ayant réussis et ratés", x, y, 'pie', colors_reussis_rates)

@app.route('/graphique_reussis_rates_lsinf1101_python')
def graphique_reussis_rates_lsinf1101_python():
    """Retourne une page affichant un graphique Chartjs du nombre de réussites et d'échecs pour le cours LSINF1101-PYTHON."""
    x = ["Réussis", "Ratés"]
    y = data_base.nbr_reussis_nbr_rates('LSINF1101-PYTHON')
    return page_creator.html_page_creator("LSINF1101-PYTHON: Nombre d'étudiants ayant réussis et ratés", x, y, 'pie', colors_reussis_rates)

@app.route('/graphique_reussis_rates_lsinf1252')
def graphique_reussis_rates_lsinf1252():
    """Retourne une page affichant un graphique Chartjs du nombre de réussites et d'échecs pour le cours LSINF1252."""
    x = ["Réussis", "Ratés"]
    y = data_base.nbr_reussis_nbr_rates('LSINF1252')
    return page_creator.html_page_creator("LSINF1252: Nombre d'étudiants ayant réussis et ratés", x, y, 'pie', colors_reussis_rates)

colors_reussis_rates = """backgroundColor: [
  "#09ff00",
  "#ff0000"
],
hoverBackgroundColor: [
  "#07cc00",
  "#c20000" """


if __name__ == '__main__':
    app.run()
