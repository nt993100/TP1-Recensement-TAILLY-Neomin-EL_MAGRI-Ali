import csv 
import matplotlib.pyplot as plt  

# Définit une fonction pour lire la population d'un département dans un fichier CSV
def lire_population(f, sep=',', col_dept=2, col_pop=9, dept='89'):
    with open(f, newline='', encoding='utf-8') as csvfile:
        # Calcule la somme de la population pour un département donné
        return sum(float(row[col_pop]) for row in csv.reader(csvfile, delimiter=sep) if row[col_dept] == dept)

# Liste des fichiers CSV avec leurs années et paramètres spécifiques
fichiers = [
    ('donnees_2008.csv', 2008), 
    ('donnees_2016.csv', 2016),
    ('donnees_2021.csv', 2021, ';', 1, 5), 
    ('donnees_2023.csv', 2023, ';', 2, 10)
]

# Fonction pour tracer le diagramme de population
def tracer_population(fichiers):
    # Calcule les populations pour chaque fichier
    populations = [lire_population(*f[:1], *f[2:] if len(f) > 2 else ()) for f in fichiers]
    # Extrait les années
    années = [f[1] for f in fichiers]
    
    # Crée une figure avec une taille spécifique
    plt.figure(figsize=(10, 6))
    # Trace un diagramme à barres
    plt.bar(années, populations, color='r', edgecolor='black')
    # Définit le titre du graphique
    plt.title("Évolution de la population dans l'Yonne")
    # Étiquette de l'axe des x
    plt.xlabel("Année")
    # Étiquette de l'axe des y
    plt.ylabel("Population")
    # Ajoute une grille sur l'axe y
    plt.grid(axis='y')
    
    # Ajoute les valeurs de population au-dessus de chaque barre
    for i, pop in enumerate(populations):
        plt.text(années[i], pop, f'{pop:,.0f}', ha='center', va='bottom')
    
    # Ajuste automatiquement la disposition du graphique
    plt.tight_layout()
    # Affiche le graphique
    plt.show()

# Appelle la fonction pour tracer le diagramme
tracer_population(fichiers)