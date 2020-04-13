# Main Python file to run our Website with graphics based on Inginious.
# Authors : Arys Simon, Alsteens Louis, El Ouilinti Aymen.

import page_creator
import data_base


from flask import Flask, render_template, url_for
app = Flask(__name__)


def get_data_from_dict(cours):
    """
    @pre:   <cours> nom du cours: LSINF1252, LSINF1101-PYTHON ou LEPL1402.
    @post:  Retourne un tuple contenant les listes des données de x et de y.
    """
    datas = ([], [])
    for x,y in data_base.get_datas(cours).items():
        datas[0].append(x)
        datas[1].append(y)
    return datas

@app.route('/')
def index():
    """
    retourne le contenu de la page index.html
    """
    return render_template('index.html')

@app.route('/selection_graphique')
def selection_graphique():
    """
    retourne le contenu de la page graphique.html
    """
    return render_template('selection_graphique.html')

@app.route('/graphique_lsinf1252')
def graphique_lsinf1252():
    """
    retourne le contenu de la page graphique.html
    """
    x_et_y = get_data_from_dict('LSINF1252')
    return page_creator.html_page_creator("LSINF1252 : Nombre d'étudiants par nombre d'essais moyens", 'Page HTML affichant un graphique basé sur les données de la database Inginious', x_et_y[0], x_et_y[1])

@app.route('/graphique_lsinf1101-python')
def graphique_lsinf1101_python():
    """
    retourne le contenu de la page graphique.html
    """
    x_et_y = get_data_from_dict('LSINF1101-PYTHON')
    return page_creator.html_page_creator("LSINF1101-PYTHON : Nombre d'étudiants par nombre d'essais moyens", 'Page HTML affichant un graphique basé sur les données de la database Inginious', x_et_y[0], x_et_y[1])

@app.route('/graphique_lepl1402')
def graphique_lepl1402():
    """
    retourne le contenu de la page graphique.html
    """
    x_et_y = get_data_from_dict('LEPL1402')
    return page_creator.html_page_creator("LEPL1402 : Nombre d'étudiants par nombre d'essais moyens", 'Page HTML affichant un graphique basé sur les données de la database Inginious', x_et_y[0], x_et_y[1])


@app.route('/auteurs')
def auteurs():
    """
    retourne le contenu de la page index.html
    """
    return render_template('auteurs.html')

if __name__ == '__main__':
    app.run()
