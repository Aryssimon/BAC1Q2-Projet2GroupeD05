# Python file containing the function designed to create the html pages with chartjs graphs.
# Authors : Arys Simon, Alsteens Louis, El Ouilinti Aymen.

def html_page_creator(label, x_axis, y_axis, type, colors="", options=""):
    """
    @Pre:   <label> Le titre du graphique (str).
            <x_axis> et <y_axis> deux listes representants les donnees des axes x et y.
            <type> string representant le type de graphique (bar, pie, radar, polarArea, scatter, bubble, line).
            <colors> string representant le backgroundColor et le hoverBackgroundColor.

    @Post:  Retourne une page html affichant un graphique contenant les donnees entrees en parametres.
    """

    html_page = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="author" content="Alsteens Louis, Arys Simon, El Ouilinti Aymen">
  <meta name="description" content="Page HTML affichant un graphique base sur les donnees de la database Inginious">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.bundle.min.js"></script>
  <title>Projet2 - Graphique Inginious</title>

  <style>
    h1 {
      text-align: center;
      margin: 1%;
      border: 4px double #1E90FF;
      background-color: white;
    }

    #title{
      color: #1E90FF;
      text-decoration: none;
    }

    #title:hover {
      font-weight: bold;
      color: blue;
    }
  </style>

</head>

<body>
  <h1 title="Retour a l accueil"><a href="/" id="title">Projet 2 - Visualisation Inginious</a></h1>
  <canvas id="mon_graphique" width="100%" height="45%"></canvas>
  <script>
    var ctx = document.getElementById('mon_graphique').getContext('2d');
    // Creation du graphique
    var myChart = new Chart(ctx, {
      type: """+'"'+type+'"'+""",
      data: {
        labels: """+str(x_axis)+""" ,
        datasets: [{
          label: """+'"'+label+'"'+""",
          data: """+str(y_axis)+""" """+colors+"""
        }]
      }"""+options+"""
    });
  </script>
</body>
</html>
"""
    return html_page
