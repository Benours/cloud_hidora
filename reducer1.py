import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys

results = {}
resultsdep = {}

for line in sys.stdin:
    line = line.strip()
    timbrecli, client, villecli, dep, qte = line.split(";")

    try:
        qte = int(qte)
    except ValueError:
        continue

    # Créer une clé unique pour chaque (client, ville, département)
    cle = (client, villecli, dep)

    # Mettre à jour le dictionnaire en incrémentant le compteur pour cette clé
    if cle in results:
        results[cle] += qte
    else:
        results[cle] = qte

    # Mettre à jour le dictionnaire des résultats par département
    if dep in resultsdep:
        resultsdep[dep] += qte
    else:
        resultsdep[dep] = qte

# Création d'un DataFrame à partir de results
results_df = pd.DataFrame(list(results.items()), columns=['Client_Ville_Dep', 'Total_Commandes'])

# Export des résultats vers un fichier Excel
results_excel_file = '/datavolume1/resultats.xlsx'
results_df.to_excel(results_excel_file, index=False)

# Créer un DataFrame à partir du dictionnaire des résultats par département
df = pd.DataFrame(list(resultsdep.items()), columns=['Département', 'Total'])

# Créer une nouvelle figure
plt.figure()

# Créer le graphe pie
plt.pie(df['Total'], labels=df['Département'], autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Assurer que le diagramme est circulaire
plt.title("Répartition des commandes par département")

# Enregistrer le graphe au format PDF
output_pdf_file = '/datavolume1/resultat.pdf'  # Chemin où le fichier PDF sera enregistré
with PdfPages(output_pdf_file) as pdf:
    pdf.savefig()  # Sauvegarder le graphe dans le fichier PDF
