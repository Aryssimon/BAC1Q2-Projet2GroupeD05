# Main Python file to run our Website with graphics based on Inginious.
# Authors : Arys Simon, Alsteens Louis, El Ouilinti Aymen.

import page_creator


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
    return "en travaux" #page_creator.html_page_creator(dates, cases)

if __name__ == '__main__':
    app.run()
