#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija


if __name__ == "__main__":

    texto = open(sys.argv[1])
    lineas = texto.readlines()
    
    for linea in lineas:
    
        print(linea, len(linea))
        line = linea.split(',')
        operando = line[0]
        resultado = int(line[1])
                   
        if operando == "suma":
            for i in range(2,len(line)):
                resultado = resultado + int(line[i])
            print(resultado)
            
        elif operando == "resta":
            for i in range(2,len(line)):
                resultado = resultado - int(line[i])
            print(resultado)
            
        elif operando == "multiplica":
            for i in range(2,len(line))
                resultado = resultado * int(line[i])
            print(resultado)
            
        elif operando == "divide":
            resultado = int(line[1])
            
        else:
            print("La operación no se puede realizar")
        
        
                
    texto.close()
