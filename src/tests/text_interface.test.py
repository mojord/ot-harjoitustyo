import unittest
from textinterface import *
from bonecatalogue import *


class Bonecaalogue(unittest.TestCase):
    def setUp(self):
        self.testdata = open("testaus.csv")Textinterface.read_file()
	self.catalogue = Bonecatalogue()
	

    def give_species_toimii_oikein(self):
	species = "Bos taurus"
	tulos = self.catalogue.give_species(species)
	self.assertEqual(tulos, "Bos taurus specimens: 1, identified bones: [('femur', '1')]")
	
	 

