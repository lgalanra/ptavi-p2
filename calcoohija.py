#!/usr/bin/python3
# -*- coding: utf-8 -*-

import calcoo

class CalculadoraHija(Calculadora):

    def mult(self):
        return self.op1 * self.op2

    def div(self):
        try:
            self.op1 / self.op2
        except DivError:
            sys.exit("No se puede dividir por cero")
           
if __name__ == "__main__":

    try:
        value1 = sys.argv[1]
        value2 = sys.argv[3]
    except ValueError:
        print("Introducir int o float")
    
