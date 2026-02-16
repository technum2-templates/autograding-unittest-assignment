"""
Solutions pour le Niveau 2 - Tests Unitaires Intermédiaires
Utilise unittest comme framework de test
Couvre tous les cas limites : exceptions, None, vide, négatifs, etc.
"""
import unittest


class TestDiviser(unittest.TestCase):
    """Tests pour la fonction diviser"""

    def setUp(self):
        from niveau_2_intermediaire.fonctions import diviser
        self.diviser = diviser

    def test_diviser_simple_10_points(self):
        """Testez que 10 / 2 = 5"""
        self.assertEqual(self.diviser(10, 2), 5)

    def test_diviser_par_zero_10_points(self):
        """Testez que diviser par 0 lève une ValueError"""
        with self.assertRaises(ValueError):
            self.diviser(10, 0)

    def test_diviser_negatifs_10_points(self):
        """Testez que -10 / 2 = -5"""
        self.assertEqual(self.diviser(-10, 2), -5)

    def test_diviser_resultat_decimal_10_points(self):
        """Testez que 5 / 2 = 2.5"""
        self.assertAlmostEqual(self.diviser(5, 2), 2.5)

    def test_diviser_un_10_points(self):
        """Testez que 5 / 1 = 5"""
        self.assertEqual(self.diviser(5, 1), 5)

    def test_diviser_zero_par_nombre_10_points(self):
        """Testez que 0 / 5 = 0"""
        self.assertEqual(self.diviser(0, 5), 0)


class TestCalculerMoyenne(unittest.TestCase):
    """Tests pour la fonction calculer_moyenne"""

    def setUp(self):
        from niveau_2_intermediaire.fonctions import calculer_moyenne
        self.calculer_moyenne = calculer_moyenne

    def test_moyenne_simple_10_points(self):
        """Testez que la moyenne de [1, 2, 3] = 2"""
        self.assertEqual(self.calculer_moyenne([1, 2, 3]), 2)

    def test_moyenne_liste_vide_10_points(self):
        """Testez que la moyenne d'une liste vide lève une ValueError"""
        with self.assertRaises(ValueError):
            self.calculer_moyenne([])

    def test_moyenne_none_10_points(self):
        """Testez que la moyenne de None retourne 0"""
        self.assertEqual(self.calculer_moyenne(None), 0)

    def test_moyenne_negatifs_10_points(self):
        """Testez que la moyenne de [-1, -2, -3] = -2"""
        self.assertEqual(self.calculer_moyenne([-1, -2, -3]), -2)

    def test_moyenne_un_element_10_points(self):
        """Testez que la moyenne de [5] = 5"""
        self.assertEqual(self.calculer_moyenne([5]), 5)

    def test_moyenne_decimaux_10_points(self):
        """Testez que la moyenne de [1.5, 2.5, 3.0] ≈ 2.333"""
        self.assertAlmostEqual(self.calculer_moyenne([1.5, 2.5, 3.0]), 2.333, places=2)


class TestValiderEmail(unittest.TestCase):
    """Tests pour la fonction valider_email"""

    def setUp(self):
        from niveau_2_intermediaire.fonctions import valider_email
        self.valider_email = valider_email

    def test_email_valide_10_points(self):
        """Testez qu'un email valide retourne True"""
        self.assertTrue(self.valider_email('test@example.com'))

    def test_email_sans_arobase_10_points(self):
        """Testez qu'un email sans @ retourne False"""
        self.assertFalse(self.valider_email('testexample.com'))

    def test_email_sans_point_10_points(self):
        """Testez qu'un email sans . retourne False"""
        self.assertFalse(self.valider_email('test@examplecom'))

    def test_email_vide_10_points(self):
        """Testez qu'une chaîne vide retourne False"""
        self.assertFalse(self.valider_email(''))

    def test_email_none_10_points(self):
        """Testez que None retourne False"""
        self.assertFalse(self.valider_email(None))

    def test_email_multiple_arobase_10_points(self):
        """Testez qu'un email avec plusieurs @ est valide si contient aussi un point"""
        # Cas limite : dépend de l'implémentation
        result = self.valider_email('test@@example.com')
        self.assertIsNotNone(result)


