"""
Niveau 3 - Tests Unitaires Avancés
À compléter par les étudiants
"""
import unittest


class TestTrierEtFiltrer(unittest.TestCase):
    """Tests pour la fonction trier_et_filtrer"""

    def setUp(self):
        from niveau_3_avance.fonctions import trier_et_filtrer
        self.trier_et_filtrer = trier_et_filtrer

    def test_trier_et_filtrer_simple_15_points(self):
        """TODO: Testez que [3, 1, 4, 1, 5] avec seuil 3 retourne [3, 4, 5]"""
        pass

    def test_trier_et_filtrer_none_15_points(self):
        """TODO: Testez que None retourne une liste vide"""
        pass

    def test_trier_et_filtrer_seuil_invalide_15_points(self):
        """TODO: Testez que seuil non-numérique lève une TypeError"""
        pass

    def test_trier_et_filtrer_aucun_match_15_points(self):
        """TODO: Testez quand aucun nombre ne dépasse le seuil"""
        pass

    def test_trier_et_filtrer_tous_match_15_points(self):
        """TODO: Testez quand tous les nombres dépassent le seuil"""
        pass

    def test_trier_et_filtrer_negatifs_15_points(self):
        """TODO: Testez avec des nombres négatifs"""
        pass

    def test_trier_et_filtrer_doublons_15_points(self):
        """TODO: Testez avec des doublons"""
        pass


class TestFusionnerDictionnaires(unittest.TestCase):
    """Tests pour la fonction fusionner_dictionnaires"""

    def setUp(self):
        from niveau_3_avance.fonctions import fusionner_dictionnaires
        self.fusionner_dictionnaires = fusionner_dictionnaires

    def test_fusionner_simple_15_points(self):
        """TODO: Testez que {'a': 1} et {'b': 2} retourne {'a': 1, 'b': 2}"""
        pass

    def test_fusionner_cles_communes_15_points(self):
        """TODO: Testez que dict2 prend le dessus en cas de clé commune"""
        pass

    def test_fusionner_none_none_15_points(self):
        """TODO: Testez que None et None retourne {}"""
        pass

    def test_fusionner_dict_vide_15_points(self):
        """TODO: Testez la fusion avec un dictionnaire vide"""
        pass

    def test_fusionner_type_invalide_15_points(self):
        """TODO: Testez que passer une liste lève une TypeError"""
        pass

    def test_fusionner_valeurs_complexes_15_points(self):
        """TODO: Testez avec des valeurs complexes (listes, dicts)"""
        pass

    def test_fusionner_ne_modifie_pas_original_15_points(self):
        """TODO: Testez que les dictionnaires originaux ne sont pas modifiés"""
        pass


class TestCompterOccurrences(unittest.TestCase):
    """Tests pour la fonction compter_occurrences"""

    def setUp(self):
        from niveau_3_avance.fonctions import compter_occurrences
        self.compter_occurrences = compter_occurrences

    def test_compter_simple_15_points(self):
        """TODO: Testez que 'hello' contient 2 'l'"""
        pass

    def test_compter_aucune_occurrence_15_points(self):
        """TODO: Testez un caractère absent"""
        pass

    def test_compter_texte_vide_15_points(self):
        """TODO: Testez avec un texte vide"""
        pass

    def test_compter_texte_none_15_points(self):
        """TODO: Testez que None retourne 0"""
        pass

    def test_compter_caractere_none_15_points(self):
        """TODO: Testez que caractère None retourne 0"""
        pass

    def test_compter_sensible_casse_15_points(self):
        """TODO: Testez que 'a' et 'A' sont différents"""
        pass

    def test_compter_caractere_special_15_points(self):
        """TODO: Testez avec des caractères spéciaux"""
        pass


class TestExtraireNombres(unittest.TestCase):
    """Tests pour la fonction extraire_nombres"""

    def setUp(self):
        from niveau_3_avance.fonctions import extraire_nombres
        self.extraire_nombres = extraire_nombres

    def test_extraire_simple_15_points(self):
        """TODO: Testez que 'abc123def456' retourne [123, 456]"""
        pass

    def test_extraire_aucun_nombre_15_points(self):
        """TODO: Testez une chaîne sans nombres"""
        pass

    def test_extraire_texte_vide_15_points(self):
        """TODO: Testez une chaîne vide"""
        pass

    def test_extraire_texte_none_15_points(self):
        """TODO: Testez que None retourne une liste vide"""
        pass

    def test_extraire_nombres_negatifs_15_points(self):
        """TODO: Testez l'extraction de nombres négatifs"""
        pass

    def test_extraire_nombres_consecutifs_15_points(self):
        """TODO: Testez 'a123b456c' retourne [123, 456]"""
        pass

    def test_extraire_nombres_avec_zeros_15_points(self):
        """TODO: Testez l'extraction avec des zéros"""
        pass


class TestValiderMotDePasse(unittest.TestCase):
    """Tests pour la fonction valider_mot_de_passe"""

    def setUp(self):
        from niveau_3_avance.fonctions import valider_mot_de_passe
        self.valider_mot_de_passe = valider_mot_de_passe

    def test_mdp_valide_15_points(self):
        """TODO: Testez un mot de passe valide 'Abc123def'"""
        pass

    def test_mdp_trop_court_15_points(self):
        """TODO: Testez un mot de passe < 8 caractères"""
        pass

    def test_mdp_pas_majuscule_15_points(self):
        """TODO: Testez un mot de passe sans majuscule"""
        pass

    def test_mdp_pas_minuscule_15_points(self):
        """TODO: Testez un mot de passe sans minuscule"""
        pass

    def test_mdp_pas_chiffre_15_points(self):
        """TODO: Testez un mot de passe sans chiffre"""
        pass

    def test_mdp_type_invalide_15_points(self):
        """TODO: Testez que passer un entier lève une TypeError"""
        pass

    def test_mdp_none_15_points(self):
        """TODO: Testez que None lève une TypeError"""
        pass


class TestCalculerStatistiques(unittest.TestCase):
    """Tests pour la fonction calculer_statistiques"""

    def setUp(self):
        from niveau_3_avance.fonctions import calculer_statistiques
        self.calculer_statistiques = calculer_statistiques

    def test_statistiques_simple_15_points(self):
        """TODO: Testez [1, 2, 3, 4, 5] retourne les bonnes stats"""
        pass

    def test_statistiques_liste_vide_15_points(self):
        """TODO: Testez qu'une liste vide lève une ValueError"""
        pass

    def test_statistiques_none_15_points(self):
        """TODO: Testez que None retourne None"""
        pass

    def test_statistiques_un_element_15_points(self):
        """TODO: Testez [5] retourne min=5, max=5, moyenne=5, mediane=5"""
        pass

    def test_statistiques_negatifs_15_points(self):
        """TODO: Testez avec des nombres négatifs"""
        pass

    def test_statistiques_mediane_pair_15_points(self):
        """TODO: Testez la médiane avec un nombre pair d'éléments"""
        pass

    def test_statistiques_mediane_impair_15_points(self):
        """TODO: Testez la médiane avec un nombre impair d'éléments"""
        pass


if __name__ == '__main__':
    unittest.main()
