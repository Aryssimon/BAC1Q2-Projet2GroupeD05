# Python file containing the function designed to create the html pages with chartjs graphs.
# Authors : Arys Simon, Alsteens Louis, El Ouilinti Aymen.

def html_page_creator(label, description, x_axis, y_axis):
    """
    @Pre  - <label> Le titre du graphique (str).
            <description> Description de la page HTML (str).
            <x_axis> et <y_axis> deux listes représentants les données des axes x et y.

    @Post - Retourne une page html affichant un graphique contenant les données entrées en paramètres.
    """


    html_page = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="author" content="Alsteens Louis, Arys Simon, El Ouilinti Aymen">
  <meta name="description" content=" """+description+""" ">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.bundle.min.js"></script>
  <title>Projet2, Graphiques Inginious</title>
</head>
<body>
  <canvas id="mon_graphique" width="200px" height="200px"></canvas>
  <script>
    var ctx = document.getElementById('mon_graphique').getContext('2d');
    // Creation du graphique
    var myChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: """+str(x_axis)+""" ,
        datasets: [{
          label: '"""+label+"""',
          data: """+str(y_axis)+"""
        }]
      }
    });
  </script>
</body>
</html>"""
    return html_page
