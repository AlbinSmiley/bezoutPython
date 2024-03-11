from base26 import coder, colerEn26, create_table_from_array, binary

# Définition des séquences de couleurs
RED = "\033[31m"  
GREEN = "\033[32m" 
BLUE = "\033[34m" 
ITALIC = "\033[3m"
RESET = "\033[0m"  

# Valeurs par défaut
nEx = 943
eEx = 21
stringEx ='jean est ici'

def get_user_input():
    response = input("Souhaitez-vous entrer de nouvelles valeurs ? (oui/non) : ").lower()
    if response in ['oui', 'o', 'yes', 'y']:
        n = int(input(f"Veuillez entrer la valeur pour le modulo {ITALIC}{GREEN}n{RESET} :     "))
        e = int(input(f"Veuillez entrer la valeur pour l'exposant {ITALIC}{GREEN}e{RESET} : "))
        string = input(f"Veuillez entrer une{ITALIC}{GREEN} chaine de caractère {RESET} :      ")
    else:
        if response not in ['non', 'n', 'no']:
            print("Réponse non reconnue. Utilisation de la valeur par défaut 'non'.")
        n, e, string = nEx, eEx, stringEx
    return n, e, string

def print_intro():
    print("Ceci est un programme permettant la cryptographie d'une chaine de caractère")
    print("Ce programme a besoin pour cela des valeurs suivantes (n,e) et d'une chaine de caractère (alphabétique uniquement)")
    print("Si vous ne souhaitez pas entrer de nouvelles valeurs il est possible de procéder à un exemple en utilisant les valeurs suivantes\n")
    print(f"{RED}\t({ITALIC}n,e{RESET}{RED}) = ({nEx},{eEx})")
    print(f'\tChaine de caractère = "{stringEx}"\n{RESET}')

def process_code(n, e, string):
    code = coder(n, e, string)
    bloc = code[0]
    groupes = '|'.join(code[1])
    numGroupes = [''.join([str(num).zfill(2) for num in subElement]) for subElement in code[2]]
    stringedNumGroupes = ' '.join(numGroupes)
    random = [' + '.join(item[::-1]) for item in map(colerEn26, numGroupes)]
    transposition = [f"{lettres} $\\rightarrow {element} = {code[3][i]}$" for i, (lettres, element) in enumerate(zip(code[1], random))]
    table = create_table_from_array(e, n, code[3])
    facteurs = ["\\cdot ".join(map(str, sous_liste)) for sous_liste in code[8]]
    modulation = [f'$ {code[3][i]}^{{{e}}}\\equiv {facteurs[i]}[{n}]\\equiv {code[9][i]}[{n}] $' for i in range(len(code[9]))]
    blabla = [' + '.join(item[::-1]) for item in map(colerEn26, code[10])]
    remodulation = [f'${code[9][i]} = {element} \\rightarrow $ {lettres}' for i, (lettres, element) in enumerate(zip(code[11], blabla))]
    return bloc, groupes, stringedNumGroupes, transposition, table, modulation, remodulation, code[12]

def crypto(n,e,string):
    beginning_latex_text = """\\documentclass[a4paper,12pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage[french]{babel}\n\\usepackage{array}\n\\usepackage{graphicx}\n\\usepackage{gensymb}\n\\usepackage{amsfonts}\n\\usepackage{MnSymbol}\n\\usepackage{booktabs}\n\\usepackage{amsthm}\n\n\\begin{document}"""
    end_latex_text = "\\end{document}"
    bloc, groupes, stringedNumGroupes, transposition, table, modulation, remodulation, coded_string = process_code(n, e, string)
    result = f'''{beginning_latex_text}\n\n$$26^{{{bloc}}} \\leq {n} < 26^{{{bloc+1}}}$$\nIl nous faut donc coder le message en blocs de {bloc}\n\n{groupes} $\\rightarrow$ {stringedNumGroupes}\n\n{'\n\n'.join(transposition)}\n\n$${e}={binary(e)}_{{(2)}}$$\n\n{table}\n\n{'\n\n'.join(modulation)}\n\n{'\n\n'.join(remodulation)}\n\n{string} codé de cette manière devient {coded_string}.\n\n{end_latex_text}''' 
    return result

def main():
    print_intro()
    n, e, string = get_user_input()
    print(crypto(n,e,string))

if __name__ == "__main__":
    main()


