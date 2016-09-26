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
