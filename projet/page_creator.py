#Python file containing the functions designed to create the html pages.
# Authors : Arys Simon, Alsteens Louis, El Ouilinti Aymen.

def html_page_creator(dates, cases):
    """
    Doc de merde
    """


    html_page = """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
      <meta charset="utf-8">
      <meta name="author" content="Arys Simon">
      <meta name="description" content="Exemple de page HTML contenant une visualisation des données liées au Covid-19.">
      <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.bundle.min.js"></script>
      <title>Projet2, Graphiques Covid-19</title>
    </head>
    <body>
      <canvas id="mon_graphique" width="200px" height="200px"></canvas>
      <script>
        var ctx = document.getElementById('mon_graphique').getContext('2d');
        // Creation du graphique
        var myChart = new Chart(ctx, {
          type: 'bar',
          data: {
            labels: """+str(dates)+""" ,
            datasets: [{
              label: 'Confirmed_cases',
              data: """+str(cases)+"""
            }]
          }
        });
      </script>
    </body>
    </html>"""
    return html_page
