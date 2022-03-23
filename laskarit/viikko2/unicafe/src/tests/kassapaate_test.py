import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassapaate = Kassapaate(100000)

    def test_toimii_alussa(self):
        self.assertEqual(str(self.kassapaate), "100000")
        self.assertEqual(str(self.edulliset), "0")
        self.assertEqual(str(self.maukkaat), "0")

    def test_kateinen_toimii(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.kassapaate.syo_maukkaasti_kateisella(420)
        self.assertEqual(str(self.kassapaate), "100640")
        self.assertEqual(str(self.kassapaate.syo_edullisesti_kateisella(250)), "10")
        self.assertEqual(str(self.kassapaate.syo_maukkaasti_kateisella(420)), "20")
        self.assertEqual(str(self.edulliset), "1")
        self.assertEqual(str(self.maukkaat), "1")

    def test_liian_vahan_kateista(self):
        self.kassapaate.syo_edullisesti_kateisella(230)
        self.kassapaate.syo_maukkaasti_kateisella(390)
        self.assertEqual(str(self.kassapaate), "100000")
        self.assertEqual(str(self.kassapaate.syo_edullisesti_kateisella(230)), "230")
        self.assertEqual(str(self.kassapaate.syo_maukkaasti_kateisella(390)), "390")
        self.assertEqual(str(self.edulliset), "0")
        self.assertEqual(str(self.maukkaat), "0")

    def test_pankkikortti_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(240)
        self.assertEqual(str(self.kassapaate.syo_edullisesti_kortilla(240)), "True")
        self.assertEqual(str(self.edulliset), "1")

    def test_pankkikortti_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(400)
        self.assertEqual(str(self.kassapaate.syo_maukkaasti_kortilla(400)), "True")
        self.assertEqual(str(self.maukkaat), "1")

    def test_pankkikortti_edullinen_ei_massia(self):
        self.kassapaate.syo_edullisesti_kortilla(230)
        self.assertEqual(str(self.kassapaate.syo_edullisesti_kortilla(240)), "False")
        self.assertEqual(str(self.edulliset), "0")

    def test_pankkikortti_maukas_ei_massia(self):
        self.kassapaate.syo_maukkaasti_kortilla(390)
        self.assertEqual(str(self.kassapaate.syo_maukkaasti_kortilla(400)), "False")
        self.assertEqual(str(self.maukkaat), "0")
