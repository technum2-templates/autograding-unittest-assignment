"""
Niveau 2 - Tests Unitaires Intermédiaires
À compléter par les étudiants
"""
import unittest


class TestDiviser(unittest.TestCase):
    """Tests pour la fonction diviser"""

    def setUp(self):
        from niveau_2_intermediaire.fonctions import diviser
        self.diviser = diviser

    def test_diviser_simple_10_points(self):
        """TODO: Testez que 10 / 2 = 5"""
        pass

    def test_diviser_par_zero_10_points(self):
        """TODO: Testez que diviser par 0 lève une ValueError"""
        pass

    def test_diviser_negatifs_10_points(self):
        """TODO: Testez que -10 / 2 = -5"""
        pass

    def test_diviser_resultat_decimal_10_points(self):
        """TODO: Testez que 5 / 2 = 2.5"""
        pass

    def test_diviser_un_10_points(self):
        """TODO: Testez que 5 / 1 = 5"""
        pass

    def test_diviser_zero_par_nombre_10_points(self):
        """TODO: Testez que 0 / 5 = 0"""
        pass


class TestCalculerMoyenne(unittest.TestCase):
    """Tests pour la fonction calculer_moyenne"""

    def setUp(self):
        from niveau_2_intermediaire.fonctions import calculer_moyenne
        self.calculer_moyenne = calculer_moyenne

    def test_moyenne_simple_10_points(self):
        """TODO: Testez que la moyenne de [1, 2, 3] = 2"""
        pass

    def test_moyenne_liste_vide_10_points(self):
        """TODO: Testez que la moyenne d'une liste vide lève une ValueError"""
        pass

    def test_moyenne_none_10_points(self):
        """TODO: Testez que la moyenne de None retourne 0"""
        pass

    def test_moyenne_negatifs_10_points(self):
        """TODO: Testez que la moyenne de [-1, -2, -3] = -2"""
        pass

    def test_moyenne_un_element_10_points(self):
        """TODO: Testez que la moyenne de [5] = 5"""
        pass

    def test_moyenne_decimaux_10_points(self):
        """TODO: Testez que la moyenne de [1.5, 2.5, 3.0] = 2.333..."""
        pass


class TestValiderEmail(unittest.TestCase):
    """Tests pour la fonction valider_email"""

    def setUp(self):
        from niveau_2_intermediaire.fonctions import valider_email
        self.valider_email = valider_email

    def test_email_valide_10_points(self):
        """TODO: Testez qu'un email valide retourne True"""
        pass

    def test_email_sans_arobase_10_points(self):
        """TODO: Testez qu'un email sans @ retourne False"""
        pass

    def test_email_sans_point_10_points(self):
        """TODO: Testez qu'un email sans . retourne False"""
        pass

    def test_email_vide_10_points(self):
        """TODO: Testez qu'une chaîne vide retourne False"""
        pass

    def test_email_none_10_points(self):
        """TODO: Testez que None retourne False"""
        pass

    def test_email_multiple_arobase_10_points(self):
        """TODO: Testez qu'un email avec plusieurs @ retourne True ou False selon implémentation"""
        pass


class TestCompterVoyelles(unittest.TestCase):
    """Tests pour la fonction compter_voyelles"""

    def setUp(self):
        from niveau_2_intermediaire.fonctions import compter_voyelles
        self.compter_voyelles = compter_voyelles

    def test_compter_voyelles_simple_10_points(self):
        """TODO: Testez que 'hello' contient 2 voyelles"""
        pass

    def test_compter_voyelles_vide_10_points(self):
        """TODO: Testez qu'une chaîne vide retourne 0"""
        pass

    def test_compter_voyelles_none_10_points(self):
        """TODO: Testez que None retourne 0"""
        pass

    def test_compter_voyelles_majuscules_10_points(self):
        """TODO: Testez que les majuscules sont comptées (ex: 'HELLO')"""
        pass

    def test_compter_voyelles_pas_de_voyelles_10_points(self):
        """TODO: Testez une chaîne sans voyelles (ex: 'xyz')"""
        pass

    def test_compter_voyelles_toutes_voyelles_10_points(self):
        """TODO: Testez une chaîne avec toutes les voyelles"""
        pass


class TestInverserListe(unittest.TestCase):
    """Tests pour la fonction inverser_liste"""

    def setUp(self):
        from niveau_2_intermediaire.fonctions import inverser_liste
        self.inverser_liste = inverser_liste

    def test_inverser_liste_simple_10_points(self):
        """TODO: Testez que [1, 2, 3] devient [3, 2, 1]"""
        pass

    def test_inverser_liste_vide_10_points(self):
        """TODO: Testez qu'une liste vide retourne une liste vide"""
        pass

    def test_inverser_liste_none_10_points(self):
        """TODO: Testez que None retourne une liste vide"""
        pass

    def test_inverser_liste_un_element_10_points(self):
        """TODO: Testez qu'une liste avec un élément reste identique"""
        pass

    def test_inverser_liste_deux_elements_10_points(self):
        """TODO: Testez que [1, 2] devient [2, 1]"""
        pass

    def test_inverser_liste_ne_modifie_pas_original_10_points(self):
        """TODO: Testez que la liste originale n'est pas modifiée"""
        pass


class TestFiltrerPairs(unittest.TestCase):
    """Tests pour la fonction filtrer_pairs"""

    def setUp(self):
        from niveau_2_intermediaire.fonctions import filtrer_pairs
        self.filtrer_pairs = filtrer_pairs

    def test_filtrer_pairs_simple_10_points(self):
        """TODO: Testez que [1, 2, 3, 4] retourne [2, 4]"""
        pass

    def test_filtrer_pairs_vide_10_points(self):
        """TODO: Testez qu'une liste vide retourne une liste vide"""
        pass

    def test_filtrer_pairs_none_10_points(self):
        """TODO: Testez que None retourne une liste vide"""
        pass

    def test_filtrer_pairs_aucun_pair_10_points(self):
        """TODO: Testez une liste sans nombres pairs"""
        pass

    def test_filtrer_pairs_tous_pairs_10_points(self):
        """TODO: Testez une liste avec que des nombres pairs"""
        pass

    def test_filtrer_pairs_negatifs_10_points(self):
        """TODO: Testez que les nombres négatifs pairs sont inclus"""
        pass


if __name__ == '__main__':
    unittest.main()
