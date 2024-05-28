s = [9,1,4,2,5]
def minimo (s:list) -> int:
    numero = s[0]
    for i in s:
        if i < numero:
            numero = i
    return numero

def eliminar (e,s):
    lista = []
    for i in s:
        if e != i:
            lista.append(i)
    return lista


def ordenados (s:list) -> bool:
    long = len(s)
    lista = []
    for i in s:
        lista.append(i)
    nueva = []
    for i in range(long):
        nueva.append(minimo(lista))
        lista.remove(minimo(lista))
    return nueva

print(ordenados(s))


palabra = ""
def palindromo (palabra:str) -> bool:
    res = False
    if palabra == alReves(palabra):
        res = True
    return res

def alReves (palabra:str) -> str:
    longitud = ((-len(palabra))-1)
    palabraNueva = ""
    for i in range(-1,longitud,-1):
        palabraNueva += palabra[i]
    return palabraNueva

print(palindromo(palabra))

def hayMinuscula (contraseña:str) -> bool:
    res = False
    for i in contraseña:
        if (i >= "a") and (i <= "z"):
            res = True
    return res    

def hayMayuscula (contraseña:str) -> bool:
    res = False
    for i in contraseña:
        if (i >= "A") and (i <= "Z"):
            res = True
    return res    

def hayNumeros (contraseña:str) -> bool:
    res = False
    for i in contraseña:
        if (i >= "0") and (i <= "9"):
            res = True
    return res    

def contraseña (palabra:str) -> str:
    longitud = len(palabra)
    if longitud < 5:
        return "ROJA"
    elif (longitud > 8) and hayMayuscula(palabra) and hayMinuscula(palabra) and hayNumeros(palabra):
        return "VERDE"
    else:
        return "AMARILLA"

print(contraseña("ejidej32"))

def cuentaBancaria (tupla:list) -> int:
    suma = 0
    for i in tupla:
        if "I" == i[0]:
            suma += i[1]
        else:
            suma -= i[1]
    return suma

print(cuentaBancaria( [("I",2000), ("R", 20),("R", 1000),("I", 300)]))

def vocales (palabra:str) -> bool:
    res = False
    contador = 0
    vocales = "aeiou"
    for i in vocales:
        if i in palabra or i.upper() in palabra:
            contador += 1
    if contador >= 3:
        res = True
    return res

print(vocales("kslAEI"))


def ceros (numeros:list) -> list:
    for i in range(len(numeros)):
        if (i % 2) == 0:
            numeros[i] = 0
    return numeros
        
print(ceros([1]))


def ceros1 (numeros:list) -> list:
    lista = []
    for i in range(len(numeros)):
        if (i % 2) != 0:
            lista.append(numeros[i])
        else:
            lista.append(0)
    return lista
print(ceros1([1]))

def sinVocales (cadena:str) -> str:
    vocales = "aeiou"
    nuevo = ""
    for i in cadena:
        if i.lower() not in vocales:
            nuevo += i
    return nuevo

print(sinVocales("ejdIejediAEI"))

def reemplazaVocales (char:[chr]) -> [chr]:
    lista = []
    vocalesMIn = "aeiou"
    vocalesMay = "AEIOU"
    for i in char:
        if i in vocalesMIn or i in vocalesMay:
            lista.append('')
        else:
            lista.append(i)
    return lista

print(reemplazaVocales(['e','s','i','A']))

def daVueltaStr (char:[chr]) -> [chr]:
    lista = []
    long = len(char)
    for i in range(-1,-long-1,-1):
        lista.append(char[i])
    return lista

print(daVueltaStr(['s','a','r','o']))


def eliminarRepetidos (s:[chr]) -> [chr]:
    lista = []
    for i in s:
        if i not in lista:
            lista.append(i)
    return lista

# print(eliminarRepetidos(['e','r',"r"]))

def promedio (notas:[int]) -> int:
    suma = 0
    cantidad = 0
    for i in notas:
        suma += i
        cantidad += 1
    promedio = suma / cantidad
    return promedio

def aprobado (notas:[int]) -> int:
    for i in notas:
        if i < 4:
            return 3
    if promedio(notas) < 4:
        return 3
    elif promedio(notas) >= 4 and promedio(notas) < 7:
        return 2
    else:
        return 1

# print(aprobado([4,5,6,5,6,6]))

def listaDeEstudiantes()->[str]:
    res:[str]=[]
    alumno = input("Ingresar alumno: ")
    while alumno != "Listo":
        res.append(alumno)
        alumno = input("Ingresar alumno: ")
    return res


# print(listaDeEstudiantes())
import random
def historial() -> list:
    suma = 0
    lista = []
    operacion = input("Ingresar operacion: ")
    while operacion != "X":
        monto = int(input("Ingresar monto: "))
        lista.append((operacion,monto))
        if operacion == "C":
            suma += monto
        if operacion == "D":
            suma -= monto
        operacion = input("Ingresar operacion: ")
    print(suma)
    return lista

# print(historial())

def perteneceACadaUno(l:list, e:int):
    res = []
    for i in l:
        if e in i:
            res.append(True)
        else:
            res.append(False)
    return res

# print(perteneceACadaUno([],3))

def esMatriz (matriz:list) -> bool:
    if len(matriz) == 0 or matriz[0] == []:
        return False
    long = len(matriz[0])
    res = True
    for i in matriz:
        if len(i) != long:
            res = False
    return res

# print(esMatriz([[2,3,1],[3,2,41],[]]))

def ordenadas (m:list) -> bool:
    res = True
    primero = m[0]
    for i in m:
        if primero > i:
            res = False
        primero = i
    return res


def filasOrdenadas (m:list) -> bool:
    res = True
    for i in m:
        if ordenadas(i) != True:
            res = False
    return res

m = [[5,2,3,4,5],[2,3,4,5,6],[1,2,3,4,5]]

print(filasOrdenadas(m))
        
def sieteYmedio ():
    numeros = [0,1,2,3,4,5,6,7,10,11,12]
    lista = []
    suma = 0
    carta = random.choice(numeros)
    numeros.remove(carta)
    print(carta)
    lista.append(carta)
    if carta <= 7:
        suma += carta
    else:
        suma += 0.5
    preguntar = input("Seguir Jugando: ")
    while preguntar != "No":
        carta = random.choice(numeros)
        numeros.remove(carta)
        lista.append(carta)
        print(carta)
        if carta <= 7:
            suma += carta
        else:
            suma += 0.5
        if suma > 7.5:
            print("Perdiste")
            return lista
        preguntar = input("Seguir Jugando: ")
    return lista

print(sieteYmedio())
