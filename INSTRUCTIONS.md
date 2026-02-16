# Instructions pour l'Assignation : Tests Unitaires

Bienvenue ! Votre mission est d'écrire des tests unitaires pour une série de fonctions Python.

---

## Votre Objectif

Pour chaque niveau (`niveau_1`, `niveau_2`, `niveau_3`) :

1.  Ouvrez le fichier `fonctions.py` pour comprendre ce que le code est censé faire.
2.  Ouvrez le fichier `test_fonctions.py`.
3.  **Complétez les tests** marqués avec `# TODO`.
4.  Vous ne devez **PAS** modifier le fichier `fonctions.py`.

---

## Comment Travailler

### 1. Cloner le Dépôt

Clonez ce dépôt sur votre machine locale.

```bash
git clone <url-de-votre-depot>
cd <nom-du-depot>
```

### 2. Installer les Dépendances

Vous aurez besoin de `pytest`.

```bash
pip install pytest pytest-json-report
```

### 3. Écrire un Test

Dans `test_fonctions.py`, trouvez un `TODO` et écrivez votre assertion.

```python
# Avant
def test_addition_cas_simple_5_points():
    # TODO: Testez que 2 + 2 = 4
    pass

# Après
def test_addition_cas_simple_5_points():
    from fonctions import addition
    assert addition(2, 2) == 4
```

### 4. Tester Localement

Ouvrez un terminal et lancez `pytest` pour vérifier votre travail.

```bash
# Lancer tous les tests
pytest -v

# Lancer les tests d'un niveau spécifique
pytest niveau_1_basique/ -v
```

### 5. Sauvegarder et Pousser

Une fois que vos tests passent localement, envoyez-les sur GitHub.

```bash
git add .
git commit -m "Termine les tests du niveau 1"
git push origin main
```

### 6. Voir votre Score

-   Allez sur votre dépôt GitHub.
-   Cliquez sur l'onglet **"Actions"**.
-   Vous verrez une coche verte ✅ si tout va bien, et votre score sera affiché.

---

Bonne chance ! 🚀
