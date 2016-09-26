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
        newline = line[1:]
        print(newline)
        
        print(operando)
        
        if operando == "suma":
            resultado = int(line[1])
            
            for newline in line:
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
