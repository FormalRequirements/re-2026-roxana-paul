import os
import sys

# ==========================================
#              CONFIGURATION
# ==========================================
FILES_TO_CHECK = [
    "projet/project_03.md",
    "projet/project_04.md",
    "goals/goals_01.md",
    "goals/goals_03.md",
    "goals/goals_07.md",
    "environment/environment_03.md",
    "system/system_01.md",
    "system/system_02.md"
]
# ==========================================

def check_structure():
    # 1. Calcul dynamique des chemins pour trouver le dossier 'content'
    #    (Fonctionne que l'on lance le script depuis la racine ou depuis tests/)
    current_script_dir = os.path.dirname(os.path.abspath(__file__)) # Dossier tests/
    project_root = os.path.dirname(current_script_dir)              # Racine du projet
    content_root = os.path.join(project_root, 'content')            # Dossier content/

    has_error = False
    print(f"🔍 Démarrage du test de structure sur {len(FILES_TO_CHECK)} fichier(s)...\n")

    for relative_path in FILES_TO_CHECK:
        filepath = os.path.join(content_root, relative_path)
        
        # A. Vérification de l'existence du fichier
        if not os.path.exists(filepath):
            print(f"ERREUR : Le fichier '{relative_path}' est introuvable.")
            has_error = True
            continue

        # B. Analyse du contenu ligne par ligne
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except Exception as e:
            print(f"ERREUR : Impossible de lire '{relative_path}'. ({e})")
            has_error = True
            continue

        last_header = None      # Le dernier titre rencontré
        line_num_header = 0     # Le numéro de ligne du titre
        content_found = False   # A-t-on trouvé du texte après ce titre ?

        for i, line in enumerate(lines):
            stripped = line.strip()
            current_line_num = i + 1
            
            # On ignore les lignes vides
            if not stripped:
                continue

            # Cas 1 : C'est un TITRE (commence par #)
            if stripped.startswith('#'):
                # Si on avait un titre en attente et qu'on n'a rien trouvé avant ce nouveau titre
                if last_header is not None and not content_found:
                    print(f"VIDE : Dans '{relative_path}' (Ligne {line_num_header})")
                    print(f"Le titre '{last_header}' n'est suivi d'aucun contenu.")
                    has_error = True

                # On mémorise ce nouveau titre et on reset le compteur
                last_header = stripped
                line_num_header = current_line_num
                content_found = False
            
            # Cas 2 : C'est du CONTENU (Texte, liste, image...)
            else:
                # Si on a un titre en mémoire, on valide qu'il a du contenu
                if last_header is not None:
                    content_found = True

        # Vérification finale pour le TOUT DERNIER titre du fichier
        if last_header is not None and not content_found:
            print(f"VIDE : Dans '{relative_path}' (Ligne {line_num_header})")
            print(f"Le dernier titre '{last_header}' n'est suivi d'aucun contenu.")
            has_error = True

        # Si aucune erreur n'a été marquée pour ce fichier spécifique
        if not has_error: 
            # Note: ceci affiche OK même si un AUTRE fichier a échoué avant, 
            # mais ça permet de voir ce qui va bien.
            print(f"OK : '{relative_path}'")

    print("\n--------------------------------")
    
    if has_error:
        print("ECHEC : La structure de certains fichiers est invalide (Titres vides).")
        sys.exit(1) # Retourne une erreur à GitHub Actions
    else:
        print("SUCCÈS : Tous les fichiers testés sont conformes.")
        sys.exit(0) # Retourne un succès

if __name__ == "__main__":
    check_structure()