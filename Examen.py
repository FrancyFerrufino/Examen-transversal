libros = {"L001":["Sombras del Sur", "A. rojas", "novela", 2019,"AndesPress", False],
"L002":["Python en Ruta", "M. Diaz", "tecnologia", 2023, "CodeBooks", True],
"L003":["Mar y Viento", "C. Silva", "poesia", 2017, "Litoral", False],
"L004":["Historia Breve", "J. Peres", "historia", 2015, "Cronos", False],
"L005":["Mundos Lejanos", "L. Torres", "cientcia ficcion", 2021, "Orion",True],
"L006": ["Cocina Simple","R.soto", "cocina", 2018, "Sabores",False]}


prestamos = {"L001":[500,4],"L002":[700, 0],"L003":[300, 10],"L004":[400, 2], "L005":[600, 1],"L006": [350, 6]}




def menu():
    print("=========MENU PRINCIPAL==========")
    print("1. Copias por genero")
    print("2. Busqueda de libros por rango de multa")
    print("3. Actulizar multa de libro")
    print("3. Agregar libro")
    print("4. Eliminar libro")
    print("6. Salir")
    print("=================================")


def leer_opc():
    try:
        opc = int(input("Ingrese una opcion del Menu: "))
        if(opc >= 1 and opc <= 6):
            return opc
        else:
            raise ValueError
    except ValueError:
        print("la ocion del menu de ser un numero entre 1 a 6")

#validaciones libros

def Validar_codigo(codigo):
    return(codigo.strip() != "")
def validar_titulo(titulo):
    return (titulo.strip() != "")
def validar_autor(autor):
    return(autor.strip() != "")
def validar_genero(genero):
    return(genero.strip() != "" )
def validar_año(año):
    return(año > 0)
def validar_editorial(editorial):
    return(editorial.strip()!= "")
def Validar_es_novedad(es_novedad):
    if(es_novedad == "s"):
        es_novedad == True
        return
    else:
        es_novedad == False
        return
        
#validar prestamo
def validar_precio_multa(precio_multa):
    return (precio_multa > 0)
def validar_copias_disponible(copias_diponibles):
    return(copias_diponibles >= 0)


#agregar libro
def agregar_libro(libros):
    while True:
        codigo = input("ingrese el Codigo del libro que desea registrar: ")
        if(not Validar_codigo(codigo)):
            print("El Libro no cumple con los requisitos!")
            return
        else:
            if(codigo in libros):
                print("el libro ya esta en la lista")
            else:
                break
    
    
    
    titulo = input("Ingrese el titulo del libro: ")
    if (not validar_titulo(titulo)):
        print("El Libro no cumple con los requisitos!")
    
    autor = input("Ingrese el nombre el autor del libro: ")
    if (not validar_autor(autor)):
        print("El Libro no cumple con los requisitos!")
    
    genero = input("ingrese el genero del libro")
    if (not validar_genero(genero)):
        print("El Libro no cumple con los requisitos!")
        
    try:
        año =int(input("Ingrese el año del libro que desea registrar: "))
        if(not validar_año(año)):
            raise ValueError
    except ValueError:
        print("El año debe ser mayor a 0")
        return
    editorial = input("ingrese la editorial del libro")
    if(not validar_editorial(editorial)):
        print("El Libro no cumple con los requisitos!")
        return
    es_novedad = input("ingrese S/N si el libro es una novedad o no: ")
    if(not Validar_es_novedad(es_novedad)):
        print("El Libro no cumple con los requisitos!")
        return
    try:
        precio_multa = float(input("ingrese la multa del libro: "))
        if(not validar_precio_multa(precio_multa)):
            raise ValueError
    except ValueError:
        print("El precio de la multa debe ser mayor a 0")
        
    try:
        copias_disponibles = float(input("ingrese la cantidad de copias disponibles: "))
        if(not validar_copias_disponible(copias_disponibles)):
            raise ValueError
    except ValueError:
        print("la cantidad de copias debe ser igual o mayor a 0")
    
    #crear diccionario
    libro ={codigo["titulo": titulo, "autor": autor, "genero": genero,"año": año, "editorial": editorial, "es_novedad": es_novedad]}
    prestamo={codigo["precio_multa": precio_multa, "copias disponibles": copias_disponibles]}
    
    #agregar a la lista
    libros.append(libro)
    prestamos.append(prestamo)
    
    print("El libro fue agregado exitosamente!!!")
    
    
    
#buscar libro
def buscar_libro(libros, codigo):
    for i in range (len (libros)):
        if (codigo[i][codigo]== codigo):
            return i
    return-1


#eliminar libro
def eliminar_libro(libros):
    codigo = input("ingrese el codigo del libro que desea eliminar")
    posicion = buscar_libro(libros, codigo)
    
    if(posicion == -1):
        print(f"el codigo {codigo} no se encuentra registrado")
















while True:
    menu()
    opc = leer_opc()
    
    if(opc==1):
        pass
    elif(opc==2):
        pass
    elif(opc==3):
        pass
    elif(opc==4):
        agregar_libro(libros)
    elif(opc==5):
        if(len(libros == 0)):
            print("libro no registrado")
        else:
            eliminar_libro(libros)
    elif(opc==6):
        print("Programa finalizado")    
        break  
    else:
        print("Opcion Invalida!!")
    
    