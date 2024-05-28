def contar_lineas (archivo:str) -> int:
    abrir = open(archivo)
    texto = abrir.readlines()
    lineas = len(texto)
    return lineas


# print(contar_lineas("himno.txt"))

def existe_palabra(palabra:str, nombre_archivo:str) -> bool:
    res = False
    abrir = open(nombre_archivo)
    texto = abrir.read()
    separado = texto.split()
    for i in separado:
        if i == palabra:
            res = True
    return res

# print(existe_palabra("juremos","himno.txt"))


def cantidad_apariciones(nombre_archivo:str,palabra:str) -> int:
    contador = 0
    abrir = open(nombre_archivo)
    texto = abrir.read()
    separado = texto.split()
    for i in separado:
        if i == palabra:
            contador += 1
    return contador

# print(cantidad_apariciones("himno.txt","juremos"))


# def clonar_sin_comentarios(nombre_archivo:str):
#     lineas = open(nombre_archivo)
#     archivo = lineas.readlines()
#     archivo_nuevo = open("himno1.txt","w")
#     comentario = open("himno1.txt", "a")
#     for i in archivo:
#         if (i[0] != "#"):
#             comentario.write(i)
#             if (i[0] == " ") and ("#" not in i):
#                 comentario.write(i) 
#     return archivo_nuevo

# print(clonar_sin_comentarios("himno.txt"))


def reverso (nombre_archivo:str):
    abrir = open(nombre_archivo)
    lineas = abrir.readlines()
    archivo_nuevo = open("reverso1.txt","w")
    comentario = open("reverso1.txt", "a")
    texto = reversoAux(lineas)
    for i in texto:
        comentario.write(i)
    return archivo_nuevo

def reversoAux (texto:list) -> list:
    long = (-len(texto))
    lista = []
    for i in range(-1,long-1,-1):
        lista.append(texto[i])
    return lista

# print(reverso("reverso.txt"))


def agregarFinal (archivo,comentario):
    agregar = open(archivo,"a")
    agregar.write(comentario + "\n")
    return agregar

# print(agregarFinal("himno.txt","uuhuh"))


def idem (archivo,comentario):
    abrir = open(archivo)
    lineas = abrir.readlines()
    textoAgregado = [comentario + "\n"] + lineas
    archivo_limpio = open(archivo, "w")
    for i in textoAgregado:
        archivo_limpio.write(i)
    abrir.close()
    return archivo

idem("himno.txt","hola")

import random
from queue import LifoQueue as Pila
from queue import Queue as Cola
# p = Pila ()
# p.put () # apilar
# elemento = p.get () # desapilar
# p.empty () # vacia ?

def generar_nros_al_azar(n:int,desde:int,hasta:int) -> Pila:
    p = Pila()
    for i in range(n):
        aleatorio = random.randint(desde,hasta)
        p.put(aleatorio)
    return p

# print(generar_nros_al_azar(4,30,40))


# def cantidad_elementos(p:Pila) -> int: 
#     lista = []
#     contador = 0
#     while not p.empty():
#         lista.append(p.get())
#         contador += 1
#     for i in lista[::-1]:
#         p.put(i)
#     return contador

p = Pila()
p.put(2)
p.put(4)
p.put(1)
[2,4,1]

c = Cola()
c.put(2)
c.put(4)
c.put(1)
[2,4,1]

listaP = [1,4,2]
while not p.empty():
    sacarP = p.get()
    listaP.append(sacarP)

listaC = [2,4,1]
while not c.empty():
    sacarC = c.get()
    listaC.append(sacarC)

[1,4,2]
for i in listaP:
    p.put(i)

[2,4,1]
for i in listaC:
    c.put(i)

# print(cantidad_elementos(p))

def buscar_el_maximo(p:Pila) -> int:
    lista = []
    while not p.empty():
        lista.append(p.get())
    maximo = lista[0]
    for i in lista:
        if i > maximo:
            maximo = i
    return maximo

# p = Pila()
# p.put(4)
# p.put(2)
# p.put(1)

# print(buscar_el_maximo(p))



def esta_bien_balanceada(s:str) -> bool:
    res = True
    p = Pila()
    for i in s[::-1]:
        p.put(i)
    contador = 0
    while not p.empty():
        parentesis = p.get()
        if parentesis == "(":
            contador += 1
        if parentesis == ")":
            contador -= 1
    if contador != 0:
        res = False
    return res        

# print(esta_bien_balanceada ("1 + ) 2 x 3 ( ( )"))


