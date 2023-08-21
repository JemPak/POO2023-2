"""
Dado el radio de un círculo. Haga un algoritmo que obtenga el área del círculo y la longitud
de la circunferencia. 
"""
import math

def solution() -> str:
    radio = float(input("Ingrese el radio del círculo: "))
    
    area = math.pi * radio ** 2
    longitud_circunferencia = 2 * math.pi * radio
    
    print("El área del círculo es:", area)
    print("La longitud de la circunferencia es:", longitud_circunferencia)
    
if __name__ == '__main__':
    solution()