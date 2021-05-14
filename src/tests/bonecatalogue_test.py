import unittest
import os
from services.bonecatalogue import Bonecatalogue
TESTDATA = os.path.join(os.path.dirname(__file__), "barts2.csv")


class TestBonecatalogue(unittest.TestCase):
    def setUp(self):
        self.catalogue = Bonecatalogue()
        self.catalogue.read_file(TESTDATA)

    def test_read_error(self):
        self.assertRaises(FileNotFoundError, lambda: self.catalogue.read_file("gobbeldygook"))
            
    
    def test_count_species(self):
        result = self.catalogue.count_species()
        self.assertEqual(
            result, {'Esox lucius': 1, 'Macropus rufus': 1, 'Bos taurus': 1, 'Phocidae': 3, 'Ovis/Capra': 1, 'Anatidae': 1, 'Laridae': 2})
    def test_count_nisp_and_weight_by_class(self):
        result = self.catalogue.count_nisp_and_weight_by_class()
        self.assertEqual(
            result, {'Mammalia': [129, 48.24], 'Indet': [64, 4.41], 'Aves': [8, 0.74], 'Teleostei': [4, 0.12]})

    def test_give_species(self):
        species = "Phocidae"
        result = self.catalogue.give_species(species)
        self.assertEqual(
            result, "Phocidae specimens: 3, identified bones: [('scapula', 446), ('costa', 917), ('costa', 917)]")

    def test_count_juveniles_by_species(self):
        result = self.catalogue.count_juveniles_by_species()
        self.assertEqual(
            result, {'Macropus rufus': [1, 0, 0], 'Indet': [7, 2, 1]})

    def test_give_species_breakdown_for_class(self):
        classis = "Mammalia"
        result = self.catalogue.give_species_breakdown_for_class(classis)
        self.assertEqual(
            result, {'Indet': 123, 'Macropus rufus': 1, 'Bos taurus': 1, 'Phocidae': 3, 'Ovis/Capra': 1})

    def test_all_burned_and_not(self):
        result = self.catalogue.all_burned_and_not()
        self.assertEqual(
            result,"ALL: 205, 53.51, NOT BURNED: 162, 44.86")
