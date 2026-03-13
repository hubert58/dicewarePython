import secrets
import sys

def main(nom_fichier):
    with open(nom_fichier, "r", encoding="utf-8") as file :
        tab = file.readlines()
    n = secrets.randbelow(len(tab))
    return tab[n].strip()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fichier_choisi = sys.argv[1]
        try:
            s = ""
            for i in range(5):
                s += main(fichier_choisi) + "-"
            s = s[:-1]
            print(s)
        except FileNotFoundError:
            print(f"Erreur : Le fichier '{fichier_choisi}' est introuvable.")
    else:
        print("Erreur : Il manque le nom du fichier. Exemple : python search.py mon_fichier.txt")