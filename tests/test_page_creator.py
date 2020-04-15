#Python file containing the unittests for the <page_creator.py> file.
# Authors : Arys Simon, Alsteens Louis, El Ouilinti Aymen.


import unittest
import sys
sys.path.append('../projet')
import page_creator


class Test_Page_Creator(unittest.TestCase):

    def test0_normal(self):
        result_created = page_creator.html_page_creator('test_label', ["01/01/20", "02/01/20", "03/01/20", "04/01/20"], [10,15,100,50000])
        with open('correct_html_page.html', 'r') as file:
            correct_result = file.read()
        self.assertEqual(result_created.replace("é", "e").replace("à", "a"), correct_result, "The page created isn't correct.")


if __name__ == '__main__':
    unittest.main()
