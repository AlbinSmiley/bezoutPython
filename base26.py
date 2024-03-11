import random
import string

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

def exponentiationDe(n,m,a):
    divisions = dividByTwo(n)
    nombre_de_termes = len(divisions)
    binary = bibin(n)
    mod_results = modulo(a, m, nombre_de_termes)
    result = [divisions,binary,list(range(nombre_de_termes)),mod_results]
    return result

def facteurs_premiers(n):
    i = 2
    facteurs = set()
    while i * i <= n:
        while n % i == 0:
            facteurs.add(i)
            n //= i
        i += 1
    if n > 1:
        facteurs.add(n)
    return list(facteurs)

def phi(n):
    facteursPremiers = facteurs_premiers(n)
    result = 1
    for p in facteursPremiers : 
        result *= (1-(1/p))
    return int(result*n)

def blocsDe(n, base=26):
    i = 0
    while base**i <= n: 
        i += 1
    return i - 1

def diviser_en_sous_listes(liste, n):
    # Utilise une compréhension de liste pour créer les sous-listes
    sous_listes = [liste[i:i + n] for i in range(0, len(liste), n)]
    return sous_listes

def ajuster_chaine(chaine, n):
    # Convertit la chaîne en liste de caractères
    liste_caracteres = list(chaine)
    
    # Calcule le nombre de caractères manquants pour atteindre un multiple de n
    manque = len(liste_caracteres) % n
    if manque != 0:
        caracteres_a_ajouter = n - manque
    else:
        caracteres_a_ajouter = 0
    
    # Ajoute des lettres aléatoires si nécessaire
    for _ in range(caracteres_a_ajouter):
        liste_caracteres.append(random.choice(string.ascii_letters))
    
    return liste_caracteres

def lettre_vers_numero(chaine):
    numeros = []
    for caractere in chaine:
        if 'a' <= caractere <= 'z':  # Pour les lettres minuscules
            numero = ord(caractere) - ord('a')
            numeros.append(numero)
        elif 'A' <= caractere <= 'Z':  # Pour les lettres majuscules
            numero = ord(caractere) - ord('A')
            numeros.append(numero)
        else:
            # Gère le cas où le caractère n'est pas une lettre
            numeros.append(None)  # Ou tout autre valeur/indicateur de votre choix
    return numeros

def numero_vers_lettre(numeros, majuscule=False):
    lettres = []
    for numero in numeros:
        if 0 <= numero <= 25:  # Assure que le numéro est dans l'intervalle valide pour les lettres
            if majuscule:
                # Convertit le numéro en lettre majuscule
                lettres.append(chr(numero + ord('A')))
            else:
                # Convertit le numéro en lettre minuscule
                lettres.append(chr(numero + ord('a')))
        else:
            # Gère le cas où le numéro n'est pas dans l'intervalle d'une lettre
            lettres.append(None)  # Ou toute autre valeur/indicateur de votre choix
    return ''.join(lettres)  # Retourne une chaîne de caractères formée des lettres

def toNormalNumbers(chaine,n):
    liste_ajustee = ajuster_chaine(chaine,n)
    char = ''.join(liste_ajustee)
    numbers = lettre_vers_numero(char)
    result = diviser_en_sous_listes(numbers,n)
    return result

def enBase26(array):
    result = [0] * len(array)  # Initialise result avec des zéros pour chaque sous-liste
    for i in range(len(array)):
        length = len(array[i])
        for j, number in enumerate(array[i]):
            puissance = length - j - 1  # Calcule la puissance correcte pour chaque position
            result[i] += number * (26 ** puissance)
    return result

def div(n,m,a):
    expo = exponentiationDe(n, m, a)
    # resultat_moduler = exponentiationDe(puissance, modulo, base)
    result = expo[0]
    return result 

def reste(n,m,a):
    expo = exponentiationDe(n, m, a)
    # resultat_moduler = exponentiationDe(puissance, modulo, base)
    result = expo[1]
    return result 

def index(n,m,a):
    expo = exponentiationDe(n, m, a)
    # resultat_moduler = exponentiationDe(puissance, modulo, base)
    result = expo[2]
    return result 

def expo(n,m,a):
    expo = exponentiationDe(n, m, a)
    # resultat_moduler = exponentiationDe(puissance, modulo, base)
    result = expo[3]
    return result 

def facteursExponant(n, m, a):
    # puissance,modulo,base
    # Appel de la fonction exponentiationDe pour obtenir ses résultats
    expo = exponentiationDe(n, m, a)
    # resultat_moduler = exponentiationDe(puissance, modulo, base)
    length = len(expo[0])
    result = []
    
    # Extraction des sous-listes nécessaires
    for i in range(length) :
        if expo[1][i] == 1 :
            result.append(expo[3][i])

    return result[::-1]

def moduler(m, array):
    result = 1
    for element in array: 
        result *= element
    return result % m

