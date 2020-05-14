# Main Python file to run our Website with graphics based on Inginious Database.
# Authors : Arys Simon, Alsteens Louis, El Ouilinti Aymen.

import page_creator
import data_base
from flask import Flask, render_template, url_for


app = Flask(__name__)

#---------Les pages principales---------
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

#--------------------------------------------------------------------------
#-------------------------Resultats des soumissions------------------------
#--------------------------------------------------------------------------
@app.route('/graphiques_resultats/<cours>')
def graphique_resultats(cours):
    """Retourne une page affichant un graphique Chartjs des resultats des soumissions."""
    y = data_base.nbr_de_chaque_result(cours)
    x = ["%Timeout", "%Crash", "%Overflow", "%Killed", "%Success", "%Failed"]
    colors_resultats = """,
    backgroundColor: [
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
      "#c800cf" ]"""
    return page_creator.html_page_creator(cours+" : Resultats des soumissions", x, y, 'pie', colors_resultats)



#--------------------------------------------------------------------------
#----------------Nombre d'etudiants par essais moyens----------------------
#--------------------------------------------------------------------------
@app.route('/graphiques_essais/<cours>')
def graphique_essais(cours):
    """Retourne une page affichant un graphique Chartjs du nombre d'etudiants par nombre d essais moyens"""
    x_et_y = data_base.nbr_etudiants_nbr_essais_moyens(cours)
    colors_essais = """,
    backgroundColor: [
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
      "#0000ff" ]"""
    return page_creator.html_page_creator(cours+" : Nombre d etudiants(y) par nombre d essais moyens(x)", x_et_y[0], x_et_y[1], 'bar', colors_essais)



#----------------------------------------------------
#---------------Reussis / Rates----------------------
#----------------------------------------------------
@app.route('/graphiques_reussis_rates/<cours>')
def graphique_reussis_rates(cours):
    """Retourne une page affichant un graphique Chartjs le pourcentage de reussites et d echecs"""
    x = ["%Soumissions reussies", "%Soumissions rates"]
    y = data_base.nbr_reussis_nbr_rates(cours)
    colors_reussis_rates = """,
    backgroundColor: [
      "#09ff00",
      "#ff0000"
    ],
    hoverBackgroundColor: [
      "#07cc00",
      "#c20000" ]"""
    return page_creator.html_page_creator(cours+" : Pourcentage de soumissions reussies ou rates", x, y, 'pie', colors_reussis_rates)



#----------------------------------------------------
#--------------Soumissions par jour----------------------
#----------------------------------------------------
@app.route('/graphiques_sub_per_day/<cours>')
def graphique_sub_per_day(cours):
    """Retourne une page affichant un graphique Chartjs le nombre de soumissions par jour"""
    res = data_base.nbr_submissions_per_day(cours)
    x = res[0]
    y = res[1]
    return page_creator.html_page_creator(cours+" : Nombre de soumissions par jour", x, y, 'line')


#---------------------------------------------
#------------Taux de reussite-----------------
#---------------------------------------------
@app.route('/graphique_taux_de_reussite')
def graphique_taux_de_reussite():
    """Retourne une page affichant un graphique Chartjs de comparaison du taux de reussite entre les sinfs et les ingis."""
    x = ["Sinf", "Ingi"]
    y = data_base.taux_de_reussite()
    return page_creator.html_page_creator("Taux de reussite", x, y, 'bar', colors_taux_de_reussite, options_taux)

colors_taux_de_reussite = """,
backgroundColor: [
  "#42baff",
  "#42baff"
],
hoverBackgroundColor: [
  "#39a0db",
  "#39a0db" ]"""

options_taux = """,
options: {
  scales: {
      yAxes: [{
      ticks: {
             min: 0,
             max: 100
          }
      }]
  }
}
"""



if __name__ == '__main__':
    app.run()
