import markdown
import os
from jinja2 import Template

# --- CONFIGURATION ---
CONTENT_DIR = 'content'
OUTPUT_FILE = 'document_pegs.html'
TEMPLATE_FILE = 'templates/template.html'

# Ordre strict des dossiers selon la méthode PEGS
# Goals -> Environment -> System -> Project
PEGS_ORDER = ['goals', 'environment', 'system', 'project']

def get_markdown_content():
    """Parcourt les dossiers et concatène tous les fichiers .md trouvés."""
    full_text = ""
    
    for folder in PEGS_ORDER:
        folder_path = os.path.join(CONTENT_DIR, folder)
        
        # Vérifie si le dossier existe
        if not os.path.exists(folder_path):
            print(f"Attention : Le dossier '{folder}' n'existe pas, je le saute.")
            continue
            
        print(f"📂 Traitement du dossier : {folder.upper()}...")
        
        # Récupère tous les fichiers .md du dossier
        files = [f for f in os.listdir(folder_path) if f.endswith('.md')]
        
        # IMPORTANT : On trie par nom pour respecter votre numérotation (01, 02, etc.)
        files.sort()
        
        for filename in files:
            filepath = os.path.join(folder_path, filename)
            print(f"   📄 Lecture de {filename}")
            
            with open(filepath, 'r', encoding='utf-8') as f:
                # On ajoute le contenu + des sauts de ligne pour éviter que les textes se collent
                full_text += f.read() + "\n\n"
    
    return full_text

def build_html():
    # 1. Récupération du contenu brut fusionné
    raw_md = get_markdown_content()
    
    if not raw_md:
        print("Erreur : Aucun contenu Markdown trouvé.")
        return

    # 2. Conversion Markdown -> HTML
    # 'toc' génère le sommaire, 'tables' gère les tableaux
    md = markdown.Markdown(extensions=['toc', 'tables', 'fenced_code'])
    html_content = md.convert(raw_md)
    
    # 3. Injection dans le template
    try:
        with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
            template = Template(f.read())
            
        final_html = template.render(
            content=html_content,
            toc=md.toc,  # Le sommaire généré automatiquement
            title="Spécifications PEGS"
        )
        
        # 4. Écriture du fichier final
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write(final_html)
            
        print(f"Succès ! Document généré : {OUTPUT_FILE}")
        
    except FileNotFoundError:
        print(f"Erreur : Le fichier template '{TEMPLATE_FILE}' est introuvable.")

if __name__ == "__main__":
    build_html()