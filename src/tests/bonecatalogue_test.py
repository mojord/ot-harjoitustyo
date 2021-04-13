
import unittest
import os
from bonecatalogue import Bonecatalogue
TESTDATA = os.path.join(os.path.dirname(__file__), "testaus.csv")

class TestBonecatalogue(unittest.TestCase):
    def setUp(self):
        self.catalogue = Bonecatalogue()
        self.testdata = self.catalogue.read_file(TESTDATA)
	

    def give_species_toimii_oikein(self):
        species = "Bos taurus"
        tulos = self.catalogue.give_species(species)
        self.assertEqual(tulos, "Bos taurus specimens: 1, identified bones: [('femur', '1')]")
	
	 