def postfix (expresion:str) -> int:
    operadores = ["+","-","*","/"]
    separado = expresion.split(" ")
    p = Pila()
    for i in separado:
        if i not in operadores:
            p.put(i)
        elif i in operadores:
            n2 = int(p.get())
            n1 = int(p.get())
            if i == "+":
                resultado = n1 + n2
                p.put(resultado)
            if i == "-":
                resultado = n1 - n2
                p.put(resultado)
            if i == "*":
                resultado = n1 * n2
                p.put(resultado)
            if i == "/":
                resultado = n1 / n2
                p.put(resultado)
    return p.get()

# print(postfix("3 4 + 5 * 2 -"))


# from queue import Queue as Cola

# def generar_nros_al_azar(n:int,desde:int,hasta:int) -> Cola:
#     c = Cola()
#     for i in range(n):
#         aleatorio = random.randint(desde,hasta)
#         p.put(aleatorio)
#     return c


def cantidad_elementos(c:Cola) -> int:
    lista = []
    contador = 0
    while not c.empty():
        lista.append(c.get())
        contador += 1
    for i in lista[::-1]:
        c.put(i)
    return contador

# c = Cola()
# c.put(1)
# c.put(4)
# c.put(3)

# print(cantidad_elementos(c))


def buscar_el_maximo(c:Cola) -> int:
    lista = []
    while not c.empty():
        lista.append(c.get())
    maximo = lista[0]
    for i in lista:
        c.put(i)
        if i > maximo:
            maximo = i
    return maximo

# print(buscar_el_maximo(c))

carton = [0,10,20,34,46,55,62,71,89,94,11,12]
def armar_secuencia_de_bingo() -> Cola:
    c = Cola()
    lista = []
    for i in range(100):
        lista.append(i)
    random.shuffle(lista)
    for i in lista:
        c.put(i)
    return c

def jugar_carton_de_bingo(carton:list,bolillero:Cola) -> int:
    contador = 0
    jugadas = 0
    lista = []
    while contador < 12:
        bolilla = bolillero.get()
        lista.append(bolilla)
        if bolilla in carton:
            contador += 1
        jugadas += 1
    return jugadas

# print(jugar_carton_de_bingo(carton,armar_secuencia_de_bingo()))

def n_pacietes_urgentes (c:Cola) -> int:
    contador = 0
    lista = []
    while not c.empty():
        paciente = c.get()
        lista.append(paciente)
        if paciente[0][0] <= 3:
            contador += 1
    c = Cola()
    for i in lista:
        c.put(i)
    return contador

# c = Cola()
# c.put([(3,"Juan","traumotoeee")])
# c.put([(2,"Juan","traumotoeee")])
# c.put([(6,"Juan","traumotoeee")])
# c.put([(8,"Juan","traumotoeee")])
# c.put([(1,"Juan","traumotoeee")])
# print(n_pacietes_urgentes(c))

def a_clientes (c:Cola) -> Cola:
    colaAux = []
    ninguno = []
    preferencial = []
    prioridad = []
    while not c.empty():
        cliente = c.get()
        colaAux.append(cliente)
        if cliente[0][3] == True:
            prioridad.append(cliente) 
        if (cliente[0][2] == True) and (cliente[0][3] == False):
            preferencial.append(cliente)
        if (cliente[0][2] == False) and (cliente[0][3] == False):
            ninguno.append(cliente)
    for i in colaAux:
        c.put(i)
    total = prioridad + preferencial + ninguno
    colaOrdenada = Cola()
    for i in total:
        colaOrdenada.put(i)
    return colaOrdenada

fila = Cola()
fila.put([("Juan",39550231,False,False)])
fila.put([("sergio",43494959,True,False)])
fila.put([("luis",23494959,False,True)])
fila.put([("pedro",42444559,True,True)])
fila.put([("thiago",39230231,False,False)])
fila.put([("gaston",59550231,True,False)])
fila.put([("carlos",39550421,False,True)])
fila.put([("sebastian",29013432,True,True)])
fila.put([("raul",45494959,False,False)])
fila.put([("mario",38091754,True,False)])
fila.put([("santiago",36550231,False,True)])
fila.put([("franco",31550231,True,True)])

print(a_clientes(fila))


def agrupar_por_longitud(nombre_archivo:str) -> dict:
    diccionario = {}
    archivo = open(nombre_archivo,"r")
    texto = archivo.read()
    palabras = texto.split()
    lista = []
    for i in palabras:
        lista.append(len(i))
    long = len(lista)
    lista_nueva = []
    for i in range(long):
        lista_nueva.append(minimo(lista))
        lista.remove(minimo(lista))
    for palabra in lista_nueva:
        if palabra not in diccionario:
            contador = 0
            for i in lista_nueva:
                if palabra == i:
                    contador += 1
            diccionario[palabra] = contador
    return diccionario

