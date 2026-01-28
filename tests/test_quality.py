import os
import sys

# --- CONFIGURATION DES CHEMINS ---

# 1. On récupère le dossier où se trouve CE script (c'est-à-dire 'tests/')
test_dir = os.path.dirname(os.path.abspath(__file__))

# 2. On remonte d'un cran pour trouver la racine du projet
project_root = os.path.dirname(test_dir)

# 3. On cible le dossier content à partir de la racine
CONTENT_ROOT = os.path.join(project_root, 'content')

FOLDERS = ['goals', 'environment', 'project', 'system']

def check_files():
    has_error = False
    
    print("🔍 Démarrage des tests de qualité...\n")

    for folder in FOLDERS:
        dir_path = os.path.join(CONTENT_ROOT, folder)
        
        # 1. Vérifier si le dossier existe
        if not os.path.exists(dir_path):
            print(f"❌ ERREUR : Le dossier '{folder}' est introuvable.")
            has_error = True
            continue
            
        files = [f for f in os.listdir(dir_path) if f.endswith('.md')]
        
        # 2. Vérifier si le dossier est vide
        if not files:
            print(f"⚠️  ATTENTION : Le dossier '{folder}' ne contient aucun fichier Markdown.")
            # On ne met pas forcément en erreur ici, sauf si c'est obligatoire pour vous
        
        # 3. Vérifier le contenu de chaque fichier
        for filename in files:
            filepath = os.path.join(dir_path, filename)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read().strip() # .strip() enlève les espaces et sauts de ligne inutiles
                
            if not content:
                print(f"❌ ERREUR : Le fichier '{folder}/{filename}' est VIDE.")
                has_error = True
            else:
                print(f"✅ OK : {folder}/{filename} ({len(content)} caractères)")

    print("\n--------------------------------")
    
    if has_error:
        print("⛔ ECHEC DES TESTS : Corrigez les erreurs ci-dessus.")
        sys.exit(1) # C'est ce code '1' qui dit à GitHub d'arrêter tout de suite
    else:
        print("✨ SUCCÈS : Tous les fichiers sont valides.")
        sys.exit(0)

if __name__ == "__main__":
    check_files()