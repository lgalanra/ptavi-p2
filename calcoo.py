#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora():

    def __init__(self, value1, value2):
        self.op1 = value1
        self.op2 = value2

    def suma(self):
        return self.op1 + self.op2

    def resta(self):
        return self.op1 - self.op2


if __name__ == "__main__":

    try:
        value1 = int(sys.argv[1])
        value2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Introducir solo numeros")
    calculadora = Calculadora(value1, value2)
    if sys.argv[2] == "suma":
        print(calculadora.suma())
    elif sys.argv[2] == "resta":
        print(calculadora.resta())
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')
