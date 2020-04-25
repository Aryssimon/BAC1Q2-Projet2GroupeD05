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

@app.route('/graphique_lsinf1252')
def graphique_lsinf1252():
    """Retourne une page affichant un graphique Chartjs du cours LSINF1252."""
    x = ["Timeout", "Success/25", "Overflow", "Killed", "Failed/50", "Crash"]
    y = data_base.nbr_de_chaque_result()
    colors = """backgroundColor: [
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
    return page_creator.html_page_creator("LSINF1252 : Nombre d'étudiants par nombre d'essais moyens", x, y, 'polarArea', colors)

@app.route('/graphique_lsinf1101-python')
def graphique_lsinf1101_python():
    """Retourne une page affichant un graphique Chartjs du cours LSINF1101-PYTHON."""
    x_et_y = data_base.nbr_etudiants_nbr_essais_moyens()
    colors = """backgroundColor: [
      "#1E90FF",
      "#1E90FF",
      "#1E90FF",
      "#1E90FF",
      "#1E90FF",
      "#1E90FF"
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
    return page_creator.html_page_creator("LSINF1101-PYTHON : Nombre d'étudiants par nombre d'essais moyens", x_et_y[0], x_et_y[1], 'bar', colors)

@app.route('/graphique_lepl1402')
def graphique_lepl1402():
    """Retourne une page affichant un graphique Chartjs du cours LEPL1402."""
    x = ["Réussis", "Ratés"]
    y = data_base.nbr_reussis_nbr_rates()
    colors = """backgroundColor: [
      "#09ff00",
      "#ff0000"
    ],
    hoverBackgroundColor: [
      "#07cc00",
      "#c20000" """
    return page_creator.html_page_creator("LEPL1402 : Nombre d'étudiants ayant réussis et ratés", x, y, 'pie', colors)



if __name__ == '__main__':
    app.run()
