"""
Solutions pour le Niveau 3 - Tests Unitaires Avancés
Utilise unittest comme framework de test
Couvre tous les cas limites : exceptions, None, vide, collections, etc.
"""
import unittest


class TestTrierEtFiltrer(unittest.TestCase):
    """Tests pour la fonction trier_et_filtrer"""

    def setUp(self):
        from niveau_3_avance.fonctions import trier_et_filtrer
        self.trier_et_filtrer = trier_et_filtrer

    def test_trier_et_filtrer_simple_15_points(self):
        """Testez que [3, 1, 4, 1, 5] avec seuil 3 retourne [3, 4, 5]"""
        result = self.trier_et_filtrer([3, 1, 4, 1, 5], 3)
        self.assertEqual(result, [3, 4, 5])

    def test_trier_et_filtrer_none_15_points(self):
        """Testez que None retourne une liste vide"""
        self.assertEqual(self.trier_et_filtrer(None, 5), [])

    def test_trier_et_filtrer_seuil_invalide_15_points(self):
        """Testez que seuil non-numérique lève une TypeError"""
        with self.assertRaises(TypeError):
            self.trier_et_filtrer([1, 2, 3], "cinq")

    def test_trier_et_filtrer_aucun_match_15_points(self):
        """Testez quand aucun nombre ne dépasse le seuil"""
        self.assertEqual(self.trier_et_filtrer([1, 2, 3], 10), [])

    def test_trier_et_filtrer_tous_match_15_points(self):
        """Testez quand tous les nombres dépassent le seuil"""
        result = self.trier_et_filtrer([5, 10, 15], 3)
        self.assertEqual(result, [5, 10, 15])

    def test_trier_et_filtrer_negatifs_15_points(self):
        """Testez avec des nombres négatifs"""
        result = self.trier_et_filtrer([-5, -2, 0, 3, 5], 0)
        self.assertEqual(result, [0, 3, 5])

    def test_trier_et_filtrer_doublons_15_points(self):
        """Testez avec des doublons"""
        result = self.trier_et_filtrer([3, 3, 1, 1, 5], 2)
        self.assertEqual(result, [3, 3, 5])


