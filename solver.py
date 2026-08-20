def pedir_nombre():
    nombre_archivo = input("Ingresa el nombre del archivo que contiene el sudoku: ")
    return nombre_archivo

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
    
    return TCompleto

def encontar_vacia(tablero):
    for fila in tablero:
        contador = 0
        for i in range(9):
            if fila[i] == 0:
                return [contador, i]
        contador += 1 
        
    


def resolver_tablero():
    pass

def main():
    #puzle = pedir_nombre()
    tablero = cargar_tablero("puzle01.txt")
    resolver_tablero()
    print(encontar_vacia(tablero))


if __name__ == "__main__":
    main()