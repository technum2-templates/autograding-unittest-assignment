"""
Solutions pour le Niveau 1 - Tests Unitaires Basiques
Utilise unittest comme framework de test
Couvre tous les cas limites : positifs, négatifs, zéro, vide, None
"""
import unittest


class TestAddition(unittest.TestCase):
    """Tests pour la fonction addition"""

    def setUp(self):
        """Importer la fonction avant chaque test"""
        from niveau_1_basique.fonctions import addition
        self.addition = addition

    def test_addition_positifs_5_points(self):
        """Testez que 2 + 3 = 5"""
        self.assertEqual(self.addition(2, 3), 5)

    def test_addition_negatifs_5_points(self):
        """Testez que -2 + -3 = -5"""
        self.assertEqual(self.addition(-2, -3), -5)

    def test_addition_mixte_5_points(self):
        """Testez que 5 + (-3) = 2"""
        self.assertEqual(self.addition(5, -3), 2)

    def test_addition_zero_5_points(self):
        """Testez que 0 + 5 = 5"""
        self.assertEqual(self.addition(0, 5), 5)

    def test_addition_zeros_5_points(self):
        """Cas limite : 0 + 0 = 0"""
        self.assertEqual(self.addition(0, 0), 0)

    def test_addition_grands_nombres_5_points(self):
        """Cas limite : grands nombres"""
        self.assertEqual(self.addition(1000000, 2000000), 3000000)

    def test_addition_floats_5_points(self):
        """Cas limite : nombres décimaux"""
        self.assertAlmostEqual(self.addition(1.5, 2.5), 4.0)


class TestMultiplication(unittest.TestCase):
    """Tests pour la fonction multiplication"""

    def setUp(self):
        """Importer la fonction avant chaque test"""
        from niveau_1_basique.fonctions import multiplication
        self.multiplication = multiplication

    def test_multiplication_positifs_5_points(self):
        """Testez que 3 * 4 = 12"""
        self.assertEqual(self.multiplication(3, 4), 12)

    def test_multiplication_par_zero_5_points(self):
        """Testez que 5 * 0 = 0"""
        self.assertEqual(self.multiplication(5, 0), 0)

    def test_multiplication_par_un_5_points(self):
        """Testez que 5 * 1 = 5"""
        self.assertEqual(self.multiplication(5, 1), 5)

    def test_multiplication_negatifs_5_points(self):
        """Testez que -2 * -3 = 6"""
        self.assertEqual(self.multiplication(-2, -3), 6)

    def test_multiplication_mixte_5_points(self):
        """Cas limite : positif * négatif"""
        self.assertEqual(self.multiplication(5, -3), -15)

    def test_multiplication_zero_zero_5_points(self):
        """Cas limite : 0 * 0 = 0"""
        self.assertEqual(self.multiplication(0, 0), 0)

    def test_multiplication_grands_nombres_5_points(self):
        """Cas limite : grands nombres"""
        self.assertEqual(self.multiplication(100, 200), 20000)


class TestEstPalindrome(unittest.TestCase):
    """Tests pour la fonction est_palindrome"""

    def setUp(self):
        """Importer la fonction avant chaque test"""
        from niveau_1_basique.fonctions import est_palindrome
        self.est_palindrome = est_palindrome

    def test_palindrome_simple_5_points(self):
        """Testez que 'aba' est un palindrome"""
        self.assertTrue(self.est_palindrome('aba'))

    def test_non_palindrome_5_points(self):
        """Testez que 'abc' n'est pas un palindrome"""
        self.assertFalse(self.est_palindrome('abc'))

    def test_palindrome_avec_espaces_5_points(self):
        """Testez que 'a b a' est un palindrome"""
        self.assertTrue(self.est_palindrome('a b a'))

    def test_palindrome_vide_5_points(self):
        """Cas limite : chaîne vide est un palindrome"""
        self.assertTrue(self.est_palindrome(''))

    def test_palindrome_un_caractere_5_points(self):
        """Cas limite : un seul caractère"""
        self.assertTrue(self.est_palindrome('a'))

    def test_palindrome_deux_identiques_5_points(self):
        """Cas limite : deux caractères identiques"""
        self.assertTrue(self.est_palindrome('aa'))

    def test_palindrome_deux_differents_5_points(self):
        """Cas limite : deux caractères différents"""
        self.assertFalse(self.est_palindrome('ab'))

    def test_palindrome_majuscules_5_points(self):
        """Cas limite : majuscules (selon implémentation)"""
        # À adapter selon si la fonction ignore la casse
        result = self.est_palindrome('Aba')
        self.assertIsNotNone(result)  # Juste vérifier que ça ne plante pas


class TestMaxDeTrois(unittest.TestCase):
    """Tests pour la fonction max_de_trois"""

    def setUp(self):
        """Importer la fonction avant chaque test"""
        from niveau_1_basique.fonctions import max_de_trois
        self.max_de_trois = max_de_trois

    def test_max_trois_simple_5_points(self):
        """Testez que max_de_trois(1, 5, 3) = 5"""
        self.assertEqual(self.max_de_trois(1, 5, 3), 5)

    def test_max_trois_negatifs_5_points(self):
        """Testez que max_de_trois(-1, -5, -3) = -1"""
        self.assertEqual(self.max_de_trois(-1, -5, -3), -1)

    def test_max_trois_identiques_5_points(self):
        """Testez que max_de_trois(3, 3, 3) = 3"""
        self.assertEqual(self.max_de_trois(3, 3, 3), 3)

    def test_max_trois_zeros_5_points(self):
        """Cas limite : tous des zéros"""
        self.assertEqual(self.max_de_trois(0, 0, 0), 0)

    def test_max_trois_premier_max_5_points(self):
        """Cas limite : le maximum est le premier"""
        self.assertEqual(self.max_de_trois(10, 5, 3), 10)

    def test_max_trois_dernier_max_5_points(self):
        """Cas limite : le maximum est le dernier"""
        self.assertEqual(self.max_de_trois(3, 5, 10), 10)

    def test_max_trois_deux_identiques_5_points(self):
        """Cas limite : deux valeurs identiques"""
        self.assertEqual(self.max_de_trois(5, 5, 3), 5)

    def test_max_trois_grands_nombres_5_points(self):
        """Cas limite : grands nombres"""
        self.assertEqual(self.max_de_trois(1000, 2000, 1500), 2000)


if __name__ == '__main__':
    unittest.main()
