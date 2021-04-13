import unittest
from textinterface import *


class TestBoneatorTextinterface(unittest.TestCase):
    def setUp(self):
        self.testdata = open("testaus.csv").read_file()

    def count_nisp_by_class_toimii_oikein(self):
	 