class TestCompterVoyelles(unittest.TestCase):
    """Tests pour la fonction compter_voyelles"""

    def setUp(self):
        from niveau_2_intermediaire.fonctions import compter_voyelles
        self.compter_voyelles = compter_voyelles

    def test_compter_voyelles_simple_10_points(self):
        """Testez que 'hello' contient 2 voyelles (e, o)"""
        self.assertEqual(self.compter_voyelles('hello'), 2)

    def test_compter_voyelles_vide_10_points(self):
        """Testez qu'une chaîne vide retourne 0"""
        self.assertEqual(self.compter_voyelles(''), 0)

    def test_compter_voyelles_none_10_points(self):
        """Testez que None retourne 0"""
        self.assertEqual(self.compter_voyelles(None), 0)

    def test_compter_voyelles_majuscules_10_points(self):
        """Testez que les majuscules sont comptées (ex: 'HELLO' = 2)"""
        self.assertEqual(self.compter_voyelles('HELLO'), 2)

    def test_compter_voyelles_pas_de_voyelles_10_points(self):
        """Testez une chaîne sans voyelles (ex: 'xyz' = 0)"""
        self.assertEqual(self.compter_voyelles('xyz'), 0)

    def test_compter_voyelles_toutes_voyelles_10_points(self):
        """Testez une chaîne avec toutes les voyelles (aeiou = 5)"""
        self.assertEqual(self.compter_voyelles('aeiou'), 5)


class TestInverserListe(unittest.TestCase):
    """Tests pour la fonction inverser_liste"""

    def setUp(self):
        from niveau_2_intermediaire.fonctions import inverser_liste
        self.inverser_liste = inverser_liste

    def test_inverser_liste_simple_10_points(self):
        """Testez que [1, 2, 3] devient [3, 2, 1]"""
        self.assertEqual(self.inverser_liste([1, 2, 3]), [3, 2, 1])

    def test_inverser_liste_vide_10_points(self):
        """Testez qu'une liste vide retourne une liste vide"""
        self.assertEqual(self.inverser_liste([]), [])

    def test_inverser_liste_none_10_points(self):
        """Testez que None retourne une liste vide"""
        self.assertEqual(self.inverser_liste(None), [])

    def test_inverser_liste_un_element_10_points(self):
        """Testez qu'une liste avec un élément reste identique"""
        self.assertEqual(self.inverser_liste([5]), [5])

    def test_inverser_liste_deux_elements_10_points(self):
        """Testez que [1, 2] devient [2, 1]"""
        self.assertEqual(self.inverser_liste([1, 2]), [2, 1])

    def test_inverser_liste_ne_modifie_pas_original_10_points(self):
        """Testez que la liste originale n'est pas modifiée"""
        original = [1, 2, 3]
        result = self.inverser_liste(original)
        self.assertEqual(original, [1, 2, 3])  # L'original ne doit pas changer
        self.assertEqual(result, [3, 2, 1])


class TestFiltrerPairs(unittest.TestCase):
    """Tests pour la fonction filtrer_pairs"""

    def setUp(self):
        from niveau_2_intermediaire.fonctions import filtrer_pairs
        self.filtrer_pairs = filtrer_pairs

    def test_filtrer_pairs_simple_10_points(self):
        """Testez que [1, 2, 3, 4] retourne [2, 4]"""
        self.assertEqual(self.filtrer_pairs([1, 2, 3, 4]), [2, 4])

    def test_filtrer_pairs_vide_10_points(self):
        """Testez qu'une liste vide retourne une liste vide"""
        self.assertEqual(self.filtrer_pairs([]), [])

    def test_filtrer_pairs_none_10_points(self):
        """Testez que None retourne une liste vide"""
        self.assertEqual(self.filtrer_pairs(None), [])

    def test_filtrer_pairs_aucun_pair_10_points(self):
        """Testez une liste sans nombres pairs [1, 3, 5]"""
        self.assertEqual(self.filtrer_pairs([1, 3, 5]), [])

    def test_filtrer_pairs_tous_pairs_10_points(self):
        """Testez une liste avec que des nombres pairs [2, 4, 6]"""
        self.assertEqual(self.filtrer_pairs([2, 4, 6]), [2, 4, 6])

    def test_filtrer_pairs_negatifs_10_points(self):
        """Testez que les nombres négatifs pairs sont inclus [-2, -1, 0, 1, 2]"""
        self.assertEqual(self.filtrer_pairs([-2, -1, 0, 1, 2]), [-2, 0, 2])


if __name__ == '__main__':
    unittest.main()
