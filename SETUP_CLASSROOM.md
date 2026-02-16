# Guide : Configurer cette Assignation dans GitHub Classroom

Ce document explique comment importer cette assignation dans GitHub Classroom et l'utiliser avec vos étudiants.

---

## 📋 Prérequis

1. Un compte GitHub (gratuit)
2. Une organisation GitHub Classroom (créée dans votre compte GitHub)
3. Ce dépôt importé comme template dans votre organisation

---

## 🚀 Étapes de Configuration

### Étape 1 : Créer un Dépôt Template

1. Allez sur GitHub et créez un nouveau dépôt privé dans votre organisation
2. Nommez-le `autograding-unittest-assignment`
3. Importez le contenu de ce dossier dans le dépôt (ou utilisez "Import a repository")
4. Allez dans **Settings → Template repository** et cochez la case pour le rendre template

### Étape 2 : Créer l'Assignation dans GitHub Classroom

1. Allez sur https://classroom.github.com
2. Sélectionnez votre organisation
3. Cliquez sur **"New assignment"**
4. Remplissez les informations :
   - **Assignment name** : "Tests Unitaires - Autograding"
   - **Repository prefix** : "unittest-assignment"
   - **Visibility** : "Private"
   - **Repository template** : Sélectionnez `autograding-unittest-assignment`

### Étape 3 : Configurer l'Autograding (Optionnel mais Recommandé)

1. Dans la section **"Add autograding tests"**, cliquez sur **"Add test"**
2. Choisissez **"Run command"**
3. Remplissez les champs :
   - **Test name** : "Run pytest"
   - **Command** : `pip install pytest && pytest --tb=short -v`
   - **Points** : Vous pouvez laisser vide (les points sont dans les noms des tests)
4. Cliquez sur **"Save"**

### Étape 4 : Ajouter une Description

1. Allez dans **"Edit assignment"**
2. Ajoutez une **description** :
   ```
   Écrivez des tests unitaires pour les fonctions fournies.
   Utilisez pytest pour tester votre code.
   Les points sont automatiquement calculés en fonction des tests réussis.
   
   Niveaux :
   - Niveau 1 (Basique) : 20 points
   - Niveau 2 (Intermédiaire) : 40 points
   - Niveau 3 (Avancé) : 40 points
   Total : 100 points
   ```
3. Définissez une **deadline** si souhaité

### Étape 5 : Générer le Lien d'Invitation

1. Cliquez sur **"Copy invitation link"**
2. Partagez ce lien avec vos étudiants par e-mail ou sur votre plateforme de cours

---

## 💯 Barème de Points

Le barème est codé directement dans les noms des tests pour être compatible avec l'autograding de GitHub Classroom.

| Niveau | Exercice | Points par Test | Total Niveau |
| :--- | :--- | :--- | :--- |
| **Niveau 1** | Fonctions de base (addition, multiplication, palindrome, max) | 5 points | 20 points |
| **Niveau 2** | Erreurs et collections | 10 points | 40 points |
| **Niveau 3** | Fixtures et paramétrisation | 15 points | 40 points |
| **TOTAL** | | | **100 points** |

---

## 🎯 Flux de Travail pour les Étudiants

1. **Accepter l'assignation** : Cliquer sur le lien d'invitation
2. **Cloner le dépôt** : `git clone <url>`
3. **Compléter les tests** : Modifier `test_fonctions.py` pour chaque niveau
4. **Tester localement** : `pytest -v`
5. **Pousser sur GitHub** : `git push origin main`
6. **Voir le score** : Aller dans l'onglet "Actions" du dépôt

---

## 📝 Personnaliser l'Assignation

### Ajouter des Niveaux Supplémentaires

1. Créez un nouveau dossier `niveau_4_*`
2. Copiez la structure de `niveau_1_basique`
3. Modifiez `fonctions.py` et `test_fonctions.py`
4. Mettez à jour `conftest.py` pour inclure le nouveau niveau
5. Mettez à jour `pytest.ini` pour inclure le nouveau dossier

### Modifier le Barème

Changez les noms des tests pour modifier les points :

```python
# Avant : 5 points
def test_addition_simple_5_points():
    pass

# Après : 10 points
def test_addition_simple_10_points():
    pass
```

### Ajouter des Instructions Personnalisées

Modifiez `INSTRUCTIONS.md` pour inclure vos propres directives spécifiques à votre cours.

---

## 🔍 Dépannage

| Problème | Solution |
| :--- | :--- |
| **Les tests ne s'exécutent pas** | Vérifiez que `pytest` est installé. Vérifiez la syntaxe des fichiers. |
| **Le score n'apparaît pas** | Assurez-vous que les noms des tests contiennent `_X_points`. |
| **Les étudiants ne peuvent pas cloner** | Vérifiez que le dépôt est privé et qu'ils ont accès via Classroom. |
| **GitHub Actions échoue** | Vérifiez les logs dans l'onglet "Actions" du dépôt. |
| **Les imports ne fonctionnent pas** | Vérifiez que `conftest.py` ajoute bien les chemins au sys.path. |

---

## 📚 Ressources Supplémentaires

- [Documentation pytest](https://docs.pytest.org/)
- [GitHub Classroom Documentation](https://classroom.github.com/help)
- [Python unittest vs pytest](https://realpython.com/pytest-vs-unittest/)

---

**Vous êtes prêt !** Partagez le lien d'invitation avec vos étudiants et commencez ! 🎓
