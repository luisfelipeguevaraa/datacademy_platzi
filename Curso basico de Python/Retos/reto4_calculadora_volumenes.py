## ##########################################
## RETO 4 - CALCULADORA DE VOLUMENES
## ##########################################
import math

def run():
    #Ingreso de datos
    print("-- CALCULADORA DE VOLUMENES")
    radio = input("ingrese radio de la base (metros): ")
    assert radio.isnumeric() or radio.isdecimal(), "Debe ingresar un numero como radio"
    altura = input("ingrese altura del cilindro (metros): ")
    assert altura.isnumeric() or altura.isdecimal(), "Debe ingresar un numero como altura"
    radio = float(radio)
    altura = float(altura)
    volumen = (math.pi)*(radio**2)*(altura)
    print("Volumen del cilindro es {} m3".format(str(volumen)))

if __name__ == '__main__':
    run()