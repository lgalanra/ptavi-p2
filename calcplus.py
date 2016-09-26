#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija


if __name__ == "__main__":

    texto = open(sys.argv[1])
    lineas = texto.readlines()
    for linea in lineas:
        print(linea)
        line = linea.split(',')
        operando = line[0]
        resultado = int(line[1])
        if operando == "suma":
            for i in range(2, len(line)):
                resultado = resultado + int(line[i])
            print("El resultado es: " + str(resultado))
        elif operando == "resta":
            for i in range(2, len(line)):
                resultado = resultado - int(line[i])
            print("El resultado es: " + str(resultado))
        elif operando == "multiplica":
            for i in range(2, len(line)):
                resultado = resultado * int(line[i])
            print("El resultado es: " + str(resultado))
        elif operando == "divide":
            for i in range(2, len(line)):
                if int(line[i]) != 0:
                    resultado = resultado / int(line[i])
                else:
                    sys.exit("Division by zero is not allowed")
            print("El resultado es: " + str(resultado))
        else:
            print("La operación no se puede realizar")
texto.close()
