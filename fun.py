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
