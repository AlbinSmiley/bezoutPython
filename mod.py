def dividByTwo(nombre):
    resultats = []
    resultats.append(nombre)
    while nombre > 1:
        nombre //= 2
        resultats.append(nombre)
    return resultats

def binary(nombre):
    return bin(nombre)[2:]

def bibin(nombre):
    return [int(digit) for digit in binary(nombre)][::-1]

def modulo(base, modulo, nombre_de_termes):
    resultats = [base]
    for i in range(1, nombre_de_termes):
        resultats.append((resultats[i - 1] ** 2) % modulo)
    return resultats

# Fonction pour créer le tableau Markdown
def create_table(n, m, a):
    divisions = dividByTwo(n)
    nombre_de_termes = len(divisions)
    binary_representation = bibin(n)
    mod_results = modulo(a, m, nombre_de_termes)

    # En-têtes du tableau Markdown
    table = "\\begin{tabular}{llll}\n"
    table += "\\toprule\n"
    table += " $x$ & $r$ & $n$ & $" 
    table += f"{a}" 
    table += "^{2^{n}}" 
    table += f" [{m}]$ \\\\\n"
    table += "\\midrule\n"

    # Remplissage du tableau avec les résultats
    for i in range(len(divisions)):
        x = divisions[i]
        reste = binary_representation[i] if i < len(binary_representation) else ' '
        div_count = i
        mod_result = mod_results[i] if i < len(mod_results) else ' '
        table += f" {x} & {reste} & {div_count} & {mod_result} \\\\\n"

    table += "\\bottomrule\n"
    table += "\\end{tabular}\n"
    return table

# Paramètres
dec = input("Voulez-vous faire un essai tel que pour la relation suivante $ x == a^n[m] $ ? (si oui, entrer << oui >>, sinon << non >>)\n a = 101, n = 149, m = 151 \n" )

if (dec == "oui"):
    a = 101
    n = 149
    m = 151 
else : 
    n = int(input("Entrer la puissance : "))
    m = int(input("Entrer le modulo :    "))
    a = int(input("Entrer la base :      "))

# Création du tableau Markdown
table = create_table(n, m, a)
print(table)
table.split('\n')  # Split pour une meilleure visualisation dans la sorti
