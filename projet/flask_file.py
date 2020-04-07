# Main Python file to run our Website with graphics based on Inginious.
# Authors : Arys Simon, Alsteens Louis, El Ouilinti Aymen.

import page_creator
import data_base


from flask import Flask, render_template, url_for
app = Flask(__name__)



@app.route('/')
def index():
    """
    retourne le contenu de la page index.html
    """
    return render_template('index.html')

@app.route('/graphique')
def graphique():
    """
    retourne le contenu de la page graphique.html
    """
    liste_x = []
    liste_y = []
    for x,y in data_base.get_datas().items():
        liste_x.append(x)
        liste_y.append(y)
    return page_creator.html_page_creator("Nombre d'essais par cours", 'Page HTML affichant un graphique basé sur les données de la database Inginious', liste_x, liste_y)

@app.route('/auteurs')
def auteurs():
    """
    retourne le contenu de la page index.html
    """
    return render_template('auteurs.html')

if __name__ == '__main__':
    app.run()
