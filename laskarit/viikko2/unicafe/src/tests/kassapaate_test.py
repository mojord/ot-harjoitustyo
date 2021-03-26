import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
        self.koyhankortti = Maksukortti(10)
    
    def test_alkukassa_oikein(self):
        alkupaate = Kassapaate()
        self.assertEqual(alkupaate.kassassa_rahaa, 1000)
    def test_alkumyynti_on_nolla(self):
        alkumyyntipaate = Kassapaate()
        self.assertEqual(alkumyyntipaate.edulliset, 0)
        self.assertEqual(alkumyyntipaate.maukkaat, 0)
    
    def test_kateisosto_raha_riittaa_edullinen(self):
        rahaa = self.kassapaate.kassassa_rahaa

        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, rahaa + 240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, rahaa + 480)
        self.assertEqual(self.kassapaate.edulliset, 2)
    
    def test_kateisosto_raha_ei_riita_edullinen(self):
        rahaa = self.kassapaate.kassassa_rahaa
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, rahaa)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_kateisosto_raha_riittaa_maukas(self):
        rahaa = self.kassapaate.kassassa_rahaa

        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, rahaa + 400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, rahaa + 800)
        self.assertEqual(self.kassapaate.maukkaat, 2)
    
    def test_kateisosto_raha_ei_riita_maukas(self):
        rahaa = self.kassapaate.kassassa_rahaa
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, rahaa)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_korttiosto_saldo_riittaa_edullinen(self):
        rahaa = self.kassapaate.kassassa_rahaa
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 760")
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, rahaa)
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))
    def test_korttiosto_saldo_ei_riita_edullinen(self):
        rahaa = self.kassapaate.kassassa_rahaa
        self.kassapaate.syo_edullisesti_kortilla(self.koyhankortti)
        self.assertEqual(str(self.koyhankortti), "saldo: 10")
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, rahaa)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.koyhankortti))
    
    def test_korttiosto_saldo_riittaa_maukas(self):
        rahaa = self.kassapaate.kassassa_rahaa
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 600")
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, rahaa)
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))
    def test_korttiosto_saldo_ei_riita_maukas(self):
        rahaa = self.kassapaate.kassassa_rahaa
        self.kassapaate.syo_maukkaasti_kortilla(self.koyhankortti)
        self.assertEqual(str(self.koyhankortti), "saldo: 10")
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, rahaa)
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(self.koyhankortti))
    

    def test_lataa_rahaa_kasvattaa_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(str(self.maksukortti), "saldo: 1100")
    def test_lataa_rahaa_kasvattaa_kassaa(self):
        rahaa = self.kassapaate.kassassa_rahaa
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, rahaa + 100)
    def test_lataa_rahaa_summa_ei_saa_olla_negatiivinen(self):
        rahaa = self.kassapaate.kassassa_rahaa
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, rahaa)





    