def minimo(palabras:list):
    minimo = palabras[0]
    for i in palabras:
        if i < minimo:
            minimo = i
    return minimo

def eliminar (minimo,palabras):
    lista = []
    for i in palabras:
        if i != minimo:
            lista.append(i)
    return lista
        

# print(agrupar_por_longitud("himno.txt"))


def promedioEstudiante(lu:str) -> float:
    lineas = open("notas.csv","r")
    texto = lineas.read()
    espacio = texto.split()
    lista = []
    for i in espacio:
        lista.append(i.split(","))
    long = len(lista)
    suma = 0
    cantidad = 0
    for i in range(long):
        if lista[i][0] == lu:
            suma += int(lista[i][3])
            cantidad += 1
    if cantidad == 0:
        return 0
    promedio = suma/cantidad
    return promedio

# print(promedioEstudiante("242"))


def promedios (archivo:str) -> dict:
    diccionario = {}
    lineas = open(archivo,"r")
    texto = lineas.read()
    espacio = texto.split()
    separadoEnComas = []
    for i in espacio:
        separadoEnComas.append(i.split(","))
    longitud = len(separadoEnComas)
    sinRepetidos = []
    for i in range(longitud):
        lu = separadoEnComas[i][0]
        if lu not in sinRepetidos:
            sinRepetidos.append(lu)
    for i in sinRepetidos:
        diccionario[i] = promedioEstudiante(i)
    return diccionario
# print(promedios("notas.csv"))


def n_la_palabra_mas_frecuente(nombre_archivo:str) -> str:
    diccionario = {}
    lineas = open(nombre_archivo,"r")
    texto = lineas.read()
    palabrasRepetidas = texto.split()
    SinRepetir = []
    for i in palabrasRepetidas:
        if i not in SinRepetir:
            SinRepetir.append(i)
    for palabra in SinRepetir:
        contador = 0
        for i in palabrasRepetidas:
            if palabra == i:
                contador += 1
        diccionario[palabra] = contador
    valores = list(diccionario.values())
    maximo = max(valores)
    maximas = []
    for clave,valor in diccionario.items():
        if maximo == valor:
            maximas.append(clave)
    return maximas

def max (lista:list) -> int:
    maximo = lista[0]
    for i in lista:
        if i > maximo:
            maximo = i
    return maximo

# print(n_la_palabra_mas_frecuente("himno.txt"))


historiales = {}

def visitar_sitio(historiales, usuario, sitio):
    if usuario not in historiales:
        historiales[usuario] = (Pila(),Pila())
    historial = historiales[usuario]
    historial[0].put(sitio)

def navegar_atras(historiales, usuario):
    historial = historiales[usuario]
    ultimo = historial[0].get()
    historial[1].put(ultimo)

def navegar_adelante(historiales, usuario):
    historial = historiales[usuario]
    ultimo = historial[1].get()
    historial[0].put(ultimo)

visitar_sitio (historiales,"usuario2","youtube.com")
visitar_sitio (historiales,"usuario2","facebook.com")
visitar_sitio (historiales,"usuario2","uba.com")
visitar_sitio (historiales,"usuario2","tiktok.com")
navegar_atras(historiales, "usuario2")
navegar_adelante(historiales, "usuario2")

# print(historiales)


inventario = {}

def agregar_producto (inventario,nombre,precio,cantidad):
    if nombre not in inventario:
        inventario[nombre] = {}
        valores = inventario[nombre]
        valores["Precio"] = precio
        valores["Cantidad"] = cantidad

def actualizar_stock (inventario, nombre, cantidad):
    if nombre in inventario:
        inventario[nombre]["Cantidad"] = cantidad

def actualizar_precios(inventario, nombre, precio):
    if nombre in inventario:
        inventario[nombre]["Precio"] = precio
    
def calcular_valor_inventario(inventario):
    total = 0
    for i in inventario:
        precio = inventario[i]["Precio"]
        cantidad = inventario[i]["Cantidad"]
        multiplicacion = precio * cantidad
        total += multiplicacion
    return total

agregar_producto(inventario,"Camisa",20.0,50)
agregar_producto(inventario, "Pantalon", 30.0, 30)
actualizar_stock(inventario,"Camisa",10)
# print(calcular_valor_inventario(inventario))


