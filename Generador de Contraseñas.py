import string, random, colorama
from colorama import *

# Algunos nombres de variables se encuentran mal escritos según la ortografía española (muchas palabras carecen de tildes, principalmente). 
# Estas faltas ortoráficas han sido realizados a propósito para evitar errores con el lenguaje de programación o editor de código.

colorama.init(autoreset = True)

# Se guardan en variables los caracteres que serán usados para la creación de contraseñas

texto = string.ascii_letters
numeros = string.digits
texto_numeros = texto + numeros
texto_numeros_simbolos = texto + numeros + string.punctuation

def generador_contraseñas():

    # Presentación del programa hacia el usuario

    print(); print(' Versión 1.0.0 - Emerald Development - Todos los derechos reservados')
    print(); print(Fore.BLUE + ' -> Generador de Contraseñas <-'); print()

    print(' > Modelos de contraseña:'); print()
    
    print(Fore.CYAN + '  1)', end = ''); print(' Texto (ABCabc...)')
    print(Fore.CYAN + '  2)', end = ''); print(' Números (123...)')
    print(Fore.CYAN + '  3)', end = ''); print(' Texto con números (Ab123)')
    print(Fore.CYAN + '  4)', end = ''); print(' Texto con números y símbolos (#Ab123)'); print()

    # El usuario escoje las características de su contraseña (combinación de caracteres y longitud)

    modelo = 0

    while modelo not in ('1', '2', '3', '4'):

        modelo = input(Fore.MAGENTA + ' >>> Selecciona un modelo de contraseña (1, 2, 3, 4): '); print()

    longitud = 0

    while int(longitud) < 4 or int(longitud) > 25:

        longitud = input(Fore.BLUE + ' >>> Selecciona una longitud para su contraseña (Mínimo 4 | Recomendado 13 - 25 | Máximo 25): '); print()

    # En función de las caracteristicas anteriores, el programa genera una contraseña

    contrasena = []

    if modelo == '1':

        # Contraseña de texto

        for i in range(int(longitud)):

            contrasena.append(random.choice(texto))

    elif modelo == '2':

        # Contraseña de números

        for i in range(int(longitud)):

            contrasena.append(random.choice(numeros))

    elif modelo == '3':

        # Contraseña de texto con números

        for i in range(int(longitud)):

            contrasena.append(random.choice(texto_numeros))

    else: 

        # Contraseña de texto, números y símbolos

        for i in range(int(longitud)):

            contrasena.append(random.choice(texto_numeros_simbolos))

    contrasena = ''.join(contrasena)

    # Contraseña generada | Se ofrece la contraseña generada al usuario

    print(Fore.CYAN + ' >>> Contraseña generada: ' + contrasena)

    print(); input(' >>> Pulse ENTER para cerrar el programa: ')

generador_contraseñas()
    






