## ##########################################
## RETO 5 - RANGOS CAMBIANTES
## ##########################################

def calcular(inferior, superior, comparador):
    if comparador > inferior and comparador < superior:
        print("Comparador es {} ".format(str(comparador)))
    else:
        comparador = input("ingrese otro comparador: ")
        assert comparador.isnumeric(), "Debe ingresar un numero"
        comparador = int(comparador)
        calcular(inferior, superior, comparador)

def run():
    #Ingreso de datos
    print("-- RANGOS CAMBIANTES")
    inferior = input("ingrese limite inferior: ")
    assert inferior.isnumeric(), "Debe ingresar un numero"
    superior = input("ingrese limite superior: ")
    assert superior.isnumeric(), "Debe ingresar un numero"
    comparador = input("ingrese comparador: ")
    assert comparador.isnumeric(), "Debe ingresar un numero"
    inferior = int(inferior)
    superior = int(superior)
    comparador = int(comparador)
    assert inferior < superior, "Número inferior debe se meno a numero superior"
    calcular(inferior, superior, comparador)

if __name__ == '__main__':
    run()