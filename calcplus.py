#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

calc = CalculadoraHija()

if __name__ == "__main__":

    texto = open(sys.argv[1])
    lineas = texto.readlines()
    
    for linea in lineas:
    
        print(linea, len(linea))
        line = linea.split(',')
        operando = line[0]
        resultado = int(line[1])
                   
        if operando == "suma":
            for i in range(2,len(line))
                resultado = resultado + 1
            print(resultado)
            
        elif operando == "resta":
            resultado = int(line[1])
            
        elif operando == "multiplica":
            resultado = int(line[1])
            
        elif operando == "divide":
            resultado = int(line[1])
            
        else:
            sys.exit("bye")
        
        
                
    texto.close()
