"""
Fonctions simples pour le Niveau 1 - Tests Unitaires Basiques
"""

def addition(a, b):
    """Retourne la somme de a et b"""
    return a + b


def multiplication(a, b):
    """Retourne le produit de a et b"""
    return a * b


def est_palindrome(s):
    """Retourne True si s est un palindrome, False sinon"""
    s = s.lower().replace(" ", "")
    return s == s[::-1]


def max_de_trois(a, b, c):
    """Retourne le maximum de trois nombres"""
    return max(a, b, c)
