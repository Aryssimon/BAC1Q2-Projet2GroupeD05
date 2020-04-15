#Python file containing the unittests for the <data_base.py> file.
# Authors : Arys Simon, Alsteens Louis, El Ouilinti Aymen.


import unittest
import sys
sys.path.append('../projet')
import data_base


class Test_Data_Base(unittest.TestCase):

    datas_0 = data_base.get_datas_from_dict('LSINF1252')
    datas_1 = data_base.get_datas_from_dict('LSINF1101-PYTHON')
    datas_2 = data_base.get_datas_from_dict('LEPL1402')

    def test0_len_0(self):
        x = Test_Data_Base.datas_0[0]
        y = Test_Data_Base.datas_0[1]
        self.assertEqual(len(x), len(y), "Les listes ne sont pas de mêmes taillles pour le cours: LSINF1252.")

    def test0_len_1(self):
        x = Test_Data_Base.datas_1[0]
        y = Test_Data_Base.datas_1[1]
        self.assertEqual(len(x), len(y), "Les listes ne sont pas de mêmes taillles pour le cours: LSINF1101-PYTHON.")

    def test0_len_2(self):
        x = Test_Data_Base.datas_2[0]
        y = Test_Data_Base.datas_2[1]
        self.assertEqual(len(x), len(y), "Les listes ne sont pas de mêmes taillles pour le cours: LEPL1402.")

    def test1_verify_numbers_0(self):
        liste_x = Test_Data_Base.datas_0[0]
        self.assertEqual(liste_x, ['0', '1', '2', '3->4', '5->6', '7->8', '9->10', '11->15', '16->20', '21->29', '30+'], "La liste x n'est pas celle attendue pour le cours: LSINF1252.")

    def test1_verify_numbers_1(self):
        liste_x = Test_Data_Base.datas_1[0]
        self.assertEqual(liste_x, ['0', '1', '2', '3->4', '5->6', '7->8', '9->10', '11->15', '16->20', '21->29', '30+'], "La liste x n'est pas celle attendue pour le cours: LSINF1101-PYTHON.")

    def test1_verify_numbers_2(self):
        liste_x = Test_Data_Base.datas_2[0]
        self.assertEqual(liste_x, ['0', '1', '2', '3->4', '5->6', '7->8', '9->10', '11->15', '16->20', '21->29', '30+'], "La liste x n'est pas celle attendue pour le cours: LEPL1402.")


if __name__ == '__main__':
    unittest.main()
