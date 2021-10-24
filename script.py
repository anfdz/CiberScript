# Lectura fichero
f = open('file.txt', 'r')


# Funciones XOR
def toBinario(texto):
    res = []
    for n in texto:
        bits = bin(ord(n))[2:]
        while len(bits) < 8:
            bits = '0' + bits
        res.append(bits)

    return res


def toTexto(argumento):
    res = ''
    for i in argumento:
        x = int(i, 2)
        if x <= 32 or x >= 255:
            res += '.'
        else:
            res += chr(x)
    return res


def logicaXOR(argumento1, argumento2):
    if argumento1 == argumento2:
        return str(0)
    else:
        return str(1)


def XOR_OP(bint, binc):
    res = []
    i = 0
    for n in bint:
        if i == len(binc):
            i = 0
        z = binc[i]
        b = ''
        for x, y in zip(n, z):
            b += logicaXOR(x, y)
        i += 1
        res.append(b)
    return res


# Funciones Cesar
def Operacion_C_Cesar(clave, texto):
    res = ''
    for i in texto:
        e = ord(i)
        C=int
        if 65 <= e <= 90:
            C = e + (clave % 26)
            if C >= 91:
                C -= 26

        elif 97 <= e <= 122:
            C = e + (clave % 26)
            if C >= 123:
                C -= 26
        res += chr(C)

    return res


def Operacion_D_Cesar(clave, texto):
    res = ''
    C=int
    for i in texto:
        e = ord(i)
        if 65 <= e <= 90:
            C = e - (clave % 26)
            if C <= 64:
                C += 26

        elif 97 <= e <= 122:
            C = e - (clave % 26)
            if C <= 96:
                C += 26
        res += chr(C)

    return res


# Menu
def salir():
    print('\nApagando el programa...')


def xor():
    print('\nRealizando operacion xor\n...\n...\n...')
    clave = f.readline().rstrip('\n')
    texto = f.readline().rstrip('\n')

    bint = toBinario(texto)
    binc = toBinario(clave)

    res = XOR_OP(bint, binc)
    print('Resultado:')
    return toTexto(res)


def encriptar_CESAR():
    print('\nCifrando codigo Cesar\n...\n...\n...\nCodigo cifrado:')
    clave = int(f.readline().rstrip('\n'))
    texto = f.readline().rstrip('\n')

    return Operacion_C_Cesar(clave, texto)


def desencriptar_CESAR():
    print('\nDescifrando codigo Cesar\n...\n...\n...\nCodigo descifrado:')
    clave = int(f.readline().rstrip('\n'))
    texto = f.readline().rstrip('\n')

    return Operacion_D_Cesar(clave, texto)


def fbruta_CESAR():
    print('\nRealizando ataque por fuerza bruta\n...\n...\n...\n')
    texto = f.readline().rstrip('\n')

    for i in range(26):
        print(Operacion_D_Cesar(i, texto))


def error():
    print('Ha ocurrido un error')


switch = {
    0: salir,
    1: xor,
    2: xor,
    3: encriptar_CESAR,
    4: desencriptar_CESAR,
    5: fbruta_CESAR
}


def ejecutar(argument):
    func = switch.get(argument, error)
    return func()


menu = int
while menu != 0:
    print(
        'Elige una opción del menú: \n0.-Salir\n1.-Encriptar con XOR\n2.-Desencriptar con XOR\n3.-Encriptar con '
        'codigo CESAR\n4.-Desencriptar con codigo CESAR\n5.-Fuerza bruta a un cifrado CESAR')
    menu = int(f.readline().rstrip('\n'))
    res = ejecutar(menu)
    if res is not None:
        print(res)
