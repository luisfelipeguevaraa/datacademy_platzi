## ##########################################
## RETO 3 - CONVERSOR DE MILLAS A KILOMETROS
## ##########################################

factor = 1.609344

def run():
    #Ingreso de datos
    print("-- CONVERSOR DE MILLAS A KILOMETROS")
    millas = input("ingrese millas: ")
    assert millas.isnumeric() or millas.isdecimal(), "Debe ingresar un numero como millas"
    millas = float(millas)
    kilometros = millas*factor
    print("Millas es {} a kilometros es {}".format(str(millas), str(kilometros) ))

if __name__ == '__main__':
    run()