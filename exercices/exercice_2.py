"""
Créer une fonction qui affiche les 20 premiers termes
de la table de multiplication de 7.
7x1 = 7
7x2 = 14
[...]
7x20 = 140

BONUS :
Pouvoir rendre variable le nombre de terme
et la table choisie.
"""
def afficher_table_multiplication(nombre_terme, table):
    """
    Affiche sur le terminal la table de multiplication avec
    le nombre de terme choisie.
    :param nombre_terme: Nombre de terme.
    :param table: La table choisie.
    :return: None
    """
    for i in range(1, nombre_terme + 1):
        print(f"{table}x{i}={table*i}")

afficher_table_multiplication(10, 9)