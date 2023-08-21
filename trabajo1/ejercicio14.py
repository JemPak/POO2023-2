"""
Elabore un algoritmo que lea un número y obtenga su cuadrado y su cubo. 
"""

def solution() -> str:
    number = float(input(f"Ingrese un número entero - "))
    print(f"El cuadrado del número {number} es {number**2}")
    print(f"El cubo del número {number} es {number**3}")
    
if __name__ == '__main__':
    solution()