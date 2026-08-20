"""def pedir_nombre():
    nombre_archivo = input("Ingresa el nombre del archivo que contiene el sudoku: ")
    return nombre_archivo
"""
def cargar_tablero(nombre_archivo):
    fichero = open(nombre_archivo)
    tablero = fichero.readlines()
    TCompleto = []
    for fila in tablero:
        FilaAAgregar= []
        prov = fila.strip()
        for caracter in prov:
            x = int(caracter)
            FilaAAgregar.append(x)
        TCompleto.append(FilaAAgregar)

    print(TCompleto)
    pass


def resolver_tablero():
    pass

def main():
    #puzle = pedir_nombre()
    cargar_tablero("puzle01.txt")
    resolver_tablero()


if __name__ == "__main__":
    main()