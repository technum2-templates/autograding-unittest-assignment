# Assignation : Maîtriser les Tests Unitaires en Python

Ce dépôt contient une série d'exercices progressifs pour apprendre à écrire des tests unitaires efficaces en Python avec `pytest`. L'objectif est de fournir aux étudiants des fonctions pré-écrites et de leur demander d'écrire les tests correspondants.

---

## 🎯 Objectifs Pédagogiques

-   **Comprendre le "Pourquoi"** : Saisir l'importance des tests pour la robustesse et la maintenance du code.
-   **Maîtriser `pytest`** : Apprendre à utiliser le framework de test le plus populaire en Python.
-   **Écrire des Assertions Pertinentes** : Savoir choisir la bonne assertion (`assert`, `pytest.raises`) pour chaque cas.
-   **Couvrir les Cas Limites** : Penser aux scénarios qui pourraient casser le code (valeurs nulles, listes vides, types incorrects, etc.).
-   **Adopter le TDD (Test-Driven Development)** : S'initier à l'écriture des tests *avant* le code.

---

## 📂 Structure du Dépôt

Le projet est divisé en trois niveaux de difficulté croissante :

1.  **`niveau_1_basique/`** : Introduction aux concepts de base.
    -   Assertions simples (`assert a == b`).
    -   Tests sur des fonctions mathématiques pures.

2.  **`niveau_2_intermediaire/`** : Gestion des erreurs et des cas plus complexes.
    -   Tester les exceptions avec `pytest.raises`.
    -   Travailler avec des listes et des dictionnaires.

3.  **`niveau_3_avance/`** : Techniques avancées et bonnes pratiques.
    -   Utilisation des fixtures pour préparer le contexte des tests.
    -   Paramétrisation pour tester de multiples entrées avec un seul test.

Chaque dossier contient :
-   `fonctions.py` : Le code que les étudiants doivent tester.
-   `test_fonctions.py` : Le fichier où les étudiants doivent écrire leurs tests (avec des `TODO`).
-   `solutions/test_fonctions.py` : La solution complète (pour le professeur).

---

## 🤖 Fonctionnement de l'Auto-Grading

Ce dépôt est configuré avec **GitHub Actions** pour fournir un feedback automatisé et un score à chaque `push`.

1.  **Déclenchement** : À chaque `push` sur la branche `main`, un workflow se lance.
2.  **Exécution des Tests** : Le workflow exécute `pytest` sur les fichiers `test_*.py` écrits par l'étudiant.
3.  **Calcul du Score** :
    -   Chaque test réussi rapporte des points.
    -   Le nombre total de points est défini dans le fichier de workflow (`.github/workflows/autograding.yml`).
    -   Les tests sont nommés de manière à correspondre aux points (ex: `test_addition_positive_5_points`).
4.  **Feedback** : L'étudiant peut voir son score et les tests échoués directement dans l'onglet "Actions" de son dépôt.

---

## 🎓 Comment Utiliser avec GitHub Classroom

1.  **Créer une Nouvelle Assignation** : Dans votre "Classroom", cliquez sur "New assignment".
2.  **Utiliser ce Dépôt comme Template** :
    -   Choisissez "Use a template repository".
    -   Fournissez l'URL de ce dépôt (une fois que vous l'aurez vous-même mis sur GitHub).
3.  **Activer les Tests d'Auto-Grading** :
    -   Lors de la création de l'assignation, allez dans la section "Add autograding tests".
    -   Cliquez sur "Run command".
    -   Dans le champ "Command", entrez : `pytest --json-report --json-report-file=report.json`
    -   Les points seront automatiquement extraits des noms des tests.
4.  **Nommer l'Assignation** : Donnez un nom clair (ex: "Labo 2 - Tests Unitaires").
5.  **Envoyer le Lien aux Étudiants** : Partagez le lien d'invitation généré par GitHub Classroom.

---

## 💯 Barème de Points (Exemple)

Le barème est défini dans les noms des tests pour être compatible avec l'autograding de GitHub Classroom.

| Niveau | Exercice | Points par Test | Total Niveau |
| :--- | :--- | :--- | :--- |
| **Niveau 1** | Fonctions de base | 5 points | 20 points |
| **Niveau 2** | Erreurs et collections | 10 points | 40 points |
| **Niveau 3** | Fixtures et paramétrisation | 15 points | 40 points |
| **TOTAL** | | | **100 points** |

Ce README fournit toutes les informations nécessaires pour que vous, en tant que professeur, puissiez déployer cette assignation rapidement et efficacement.
