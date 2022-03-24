import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(500)

    def test_toimii_alussa(self):
        self.assertEqual((self.kassapaate.kassassa_rahaa), 100000)
        self.assertEqual((self.kassapaate.edulliset + self.kassapaate.maukkaat), 0)

    def test_rahan_maara_kateinen_toimii_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateinen_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250), 10)

    def test_edullinen_ei_massia_vaihtoraha(self):
        self.assertEqual((self.kassapaate.syo_edullisesti_kateisella(230)), 230)

    def test_edullinen_ei_massia_loput(self):
        self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual((self.kassapaate.edulliset), 0)
        self.assertEqual((self.kassapaate.kassassa_rahaa), 100000)


    def test_rahan_maara_kateinen_toimii_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(420)
        self.assertEqual((self.kassapaate.kassassa_rahaa), 100400)
        self.assertEqual((self.kassapaate.maukkaat), 1)

    def test_kateinen_vaihtoraha_maukas(self):
        self.assertEqual((self.kassapaate.syo_maukkaasti_kateisella(420)), 20)

    def test_liian_vahan_kateista_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(390)
        self.assertEqual((self.kassapaate.kassassa_rahaa), 100000)
        self.assertEqual((self.kassapaate.maukkaat), 0)

    def test_liian_vahan_massia_maukas_vaihtoraha(self):
        self.assertEqual((self.kassapaate.syo_maukkaasti_kateisella(390)), 390)

    def test_pankkikortti_maukas_True(self):
        self.assertEqual((self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)), True)

    def test_pankkikortti_edullinen_True(self):
        self.assertEqual((self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)), True)

    def test_pankkikortti_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual((self.kassapaate.edulliset), 1)
        self.assertEqual((self.maksukortti.saldo), 260)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_pankkikortti_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual((self.kassapaate.maukkaat), 1)
        self.assertEqual((self.maksukortti.saldo), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortti_ei_massia_False(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual((self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)), False)

    def test_kortti_ei_massia_False_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual((self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)), False)

    def test_pankkikortti_edullinen_ei_massia(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual((self.kassapaate.edulliset), 2)
        self.assertEqual((self.maksukortti.saldo), 20)

    def test_pankkikortti_maukas_ei_massia(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual((self.kassapaate.maukkaat), 1)
        self.assertEqual((self.maksukortti.saldo), 100)

    def test_kortille_ladattaessa_saldo_muutttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
        self.assertEqual(self.maksukortti.saldo, 600)

    def test_negatiivinen_lataus(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.maksukortti.saldo, 500)
