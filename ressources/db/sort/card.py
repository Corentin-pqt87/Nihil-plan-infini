import sqlite3
from weasyprint import HTML

# 1. Connexion a la BDD SQLite
conn = sqlite3.connect('liste_sort')
cursor = conn.cursor()
cursor.execute("SELECT nom, niveau, type, combinable, temps_incantation, portee, composantes, duree, description FROM sort")
sorts = cursor.fetchall()

# 2. Construction du template HTML/CSS
html_content = """
<!DOCTYPE html>
<html>
<head>
<style>
  @page { size: A4 portrait; margin: 10mm; }
  body { font-family: sans-serif; margin: 0; display: flex; flex-wrap: wrap; gap: 5mm; }
  .card {
    width: 63mm;
    height: 88mm;
    border: 2mm solid #4a2e1b;
    border-radius: 4mm;
    padding: 3mm;
    box-sizing: border-box;
    background: #fdf6e7;
    page-break-inside: avoid;
    
    /* Permet de verrouiller la taille et d'activer le flexbox */
    display: flex;
    flex-direction: column;
    overflow: hidden; /* Empêche physiquement le texte de sortir */
    }

    .title { 
    font-size: 10pt; 
    font-weight: bold; 
    color: #2c1d11; 
    border-bottom: 1px solid #8b5a2b; 
    }

    .meta { 
    font-size: 7pt; 
    color: #5c4033; 
    margin-bottom: 2mm; 
    }

    .stats { 
    font-size: 6.5pt; 
    background: #eae0d0; 
    padding: 1.5mm; 
    border-radius: 2mm; 
    margin-bottom: 2mm; 
    flex-shrink: 0; /* Empêche les stats de s'écraser */
    }

    .desc { 
    font-size: 7pt; 
    line-height: 1.15; 
    flex-grow: 1; /* Occupe tout l'espace restant */
    overflow: hidden; 
    text-overflow: ellipsis; /* Ajoute "..." si ça dépasse vraiment trop */
    }
</style>
</head>
<body>
"""

for sort in sorts:
    nom, niveau, type_sort, combinable, temps, portee, comp, duree, desc = sort
    
    # Choix de la taille de police en fonction de la longueur de la description
    desc_len = len(desc) if desc else 0
    if desc_len > 400:
        desc_class = "desc font-xs"
    elif desc_len > 250:
        desc_class = "desc font-sm"
    else:
        desc_class = "desc"

    html_content += f"""
    <div class="card">
      <div class="title">{nom}</div>
      <div class="meta">Niveau {niveau} — {type_sort or 'Général'}</div>
      <div class="stats">
        <b>Temps:</b> {temps or '-'}<br/>
        <b>Portée:</b> {portee or '-'}<br/>
        <b>Composantes:</b> {comp or '-'}<br/>
        <b>Durée:</b> {duree or '-'}<br/>
        <b>Combinable:</b> {'Oui' if combinable else 'Non'}
      </div>
      <div class="{desc_class}">{desc}</div>
    </div>
    """

html_content += "</body></html>"

# 3. Export PDF
HTML(string=html_content).write_pdf("cartes_sorts_dnd.pdf")