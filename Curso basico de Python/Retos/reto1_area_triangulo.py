## ################################
## RETO 1 - AREA DE UN TRIANGULO
## ################################
def run():
    #Ingreso de datos
    print("-- Calculo del area de un triangulo")
    base = input("ingrese la base: ")
    assert base.isnumeric(), "Base debe ser un numero"
    altura = input("ingrese la altura: ")
    assert altura.isnumeric(), "Base debe ser un numero"

    base = int(base)
    altura = int(altura)

    area = (base*altura)/2
    print("El area del triangulo es {}".format(str(area)))

if __name__ == '__main__':
    run()