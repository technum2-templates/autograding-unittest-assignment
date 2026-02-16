# Niveau 1 : Tests Unitaires Basiques

Bienvenue au premier niveau ! Vous allez apprendre les bases de `pytest` en écrivant des tests pour des fonctions simples.

---

## 📚 Concepts Clés

-   **Assertion** : Une vérification que quelque chose est vrai. Syntaxe : `assert condition`
-   **Test** : Une fonction qui vérifie qu'une partie du code fonctionne correctement.
-   **pytest** : Un framework Python pour écrire et exécuter des tests.

---

## 🎯 Exercices

### Exercice 1 : Tester une Addition

**Fichier** : `fonctions.py::addition(a, b)`

**Fonction à tester** :
```python
def addition(a, b):
    """Retourne la somme de a et b"""
    return a + b
```

**Cas de test à couvrir** :
1. Deux nombres positifs
2. Deux nombres négatifs
3. Un nombre positif et un négatif
4. Zéro

**Exemple de test** :
```python
def test_addition_cas_simple_5_points():
    from fonctions import addition
    assert addition(2, 2) == 4
```

---

### Exercice 2 : Tester une Multiplication

**Fonction à tester** :
```python
def multiplication(a, b):
    """Retourne le produit de a et b"""
    return a * b
```

**Cas de test à couvrir** :
1. Deux nombres positifs
2. Multiplication par zéro
3. Multiplication par un

---

### Exercice 3 : Tester une Fonction de Chaîne

**Fonction à tester** :
```python
def est_palindrome(s):
    """Retourne True si s est un palindrome, False sinon"""
    s = s.lower().replace(" ", "")
    return s == s[::-1]
```

**Cas de test à couvrir** :
1. Un palindrome simple
2. Un non-palindrome
3. Une chaîne vide
4. Une chaîne avec espaces

---

## 📋 Barème

-   Chaque test réussi = 5 points
-   Total du niveau = 20 points

---

Commencez par `test_fonctions.py` et complétez les `TODO` !
