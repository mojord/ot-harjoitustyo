import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10")
    
    def test_rahan_lataaminen_toimii_oikein(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 20")
    
    def test_rahaa_vahenee_oikea_maara(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 5")    

    def test_saldo_ei_muutu_jos_raha_ei_riita(self):
        self.maksukortti.ota_rahaa(15)
        self.assertEqual(str(self.maksukortti), "saldo: 10")

    def test_ota_rahaa_palauttaa_true_kun_raha_riittaa(self):
        self.maksukortti.ota_rahaa(5)
        self.assertTrue(self.maksukortti.ota_rahaa)
    
    def test_ota_rahaa_palauttaa_false_kun_raha_ei_riita(self):
        self.maksukortti.ota_rahaa(15)
        self.assertFalse(self.maksukortti.ota_rahaa)
