#Python file containing the unittests for the <page_creator.py> file.
# Authors : Arys Simon, Alsteens Louis, El Ouilinti Aymen.


import unittest
import sys
sys.path.append('../projet')
import page_creator


class Test_Page_Creator(unittest.TestCase):

    def test0_normal(self):
        result_created = page_creator.html_page_creator('test_label', "Exemple de page HTML.", ["01/01/20", "02/01/20", "03/01/20", "04/01/20"], [10,15,100,50000])
        right_result ="""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="author" content="Alsteens Louis, Arys Simon, El Ouilinti Aymen">
  <meta name="description" content="Exemple de page HTML.">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.bundle.min.js"></script>
  <title>Projet2, Graphiques Inginious</title>

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
  <h1 title="Retour à l'acceuil"><a href="/" id="title">Projet 2 - Visualisation Inginious</a></h1>
  <canvas id="mon_graphique" width="200px" height="200px"></canvas>
  <script>
    var ctx = document.getElementById('mon_graphique').getContext('2d');
    // Creation du graphique
    var myChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['01/01/20', '02/01/20', '03/01/20', '04/01/20'] ,
        datasets: [{
          label: "test_label",
          data: [10, 15, 100, 50000]
        }]
      }
    });
  </script>
</body>
</html>"""
        self.assertEqual(result_created, right_result, "The page created isn't correct.")


if __name__ == '__main__':
    unittest.main()
