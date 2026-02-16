"""
Configuration pytest pour tous les niveaux
"""
import sys
from pathlib import Path

# Ajouter les dossiers de niveau au path pour les imports
sys.path.insert(0, str(Path(__file__).parent / 'niveau_1_basique'))
sys.path.insert(0, str(Path(__file__).parent / 'niveau_2_intermediaire'))
sys.path.insert(0, str(Path(__file__).parent / 'niveau_3_avance'))