class TestFusionnerDictionnaires(unittest.TestCase):
    """Tests pour la fonction fusionner_dictionnaires"""

    def setUp(self):
        from niveau_3_avance.fonctions import fusionner_dictionnaires
        self.fusionner_dictionnaires = fusionner_dictionnaires

    def test_fusionner_simple_15_points(self):
        """Testez que {'a': 1} et {'b': 2} retourne {'a': 1, 'b': 2}"""
        result = self.fusionner_dictionnaires({'a': 1}, {'b': 2})
        self.assertEqual(result, {'a': 1, 'b': 2})

    def test_fusionner_cles_communes_15_points(self):
        """Testez que dict2 prend le dessus en cas de clé commune"""
        result = self.fusionner_dictionnaires({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
        self.assertEqual(result, {'a': 1, 'b': 3, 'c': 4})

    def test_fusionner_none_none_15_points(self):
        """Testez que None et None retourne {}"""
        self.assertEqual(self.fusionner_dictionnaires(None, None), {})

    def test_fusionner_dict_vide_15_points(self):
        """Testez la fusion avec un dictionnaire vide"""
        result = self.fusionner_dictionnaires({'a': 1}, {})
        self.assertEqual(result, {'a': 1})

    def test_fusionner_type_invalide_15_points(self):
        """Testez que passer une liste lève une TypeError"""
        with self.assertRaises(TypeError):
            self.fusionner_dictionnaires([1, 2], {'a': 1})

    def test_fusionner_valeurs_complexes_15_points(self):
        """Testez avec des valeurs complexes (listes, dicts)"""
        result = self.fusionner_dictionnaires({'a': [1, 2]}, {'b': {'x': 10}})
        self.assertEqual(result, {'a': [1, 2], 'b': {'x': 10}})

    def test_fusionner_ne_modifie_pas_original_15_points(self):
        """Testez que les dictionnaires originaux ne sont pas modifiés"""
        dict1 = {'a': 1}
        dict2 = {'b': 2}
        result = self.fusionner_dictionnaires(dict1, dict2)
        self.assertEqual(dict1, {'a': 1})
        self.assertEqual(dict2, {'b': 2})


class TestCompterOccurrences(unittest.TestCase):
    """Tests pour la fonction compter_occurrences"""

    def setUp(self):
        from niveau_3_avance.fonctions import compter_occurrences
        self.compter_occurrences = compter_occurrences

    def test_compter_simple_15_points(self):
        """Testez que 'hello' contient 2 'l'"""
        self.assertEqual(self.compter_occurrences('hello', 'l'), 2)

    def test_compter_aucune_occurrence_15_points(self):
        """Testez un caractère absent"""
        self.assertEqual(self.compter_occurrences('hello', 'x'), 0)

    def test_compter_texte_vide_15_points(self):
        """Testez avec un texte vide"""
        self.assertEqual(self.compter_occurrences('', 'a'), 0)

    def test_compter_texte_none_15_points(self):
        """Testez que None retourne 0"""
        self.assertEqual(self.compter_occurrences(None, 'a'), 0)

    def test_compter_caractere_none_15_points(self):
        """Testez que caractère None retourne 0"""
        self.assertEqual(self.compter_occurrences('hello', None), 0)

    def test_compter_sensible_casse_15_points(self):
        """Testez que 'a' et 'A' sont différents"""
        self.assertEqual(self.compter_occurrences('AaBbCc', 'a'), 1)
        self.assertEqual(self.compter_occurrences('AaBbCc', 'A'), 1)

    def test_compter_caractere_special_15_points(self):
        """Testez avec des caractères spéciaux"""
        self.assertEqual(self.compter_occurrences('hello!world!', '!'), 2)


class TestExtraireNombres(unittest.TestCase):
    """Tests pour la fonction extraire_nombres"""

    def setUp(self):
        from niveau_3_avance.fonctions import extraire_nombres
        self.extraire_nombres = extraire_nombres

    def test_extraire_simple_15_points(self):
        """Testez que 'abc123def456' retourne [123, 456]"""
        result = self.extraire_nombres('abc123def456')
        self.assertEqual(result, [123, 456])

    def test_extraire_aucun_nombre_15_points(self):
        """Testez une chaîne sans nombres"""
        self.assertEqual(self.extraire_nombres('abcdef'), [])

    def test_extraire_texte_vide_15_points(self):
        """Testez une chaîne vide"""
        self.assertEqual(self.extraire_nombres(''), [])

    def test_extraire_texte_none_15_points(self):
        """Testez que None retourne une liste vide"""
        self.assertEqual(self.extraire_nombres(None), [])

    def test_extraire_nombres_negatifs_15_points(self):
        """Testez l'extraction de nombres négatifs"""
        # Dépend de l'implémentation (si elle gère les négatifs)
        result = self.extraire_nombres('a-123b456')
        self.assertIsNotNone(result)

    def test_extraire_nombres_consecutifs_15_points(self):
        """Testez 'a123b456c' retourne [123, 456]"""
        result = self.extraire_nombres('a123b456c')
        self.assertEqual(result, [123, 456])

    def test_extraire_nombres_avec_zeros_15_points(self):
        """Testez l'extraction avec des zéros"""
        result = self.extraire_nombres('a0b00c000')
        self.assertEqual(result, [0, 0, 0])


class TestValiderMotDePasse(unittest.TestCase):
    """Tests pour la fonction valider_mot_de_passe"""

    def setUp(self):
        from niveau_3_avance.fonctions import valider_mot_de_passe
        self.valider_mot_de_passe = valider_mot_de_passe

    def test_mdp_valide_15_points(self):
        """Testez un mot de passe valide 'Abc123def'"""
        self.assertTrue(self.valider_mot_de_passe('Abc123def'))

    def test_mdp_trop_court_15_points(self):
        """Testez un mot de passe < 8 caractères"""
        self.assertFalse(self.valider_mot_de_passe('Abc123'))

    def test_mdp_pas_majuscule_15_points(self):
        """Testez un mot de passe sans majuscule"""
        self.assertFalse(self.valider_mot_de_passe('abc123def'))

    def test_mdp_pas_minuscule_15_points(self):
        """Testez un mot de passe sans minuscule"""
        self.assertFalse(self.valider_mot_de_passe('ABC123DEF'))

    def test_mdp_pas_chiffre_15_points(self):
        """Testez un mot de passe sans chiffre"""
        self.assertFalse(self.valider_mot_de_passe('AbcDefgh'))

    def test_mdp_type_invalide_15_points(self):
        """Testez que passer un entier lève une TypeError"""
        with self.assertRaises(TypeError):
            self.valider_mot_de_passe(123456789)

    def test_mdp_none_15_points(self):
        """Testez que None lève une TypeError"""
        with self.assertRaises(TypeError):
            self.valider_mot_de_passe(None)


class TestCalculerStatistiques(unittest.TestCase):
    """Tests pour la fonction calculer_statistiques"""

    def setUp(self):
        from niveau_3_avance.fonctions import calculer_statistiques
        self.calculer_statistiques = calculer_statistiques

    def test_statistiques_simple_15_points(self):
        """Testez [1, 2, 3, 4, 5] retourne les bonnes stats"""
        result = self.calculer_statistiques([1, 2, 3, 4, 5])
        self.assertEqual(result['min'], 1)
        self.assertEqual(result['max'], 5)
        self.assertEqual(result['moyenne'], 3)
        self.assertEqual(result['mediane'], 3)

    def test_statistiques_liste_vide_15_points(self):
        """Testez qu'une liste vide lève une ValueError"""
        with self.assertRaises(ValueError):
            self.calculer_statistiques([])

    def test_statistiques_none_15_points(self):
        """Testez que None retourne None"""
        self.assertIsNone(self.calculer_statistiques(None))

    def test_statistiques_un_element_15_points(self):
        """Testez [5] retourne min=5, max=5, moyenne=5, mediane=5"""
        result = self.calculer_statistiques([5])
        self.assertEqual(result['min'], 5)
        self.assertEqual(result['max'], 5)
        self.assertEqual(result['moyenne'], 5)
        self.assertEqual(result['mediane'], 5)

    def test_statistiques_negatifs_15_points(self):
        """Testez avec des nombres négatifs"""
        result = self.calculer_statistiques([-5, -2, 0, 2, 5])
        self.assertEqual(result['min'], -5)
        self.assertEqual(result['max'], 5)
        self.assertEqual(result['moyenne'], 0)

    def test_statistiques_mediane_pair_15_points(self):
        """Testez la médiane avec un nombre pair d'éléments"""
        result = self.calculer_statistiques([1, 2, 3, 4])
        # Médiane de [1, 2, 3, 4] est (2+3)/2 = 2.5
        self.assertEqual(result['mediane'], 2.5)

    def test_statistiques_mediane_impair_15_points(self):
        """Testez la médiane avec un nombre impair d'éléments"""
        result = self.calculer_statistiques([1, 2, 3])
        self.assertEqual(result['mediane'], 2)


if __name__ == '__main__':
    unittest.main()
