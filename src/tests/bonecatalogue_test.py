import unittest
import os
from services.bonecatalogue import Bonecatalogue
TESTDATA = os.path.join(os.path.dirname(__file__), "barts2.csv")


class TestBonecatalogue(unittest.TestCase):
    def setUp(self):
        self.catalogue = Bonecatalogue()
        self.catalogue.read_file(TESTDATA)

    def test_give_species_toimii_oikein(self):
        species = "Phocidae"
        tulos = self.catalogue.give_species(species)
        self.assertEqual(
            tulos, "Phocidae specimens: 3, identified bones: [('scapula', 446), ('costa', 917), ('costa', 917)]")

    def test_count_juveniles_by_species_toimii_oikein(self):
        tulos = self.catalogue.count_juveniles_by_species()
        self.assertEqual(
            tulos, {'Macropus rufus': [1, 0, 0], 'Indet': [7, 2, 1]})

    def test_give_species_breakdown_for_class_toimii_oikein(self):
        classis = "Mammalia"
        tulos = self.catalogue.give_species_breakdown_for_class(classis)
        self.assertEqual(
            tulos, {'Indet': 123, 'Macropus rufus': 1, 'Bos taurus': 1, 'Phocidae': 3, 'Ovis/Capra': 1})

    def test_all_burned_and_not_toimii_oikein(self):
        tulos = self.catalogue.all_burned_and_not()
        self.assertEqual(
            tulos,"ALL: 205, 53.51, NOT BURNED: 162, 44.86")
