
import unittest
import os
from bonecatalogue import Bonecatalogue
TESTDATA = os.path.join(os.path.dirname(__file__), "testaus.csv")


class TestBonecatalogue(unittest.TestCase):
    def setUp(self):
        self.catalogue = Bonecatalogue()
#        self.testdata = self.catalogue.read_file(TESTDATA)

    def test_give_species_toimii_oikein(self):
        self.catalogue.read_file(TESTDATA)
        species = "Bos taurus"
        tulos = self.catalogue.give_species(species)
        self.assertEqual(
            tulos, "Bos taurus specimens: 1, identified bones: [('femur', '1')]")

    def test_kokeilu_toimii_oikein(self):
        koe = self.catalogue.kokeilu()
        self.assertEqual(koe, "buenos dias")

    def test_naughty_test(self):
        naughty = self.catalogue.kokeilu()
        self.assertEqual(naughty, "adios amigos")
