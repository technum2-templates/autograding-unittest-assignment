"""
Solutions pour le Niveau 1 - Tests Unitaires Basiques
"""
import pytest


# ============================================================================
# EXERCICE 1 : Addition
# ============================================================================

def test_addition_positifs_5_points():
    """Testez que 2 + 3 = 5"""
    from fonctions import addition
    assert addition(2, 3) == 5


def test_addition_negatifs_5_points():
    """Testez que -2 + -3 = -5"""
    from fonctions import addition
    assert addition(-2, -3) == -5


def test_addition_mixte_5_points():
    """Testez que 5 + (-3) = 2"""
    from fonctions import addition
    assert addition(5, -3) == 2


def test_addition_zero_5_points():
    """Testez que 0 + 5 = 5"""
    from fonctions import addition
    assert addition(0, 5) == 5


# ============================================================================
# EXERCICE 2 : Multiplication
# ============================================================================

def test_multiplication_positifs_5_points():
    """Testez que 3 * 4 = 12"""
    from fonctions import multiplication
    assert multiplication(3, 4) == 12


def test_multiplication_par_zero_5_points():
    """Testez que 5 * 0 = 0"""
    from fonctions import multiplication
    assert multiplication(5, 0) == 0


def test_multiplication_par_un_5_points():
    """Testez que 5 * 1 = 5"""
    from fonctions import multiplication
    assert multiplication(5, 1) == 5


def test_multiplication_negatifs_5_points():
    """Testez que -2 * -3 = 6"""
    from fonctions import multiplication
    assert multiplication(-2, -3) == 6


# ============================================================================
# EXERCICE 3 : Palindrome
# ============================================================================

def test_palindrome_simple_5_points():
    """Testez que 'aba' est un palindrome"""
    from fonctions import est_palindrome
    assert est_palindrome('aba') == True


def test_non_palindrome_5_points():
    """Testez que 'abc' n'est pas un palindrome"""
    from fonctions import est_palindrome
    assert est_palindrome('abc') == False


def test_palindrome_avec_espaces_5_points():
    """Testez que 'a b a' est un palindrome"""
    from fonctions import est_palindrome
    assert est_palindrome('a b a') == True


def test_palindrome_vide_5_points():
    """Testez que '' est un palindrome"""
    from fonctions import est_palindrome
    assert est_palindrome('') == True


# ============================================================================
# EXERCICE 4 : Maximum de Trois
# ============================================================================

def test_max_trois_simple_5_points():
    """Testez que max_de_trois(1, 5, 3) = 5"""
    from fonctions import max_de_trois
    assert max_de_trois(1, 5, 3) == 5


def test_max_trois_negatifs_5_points():
    """Testez que max_de_trois(-1, -5, -3) = -1"""
    from fonctions import max_de_trois
    assert max_de_trois(-1, -5, -3) == -1


def test_max_trois_identiques_5_points():
    """Testez que max_de_trois(3, 3, 3) = 3"""
    from fonctions import max_de_trois
    assert max_de_trois(3, 3, 3) == 3


def test_max_trois_zeros_5_points():
    """Testez que max_de_trois(0, 0, 0) = 0"""
    from fonctions import max_de_trois
    assert max_de_trois(0, 0, 0) == 0
