# Python file containing the function designed to create the html pages with chartjs graphs.
# Authors : Arys Simon, Alsteens Louis, El Ouilinti Aymen.

def html_page_creator(label, x_axis, y_axis):
    """
    @Pre:   <label> Le titre du graphique (str).
            <x_axis> et <y_axis> deux listes représentants les données des axes x et y.

    @Post:  Retourne une page html affichant un graphique contenant les données entrées en paramètres.
    """

    html_page = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="author" content="Alsteens Louis, Arys Simon, El Ouilinti Aymen">
  <meta name="description" content="Page HTML affichant un graphique basé sur les données de la database Inginious">
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
  <h1 title="Retour à l'accueil"><a href="/" id="title">Projet 2 - Visualisation Inginious</a></h1>
  <canvas id="mon_graphique" width="100%" height="45%"></canvas>
  <script>
    var ctx = document.getElementById('mon_graphique').getContext('2d');
    // Creation du graphique
    var myChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: """+str(x_axis)+""" ,
        datasets: [{
          label: """+'"'+label+'"'+""",
          data: """+str(y_axis)+""",
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
            "#0000ff"
          ]
        }]
      }
    });
  </script>
</body>
</html>
"""
    return html_page
