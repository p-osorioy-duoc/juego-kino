import random as r
import datetime as f

# Agrego un comentario al codigo

#El resultado de date es un tipo de datos "datetime"
#Por lo tanto hay que transformarlo a STRING
fecha=str(f.date.today())

# Ahora definiré las funciones de mi código
def imprime_numero_kino():
    for i in range(1,26,1):
        if (i==5 or i==10 or i==15 or i==20):
            print(i) # \n
        else:
            print(i, end="\t")

# Lista que almacena mis números comprados
numeros_comprados=[]

def selecciona_azar():
    # Para poder utilizar la lista que vive fuera de la función
    # Necesito decirle a python que la busque fuera de función
    # mediante la palabla global
    global numeros_comprados
    
    for i in range(14):
        num=r.randint(1,25) # Genera un número entre 1 y 25

        while num in numeros_comprados:
            num=r.randint(1,25) # Si el número generado ya esta
                                # en la lista... se vuelve a generar
        else:
            numeros_comprados.append(num) # Si no estaba en la lista.. 
                                        # Entonces lo guardamos..se agrega!


nombre=input("Ingresa tu nombre:")
#Ordenamos la lista
numeros_comprados.sort()
print("Tus números son:")
print(numeros_comprados)

archivo_nombre = "C:\\Users\\pv-alumno\\Desktop\\clase archivos\\ventas.txt"
# Abrir para escribir ('w' de write | 'a' de agregar)
with open(archivo_nombre, "a") as archivo:   
    archivo.write("\n")
    archivo.write(fecha)
    archivo.write("\t")
    archivo.write(nombre)
    archivo.write("\t")
    archivo.write(str(numeros_comprados))
    
print("Historial de ventas de numeros")
# Abrir para escribir ('r' de read)
with open(archivo_nombre, "r") as archivo:
    for linea in archivo:   
        print(linea.strip())
    