def enBaseDe(n, base = 26):
    p = 0
    result = []
    while base**p <= n :
        p += 1

    while base**p >= 1 :
        result.append((n//base**p) % base)
        p -= 1
    return result

def colerEn26(array):
    array[::-1]
    result = [0] * len(array)  # Initialise result avec des zéros pour chaque sous-liste
    for i in range(len(array)):
        if i != 0 :
            result[i] = str(array[i]) + '\\cdot 26^{' + str(i) + '}'
        else :
            result[i] = str(array[i])
    return result

def coder(modulo, exponent, chaine, base = 26):
    chaine = chaine.replace(" ", "")
    chaine = chaine.upper()
    result = []
    bloc = blocsDe(modulo, base)
    groupe = diviser_en_sous_listes(chaine, bloc)
    nums = toNormalNumbers(chaine, bloc)
    bases = enBase26(nums)
    basesEnFacteurs = []
    for element in bases : 
        basesEnFacteurs.append(facteursExponant(exponent, modulo, element))
    division = div(exponent, modulo, bases[0])
    restes = reste(exponent, modulo, bases[0])
    indice = index(exponent, modulo, bases[0])
    exponentiation = []
    for element in bases : 
        exponentiation.append(expo(exponent, modulo, element))
    basesModulé = []
    for element in basesEnFacteurs : 
        basesModulé.append(moduler(modulo, element))
    basesEn26 = []
    for element in basesModulé : 
        basesEn26.append(enBaseDe(element)[-(bloc + 1):])
    basesEnLettre = []
    for element in basesEn26:
        basesEnLettre.append(numero_vers_lettre(element).upper())
    chaine = ''.join(basesEnLettre)
    result.append(bloc)
    result.append(groupe)
    result.append(nums)
    result.append(bases)
    result.append(division)
    result.append(restes)
    result.append(indice)
    result.append(exponentiation)
    result.append(basesEnFacteurs)
    result.append(basesModulé)
    result.append(basesEn26)
    result.append(basesEnLettre)
    result.append(chaine)
    return result

def decoder(modulo, exponent, chaine, base = 26):
    chaine = chaine.replace(" ", "")
    chaine = chaine.upper()
    result = []
    bloc = blocsDe(modulo, base) + 1
    groupe = diviser_en_sous_listes(chaine, bloc)
    nums = toNormalNumbers(chaine, bloc)
    bases = enBase26(nums)
    basesEnFacteurs = []
    for element in bases : 
        basesEnFacteurs.append(facteursExponant(exponent, modulo, element))
    division = div(exponent, modulo, bases[0])
    restes = reste(exponent, modulo, bases[0])
    indice = index(exponent, modulo, bases[0])
    exponentiation = []
    for element in bases : 
        exponentiation.append(expo(exponent, modulo, element))
    basesModulé = []
    for element in basesEnFacteurs : 
        basesModulé.append(moduler(modulo, element))
    basesEn26 = []
    for element in basesModulé : 
        basesEn26.append(enBaseDe(element)[-(bloc - 1):])
    basesEnLettre = []
    for element in basesEn26:
        basesEnLettre.append(numero_vers_lettre(element).upper())
    chaine = ''.join(basesEnLettre)
    result.append(bloc)
    result.append(groupe)
    result.append(nums)
    result.append(bases)
    result.append(division)
    result.append(restes)
    result.append(indice)
    result.append(exponentiation)
    result.append(basesEnFacteurs)
    result.append(basesModulé)
    result.append(basesEn26)
    result.append(basesEnLettre)
    result.append(chaine)
    return result

def create_table_from_array(n, m, array):
    divisions = dividByTwo(n)
    length = len(divisions)
    binary_representation = bibin(n)
    mod_results = [modulo(element, m, length) for element in array]
    mod_results_transposé = [list(i) for i in zip(*mod_results)]
    mod_results_ts = [str(element) for element in mod_results_transposé]
    # table = mod_results

    
    head = 'l' * len(array)
    table = "\\begin{tabular}{lll" + head
    table +="}\n"
    table += "\\toprule\n$x$ & $r$ & $n$ & " 
    i = 0
    while i < len(array) - 1: 
        table += f"${array[i]}" 
        table += "^{2^{n}}" 
        table += f" [{m}]$ & "
        i += 1
    table += f"${array[i]}" 
    table += "^{2^{n}}" 
    moduloS = " ["+ str(m) +"] "
    # moduloS2 = moduloS + "& "
    table += moduloS + "$\\\\\n"
    table += "\\midrule\n"

    mod_ligne = ['$' + '$ & $'.join(map(str, sous_liste)) + '$' for sous_liste in mod_results_transposé]

    # Remplissage du tableau avec les résultats
    for i in range(len(divisions)):
        x = divisions[i]
        reste = binary_representation[i]
        div_count = i
        ligne = mod_ligne[i]
        table += f" {x} & {reste} & {div_count} & {ligne} \\\\\n"

    table += "\\bottomrule\n"
    table += "\\end{tabular}\n"
    return table

# [2, ['JE', 'AN', 'ES', 'TI', 'CI'], [[9, 4], [0, 13], [4, 18], [19, 8], [2, 8]], [238, 13, 122, 502, 60], [21, 10, 5, 2, 1], [ 1, 0, 1, 0, 1], [0, 1, 2, 3, 4], [[238, 64, 324, 303, 338], [13 , 169, 271, 830, 510], [122, 739, 124, 288, 903], [502, 223, 69 3, 262, 748], [60, 771, 351, 611, 836]], [[338, 324, 238], [510 , 271, 13], [903, 124, 122], [748, 693, 502], [836, 351, 60]], [279, 315, 286, 707, 350], [[0, 10, 19], [0, 12, 3], [0, 11, 0] , [1, 1, 5], [0, 13, 12]], ['AKT', 'AMD', 'ALA', 'BBF', 'ANM'], 'AKTAMDALABBFANM']
