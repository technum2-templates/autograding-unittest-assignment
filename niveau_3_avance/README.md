# Niveau 3 : Tests Unitaires Avancés

## Objectifs

À ce niveau, vous allez apprendre à :
- Tester des **logiques complexes** (tri, fusion, filtrage)
- Tester des **structures de données** (dictionnaires, listes imbriquées)
- Tester des **validations complexes** (mot de passe, statistiques)
- Couvrir **tous les cas limites** possibles
- Écrire des tests **robustes et exhaustifs**

## Exercices

### 1. **Trier et Filtrer** (7 tests, 105 points)
Testez une fonction qui trie et filtre une liste.

**Cas à couvrir :**
- Tri et filtrage simple
- None (retourne liste vide)
- Seuil invalide (exception)
- Aucun match
- Tous match
- Nombres négatifs
- Doublons

### 2. **Fusionner Dictionnaires** (7 tests, 105 points)
Testez une fonction qui fusionne deux dictionnaires.

**Cas à couvrir :**
- Fusion simple
- Clés communes (dict2 prend le dessus)
- None et None
- Dictionnaire vide
- Type invalide (exception)
- Valeurs complexes
- Vérifier que les originaux ne sont pas modifiés

### 3. **Compter Occurrences** (7 tests, 105 points)
Testez une fonction qui compte les occurrences d'un caractère.

**Cas à couvrir :**
- Comptage simple
- Aucune occurrence
- Texte vide
- Texte None
- Caractère None
- Sensibilité à la casse
- Caractères spéciaux

### 4. **Extraire Nombres** (7 tests, 105 points)
Testez une fonction qui extrait tous les nombres d'une chaîne.

**Cas à couvrir :**
- Extraction simple
- Aucun nombre
- Texte vide
- Texte None
- Nombres négatifs
- Nombres consécutifs
- Zéros

### 5. **Valider Mot de Passe** (7 tests, 105 points)
Testez une fonction qui valide un mot de passe robuste.

**Cas à couvrir :**
- Mot de passe valide
- Trop court
- Pas de majuscule
- Pas de minuscule
- Pas de chiffre
- Type invalide (exception)
- None (exception)

### 6. **Calculer Statistiques** (7 tests, 105 points)
Testez une fonction qui calcule min, max, moyenne, médiane.

**Cas à couvrir :**
- Statistiques simples
- Liste vide (exception)
- None (retourne None)
- Un élément
- Nombres négatifs
- Médiane avec nombre pair d'éléments
- Médiane avec nombre impair d'éléments

## Total

- **6 exercices**
- **42 tests**
- **630 points**

## Conseils

1. **Testez la logique complexe** : tri, fusion, filtrage
2. **Testez les structures de données** : dictionnaires, listes
3. **Couvrez TOUS les cas limites** : None, vide, négatif, zéro
4. **Testez les exceptions** : type invalide, liste vide
5. **Vérifiez les effets secondaires** : les originaux ne doivent pas être modifiés
6. **Testez les résultats** : min, max, moyenne, médiane

## Barème

- 15 points par test réussi
- Total : 630 points

## Progression

**Niveau 1** → **Niveau 2** → **Niveau 3**

À ce stade, vous devez être capable de :
- Écrire des tests complets et exhaustifs
- Couvrir tous les cas limites
- Tester des logiques complexes
- Valider les exceptions
- Vérifier les effets secondaires
