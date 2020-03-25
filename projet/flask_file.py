# Python file to create a html page with graphics on the covid-19, with the data of https://ourworldindata.org/coronavirus-source-data
# Authors : Arys Simon, Alsteens Louis, El Ouilinti Aymen.

import page_creator
import translate_file


from flask import Flask, render_template, url_for
app = Flask(__name__)



@app.route('/')
def index():
    """
    retourne le contenu de la page index.html
    """
    return render_template('index.html')
    #with open('index.html') as file:
        #return file.read()

@app.route('/graphique')
def graphique():
    """
    retourne le contenu de la page graphique.html
    """
    dates_and_cases = translate_file.file_to_graph('total_cases.csv')
    dates = dates_and_cases[0]
    cases = dates_and_cases[1]
    return page_creator.html_page_creator(dates, cases)

if __name__ == '__main__':
    app.run()
