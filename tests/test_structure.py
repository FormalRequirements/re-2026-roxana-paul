import os
import sys

# ==========================================
#              CONFIGURATION
# ==========================================
FILES_TO_CHECK = [
    "project/project_03.md",
    "project/project_04.md",
    "goals/goals_01.md",
    "goals/goals_03.md",
    "goals/goals_07.md",
    "environment/environment_03.md",
    "system/system_01.md",
    "system/system_02.md"
]
# ==========================================

def check_structure():
    # 1. Calcul des chemins
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_script_dir)
    content_root = os.path.join(project_root, 'content')

    global_error = False
    print(f"🔍 Démarrage du test (Seuls les Titres 2 '##' doivent avoir du texte)...\n")

    for relative_path in FILES_TO_CHECK:
        filepath = os.path.join(content_root, relative_path)
        file_error = False

        if not os.path.exists(filepath):
            print(f"❌ ERREUR : Le fichier '{relative_path}' est introuvable.")
            global_error = True
            continue

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except Exception as e:
            print(f"❌ ERREUR : Lecture impossible '{relative_path}'. ({e})")
            global_error = True
            continue

        last_header = None      
        line_num_header = 0     
        content_found = False   
        has_valid_h2_block = False 

        for i, line in enumerate(lines):
            stripped = line.strip()
            current_line_num = i + 1
            
            if not stripped:
                continue

            # Cas 1 : C'est un NOUVEAU TITRE
            if stripped.startswith('#'):
                # Avant de passer à ce nouveau titre, on vérifie l'ANCIEN
                if last_header is not None:
                    # --- LA REGLE D'OR ---
                    # On ne déclenche l'erreur QUE si l'ancien titre était un H2 strict (##)
                    is_h2 = last_header.startswith('##') and not last_header.startswith('###')
                    
                    if is_h2 and not content_found:
                        print(f"⚠️  VIDE : Dans '{relative_path}' (Ligne {line_num_header})")
                        print(f"          Le Titre 2 '{last_header}' n'est suivi d'aucun contenu.")
                        file_error = True
                        global_error = True

                # On enregistre le nouveau
                last_header = stripped
                line_num_header = current_line_num
                content_found = False
            
            # Cas 2 : C'est du CONTENU
            else:
                if last_header is not None:
                    content_found = True
                    # Si le titre actuel est un H2, on note qu'il est valide
                    if last_header.startswith('##') and not last_header.startswith('###'):
                        has_valid_h2_block = True

        # Vérification finale (pour le tout dernier titre du fichier)
        if last_header is not None:
            is_h2 = last_header.startswith('##') and not last_header.startswith('###')
            if is_h2 and not content_found:
                print(f"⚠️  VIDE : Dans '{relative_path}' (Ligne {line_num_header})")
                print(f"          Le dernier Titre 2 '{last_header}' n'est suivi d'aucun contenu.")
                file_error = True
                global_error = True

        # Règle de sécurité : Le fichier doit quand même contenir au moins UN Titre 2 valide
        if not has_valid_h2_block:
            print(f"⛔ MANQUANT : '{relative_path}' ne contient aucun '## Titre' avec du texte.")
            file_error = True
            global_error = True

        if not file_error: 
            print(f"✅ OK : '{relative_path}'")

    print("\n--------------------------------")
    
    if global_error:
        sys.exit(1)
    else:
        print("✨ SUCCÈS : Structure validée.")
        sys.exit(0)

if __name__ == "__main__":
    check_structure()