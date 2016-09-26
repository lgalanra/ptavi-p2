#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija
import csv


if __name__ == "__main__":

    with open('fichero.csv') as mifichero:
        texto = csv.reader(mifichero)
        for linea in texto:
            print(linea)
            operando = linea[0]
            resultado = int(linea[1])
            if operando == "suma":
                for i in range(2, len(linea)):
                    resultado = resultado + int(linea[i])
                print("El resultado es: " + str(resultado))
            elif operando == "resta":
                for i in range(2, len(linea)):
                    resultado = resultado - int(linea[i])
                print("El resultado es: " + str(resultado))
            elif operando == "multiplica":
                for i in range(2, len(linea)):
                    resultado = resultado * int(linea[i])
                print("El resultado es: " + str(resultado))
            elif operando == "divide":
                for i in range(2, len(linea)):
                    if int(linea[i]) != 0:
                        resultado = resultado / int(linea[i])
                    else:
                        sys.exit("Division by zero is not allowed")
                print("El resultado es: " + str(resultado))
            else:
                print("La operación no se puede realizar")
