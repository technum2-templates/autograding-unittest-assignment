# Niveau 2 : Tests Unitaires Intermédiaires

## Objectifs

À ce niveau, vous allez apprendre à :
- Tester des fonctions avec **gestion d'erreurs** (exceptions)
- Tester des **cas limites** (None, vide, négatif, zéro)
- Utiliser `assertRaises` pour vérifier les exceptions
- Tester des **collections** (listes, dictionnaires)

## Exercices

### 1. **Diviser** (6 tests, 60 points)
Testez une fonction de division qui lève une `ValueError` si le diviseur est 0.

**Cas à couvrir :**
- Division simple
- Division par zéro (exception)
- Nombres négatifs
- Résultats décimaux
- Division par 1
- Zéro divisé par un nombre

### 2. **Calculer Moyenne** (6 tests, 60 points)
Testez une fonction qui calcule la moyenne d'une liste.

**Cas à couvrir :**
- Liste simple
- Liste vide (exception)
- None (retourne 0)
- Nombres négatifs
- Un seul élément
- Nombres décimaux

### 3. **Valider Email** (6 tests, 60 points)
Testez une fonction qui valide un email simple.

**Cas à couvrir :**
- Email valide
- Sans @
- Sans point
- Chaîne vide
- None
- Plusieurs @

### 4. **Compter Voyelles** (6 tests, 60 points)
Testez une fonction qui compte les voyelles.

**Cas à couvrir :**
- Texte simple
- Chaîne vide
- None
- Majuscules
- Pas de voyelles
- Toutes les voyelles

### 5. **Inverser Liste** (6 tests, 60 points)
Testez une fonction qui inverse une liste.

**Cas à couvrir :**
- Liste simple
- Liste vide
- None
- Un élément
- Deux éléments
- Vérifier que l'original n'est pas modifié

### 6. **Filtrer Pairs** (6 tests, 60 points)
Testez une fonction qui filtre les nombres pairs.

**Cas à couvrir :**
- Liste simple
- Liste vide
- None
- Aucun pair
- Tous pairs
- Nombres négatifs

## Total

- **6 exercices**
- **36 tests**
- **360 points**

## Conseils

1. **Utilisez `setUp()`** pour importer les fonctions
2. **Testez les exceptions** avec `self.assertRaises()`
3. **Couvrez les cas limites** : None, vide, négatif, zéro
4. **Testez les collections** : listes, dictionnaires
5. **Vérifiez les effets secondaires** : la fonction modifie-t-elle l'original ?

## Barème

- 10 points par test réussi
- Total : 360 points
