def pedir_nombre():
    nombre_archivo = input("Ingresa el nombre del archivo que contiene el sudoku: ")
    return nombre_archivo

def cargar_tablero(nombre_archivo):
    fichero = open(nombre_archivo)
    print(fichero.readlines())
    pass

def main():
    puzle = pedir_nombre()
    cargar_tablero(puzle)

if __name__ == "__main__":
    main()