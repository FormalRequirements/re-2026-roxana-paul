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
    print(f"Démarrage du test strict (H2 + Paragraphe) sur {len(FILES_TO_CHECK)} fichier(s)...\n")

    for relative_path in FILES_TO_CHECK:
        filepath = os.path.join(content_root, relative_path)
        file_error = False # Pour savoir si CE fichier a échoué

        # A. Vérification de l'existence
        if not os.path.exists(filepath):
            print(f"ERREUR : Le fichier '{relative_path}' est introuvable.")
            global_error = True
            continue

        # B. Lecture du fichier
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except Exception as e:
            print(f"ERREUR : Impossible de lire '{relative_path}'. ({e})")
            global_error = True
            continue

        last_header = None      
        line_num_header = 0     
        content_found = False   
        
        # NOUVEAU : On track si on a trouvé au moins un H2 valide
        has_valid_h2_block = False 

        for i, line in enumerate(lines):
            stripped = line.strip()
            current_line_num = i + 1
            
            if not stripped:
                continue

            # Cas 1 : C'est un TITRE
            if stripped.startswith('#'):
                # Vérifier si le titre précédent était vide (Règle générale)
                if last_header is not None and not content_found:
                    print(f"VIDE : Dans '{relative_path}' (Ligne {line_num_header})")
                    print(f"Le titre '{last_header}' n'est suivi d'aucun contenu.")
                    file_error = True
                    global_error = True

                # Reset pour le nouveau titre
                last_header = stripped
                line_num_header = current_line_num
                content_found = False
            
            # Cas 2 : C'est du CONTENU
            else:
                if last_header is not None:
                    content_found = True
                    
                    # --- LA NOUVELLE REGLE ICI ---
                    # Si le titre au-dessus commence par '##' (mais pas '###')
                    # Alors on considère que l'exigence est remplie.
                    if last_header.startswith('##') and not last_header.startswith('###'):
                        has_valid_h2_block = True

        # Vérification du tout dernier titre du fichier
        if last_header is not None and not content_found:
            print(f"VIDE : Dans '{relative_path}' (Ligne {line_num_header})")
            print(f"Le dernier titre '{last_header}' n'est suivi d'aucun contenu.")
            file_error = True
            global_error = True

        # --- VERIFICATION FINALE POUR CE FICHIER ---
        if not has_valid_h2_block:
            print(f"MANQUANT : '{relative_path}' ne contient aucun Titre 2 (##) avec du contenu.")
            print(f"Règle : Chaque fichier listé doit avoir au moins une exigence de niveau 2.")
            file_error = True
            global_error = True

        # Si tout est OK pour ce fichier précis
        if not file_error: 
            print(f"OK : '{relative_path}'")

    print("\n--------------------------------")
    
    if global_error:
        print("ECHEC : Certains fichiers ne respectent pas les règles.")
        sys.exit(1)
    else:
        print("SUCCÈS : Structure validée.")
        sys.exit(0)

if __name__ == "__main__":
    check_structure()