def resteDe(n1, n2):
    resultats = [n1, n2]
    i = 0
    while resultats[i + 1] != 0:
        reste = resultats[i] % resultats[i + 1]
        resultats.append(reste)
        i += 1
    return resultats

def kaDe(n1, n2):
    if n2 == 0: return [0]  # Éviter la division par zéro

    restes = [n1, n2]
    k = [0, 0]
    i = 0
    while restes[i + 1] != 0:
        reste = restes[i] % restes[i + 1]
        ka = restes[i] // restes[i + 1]  
        restes.append(reste)
        k.append(ka)
        i += 1
    return k

def xDe(n1, n2):
    k = kaDe(n1, n2)
    if len(k) < 3: return []  # Gérer le cas où k est trop court

    x = [1, 0]
    for i in range(2, len(k) - 1):
        ix = x[i - 2] - k[i] * x[i - 1]
        x.append(ix)
    return x

def yDe(n1, n2):
    k = kaDe(n1, n2)
    if len(k) < 3: return []  # Gérer le cas où k est trop court

    y = [0, 1]
    for i in range(2, len(k) - 1):
        iy = y[i - 2] - k[i] * y[i - 1]
        y.append(iy)
    return y

def bezoutDe(n1, n2): 
    reste = resteDe(n1, n2)
    ka = kaDe(n1, n2)
    ix = xDe(n1, n2)
    yg = yDe(n1, n2)

    lin = len(ix) - 1
    bezout = [reste[lin], ix[lin], yg[lin]]
    return bezout

def create_table(n1, n2, format):
    reste = resteDe(n1, n2)
    ka = kaDe(n1, n2)
    ix = xDe(n1, n2)
    yg = yDe(n1, n2)

    if format == "latex":
        table = "\n\\begin{tabular}{llll}\n"
        table += "\\toprule\n"
        table += " $r$ & $x$ & $y$ & $L_n$\\\\\n" 
        table += "\\midrule\n"

        table += f" {reste[0]} & {ix[0]} & {yg[0]} & $L_1$\\\\\n" 
        table += f" {reste[1]} & {ix[1]} & {yg[1]} & $L_2$\\\\\n" 

        table += "\\midrule\n"
        # Remplissage du tableau avec les résultats
        for i in range(2, len(ix) - 1):
            r = reste[i]
            x = ix[i]
            y = yg[i]
            k = ka[i]
            if k == 1:
                table += f" {r} & {x} & {y} & $L_{{{i + 1}}} = L_{{{i - 1}}} - L_{{{i}}}$ \\\\\n"
            else :
                table += f" {r} & {x} & {y} & $L_{{{i + 1}}} = L_{{{i - 1}}} - {k}L_{{{i}}}$ \\\\\n"

        table += "\\midrule\n"

        lin = len(ix) - 1
        # table += " \\textbf{" + str(reste[lin]) + "} & \\textbf{"+ str(ix[lin])+"} & \\textbf{"+ str(yg[lin]) + "} & \\textbf{$L_"+ str(len(ix))+"= L_"+ str(len(ix) - 2)+" - "
        table += f" {str(reste[lin])} & {str(ix[lin])} & {str(yg[lin])} & $L_{str(len(ix))} = L_{str(len(ix) - 2)} - "

        # + str(ka[lin]) + "L_{"+ str(len(ix) - 1)+"}$ \\\\\n"

        if ka[len(ix) - 1] == 1:
            table += f"L_{str(len(ix) - 1)}$ \\\\\n"
        else :
            table += str(ka[lin]) + f"L_{str(len(ix) - 1)}$ \\\\\n"

        table += "\\bottomrule\n"
        table += "\\end{tabular}\n"

        # table += f"\nNous avons donc la relation de Bezout suivante : ${n1}({str(ix[lin])}) + {n2}({str(yg[lin])}) = ({n1};{n2}) = {reste[lin]}$\n"

        return table
    else:
        # Création d'une table pour la ligne de commande
        table = "r_n\tx\ty\tL_n\n"
        table += "-----------------------------\n"
        for i in range(len(reste)):
            r = reste[i]
            x = ix[i] if i < len(ix) else ''
            y = yg[i] if i < len(yg) else ''
            l = f"L_{i + 1}"
            if i > 0 and i < len(ka):
                k = ka[i]
                if i == 0 or i == 1:
                    l += ""
                else : 
                    l += f" = L_{i - 1} - {k}L_{i}" if k != 1 else f" = L_{i - 1} - L_{i}"
            table += f"{r:<4}\t{x:<4}\t{y:<4}\t{l}\n"
        return table

# Paramètres
dec = input("Voulez-vous utiliser les valeurs par défaut (n1=260, n2=57) ? Entrez 'oui' ou 'non': ")
if dec.lower() == "oui":
    n1 = 260
    n2 = 57
else:
    n1 = int(input("Entrer la valeur pour n1 : "))
    n2 = int(input("Entrer la valeur pour n2 : "))

deca = input("Voulez-vous créer un tableau ? Entrez 'oui' ou 'non': ")
format = input("Choisissez le format de sortie ('latex' (nécéssitant le package 'booktabs' pour les tableaux) ou 'cmd' pour ligne de commande): ")

bezout = bezoutDe(n1,n2)
table = create_table(n1, n2, format)

if deca.lower() == "oui":
    print(table)
elif format.lower() == "latex":
    print(f"\n${n1}\\cdot({bezout[1]}) + {n2}\\cdot({bezout[2]}) = {bezout[0]} = ({n1},{n2})$")
elif format.lower() == "cmd":
    print(f"\n{n1}*({bezout[1]}) + {n2}*({bezout[2]}) = {bezout[0]} = ({n1},{n2})")
