""" on importe les librairies utiles au développement de la fonction"""

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename> sous forme de liste d'entiers"""
    with open(filename, mode = 'r', encoding = 'utf8') as file:
        lignes = file.readlines()
    l = [list(map(int, line.strip().split(';'))) for line in lignes]
    return l

def get_list_k(data, k):
    """ on retourne la k_ieme liste du fichier data"""
    return data[k]

def get_first(l):
    """on retourne la première liste du fichier"""
    return l[0]

def get_last(l):
    """on retourne la dernière liste du fichier"""
    return l[-1]

def get_max(l):
    """on retourne la liste ayant des valeurs maximales du fichier"""
    return max(l)

def get_min(l):
    """on retourne la liste ayant des valeurs minimales du fichier"""
    return min(l)

def get_sum(l):
    """on retourne la somme des listes du fichier"""
    return sum(l)


#### Fonction principale


def main():
    """on fait appel aux fonctions secondaires grâce à la fonction main"""
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
