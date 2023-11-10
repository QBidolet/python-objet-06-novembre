import unittest
from addition import addition
class TestAddition(unittest.TestCase):
    def test_addition(self):
        """
        Test de la fonction addition avec deux nombres simples.
        """
        resultat = addition(1, 2)
        self.assertEqual(3, resultat)

    def test_addition_negative(self):
        """
        Test de la fonction addition avec des nombres négatifs.
        """
        self.assertEquals(0, addition(-1, 1))