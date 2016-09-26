#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo

class CalculadoraHija(calcoo.Calculadora):

    def mult(self):
        return self.op1 * self.op2

    def div(self):
        try:
            return self.op1 / self.op2
        except DivError:
            sys.exit("No se puede dividir por cero")
           
if __name__ == "__main__":

    try:
        value1 = int(sys.argv[1])
        value2 = int(sys.argv[3])
    except ValueError:
        print("Introducir int o float")
        
    calc = CalculadoraHija(value1,value2)
    
    if sys.argv[2] == "suma":
        print(calc.suma())
    elif sys.argv[2] == "resta":
        print(calc.resta())
    elif sys.argv[2] == "multiplica":
        print(calc.mult())
    elif sys.argv[2] == "divide":
        print(calc.div())
    else:
        sys.exit("Operación no válida")
    
