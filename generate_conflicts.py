#!/usr/bin/env python3
"""
Script pour générer 10 branches IDENTIQUES avec un conflit MEDIUM
SANS TOUCHER À MAIN - Idéal pour des étudiants qui apprennent Git

Le conflit sera pédagogique :
- Visible et compréhensible (modifications sur les mêmes fonctions)
- Pas trop complexe (pas de restructuration majeure)
- Nécessite de faire des choix (garder quoi de chaque version ?)
- Les tests doivent passer après résolution

Usage: python generate_conflicts.py
"""

import subprocess
import sys

def run_command(cmd, check=True, silent=False):
    """Exécute une commande shell"""
    if not silent:
        print(f"  → {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"  ❌ Erreur: {result.stderr}")
        sys.exit(1)
    return result


def main():
    print("="*70)
    print("🎓 GÉNÉRATION DE 10 BRANCHES AVEC UN CONFLIT PÉDAGOGIQUE")
    print("   (niveau MEDIUM - sans modifier main)")
    print("="*70)
    
    # Vérifier qu'on est dans un repo git
    result = run_command("git rev-parse --git-dir", check=False, silent=True)
    if result.returncode != 0:
        print("❌ Erreur: Vous devez être dans un repository git")
        sys.exit(1)
    
    # S'assurer qu'on est sur main
    print("\n📍 Étape 1: Vérification de main")
    run_command("git checkout main")
    run_command("git pull origin main", check=False)
    
    # Récupérer le hash du commit actuel de main
    result = run_command("git rev-parse HEAD", silent=True)
    main_commit = result.stdout.strip()
    print(f"  ✓ Main est au commit: {main_commit[:8]}")
    
    # Revenir 1 commit en arrière pour créer les branches
    print("\n📍 Étape 2: Positionnement au commit parent")
    run_command("git checkout HEAD~1")
    base_commit_result = run_command("git rev-parse HEAD", silent=True)
    base_commit = base_commit_result.stdout.strip()
    print(f"  ✓ Point de départ: {base_commit[:8]}")
    
    # Contenu qui va créer un conflit MEDIUM avec main
    # Conflit sur add() et divide() - deux endroits distincts
    conflicting_content = '''def add(a, b):
    """Addition de deux nombres
    
    Cette fonction additionne a et b.
    
    Args:
        a: Premier nombre à additionner
        b: Deuxième nombre à additionner
    
    Returns:
        La somme de a et b
    """
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    """Division de a par b
    
    Args:
        a: Le numérateur
        b: Le dénominateur
    
    Returns:
        Le résultat de a / b
    
    Raises:
        ZeroDivisionError: Si b vaut 0
    """
    if b == 0:
        raise ZeroDivisionError("Erreur : impossible de diviser par zéro")
    result = a / b
    return result
'''
    
    # Créer les 10 branches identiques
    print("\n🌿 Étape 3: Création des 10 branches étudiants")
    
    for i in range(1, 16):
        branch_name = f"etudiant-{i:02d}-conflict"
        print(f"\n  📌 Branche {branch_name}")
        
        # Revenir au commit de base
        run_command(f"git checkout {base_commit}", silent=True)
        
        # Créer la branche
        run_command(f"git checkout -b {branch_name}", silent=True)
        
        # Appliquer la version conflictuelle
        with open('src/calculator.py', 'w', encoding='utf-8') as f:
            f.write(conflicting_content)
        
        run_command("git add src/calculator.py", silent=True)
        run_command(f'git commit -m "docs: amélioration documentation add() et divide()"', silent=True)
        
        # Pousser la branche
        run_command(f"git push -u origin {branch_name}")
        
        print(f"  ✅ {branch_name} créée")
    
    # Retourner sur main
    print("\n📍 Étape 4: Retour sur main")
    run_command("git checkout main")
    
    print("\n" + "="*70)
    print("✅ GÉNÉRATION TERMINÉE !")
    print("="*70)
    print("\n📋 Ce qui a été créé:")
    print(f"  • Main reste intact (commit: {main_commit[:8]})")
    print(f"  • 10 branches depuis le commit: {base_commit[:8]}")
    print(f"  • Toutes les branches ont le MÊME code conflictuel")
    
    print("\n🎯 Zones de conflit (MEDIUM) :")
    print("  ⚠️  Fonction add():")
    print("      - Docstring différente entre main et branches")
    print("      - Les étudiants doivent choisir quelle doc garder")
    print()
    print("  ⚠️  Fonction divide():")
    print("      - Docstring différente")
    print("      - Message d'erreur différent")
    print("      - Variable 'result' ajoutée (ligne supplémentaire)")
    print("      - Les étudiants doivent fusionner intelligemment")
    
    print("\n💡 Processus pour les étudiants:")
    print("  1. Cloner le repo")
    print("  2. Checkout leur branche (etudiant-XX-conflict)")
    print("  3. Faire: git merge main")
    print("  4. Git signalera un conflit dans src/calculator.py")
    print("  5. Ouvrir le fichier et résoudre les marqueurs <<<<< ===== >>>>>")
    print("  6. Décider quelle version garder (ou combiner les deux)")
    print("  7. git add src/calculator.py")
    print("  8. git commit")
    print("  9. Vérifier que les tests passent: pytest")
    print(" 10. git push")
    print(" 11. Créer une Pull Request vers main")
    
    print("\n📚 Points d'apprentissage:")
    print("  ✓ Comprendre ce qu'est un conflit Git")
    print("  ✓ Lire les marqueurs de conflit")
    print("  ✓ Prendre des décisions sur quelle version garder")
    print("  ✓ Tester après résolution")
    print("  ✓ Workflow PR après merge")
    
    print("\n⏱️  Temps estimé par étudiant: 15-30 minutes")
    print("="*70)


if __name__ == "__main__":
    main()