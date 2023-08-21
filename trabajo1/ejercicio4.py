"""
A la mamá de Juan le preguntan su edad, y contesta: tengo 3 hijos, pregúntele a Juan su
edad. Alberto tiene 2/3 de la edad de Juan, Ana tiene 4/3 de la edad de Juan y mi edad es
la suma de las tres. Hacer un algoritmo que muestre la edad de los cuatro.
"""

def solution() -> str:
    print('Digita la edad de Juan')
    edad_juan = int(input(""))
    
    alberto = int(2/3 * edad_juan)
    ana = int(4/3 * edad_juan)
    
    mama = edad_juan + alberto + ana
    
    print(f'La edad de Juan es {edad_juan} años')
    print(f'La edad de Alberto es {alberto} años')
    print(f'La edad de Ana es {ana} años')
    print(f'La edad de la Mamá es {mama} años')
    
    
if __name__ == '__main__':
    solution()