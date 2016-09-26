#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv
import calcoohija


if __name__ == "__main__":

texto = sys.argv[1]

with open(texto) as d
    lineas = csv.lines(d)
    
    for fila in lineas:
        line = row.split(',')
        operador = line[0]
        resultado = int(line[1])
        
        if operador == "suma":
            for i in range(2,len(line))
                resultado = resultado + int(line[i])
            print(resultado)
            
        elif operador == "resta":
            for i in range(2,len(line))
                resultado = resultado - int(line[i])
            print(resultado)
        
        elif operador == "multiplica":
            for i in range(2,len(line))
                resultado = resultado * int(line[i])
            print(resultado)
            
        elif operador == "divide"
            for i in range(2,len(line))
                if int(line[i] != 0:
                    resultado = resultado / int(line[i])
                else:
                    sys.exit("División por cero no válida")
            print(resultado)
            
        else:
            print("La operación no se puede realizar")
            
texto.close()
