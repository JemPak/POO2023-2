"""
Un empleado trabaja 48 horas en la semana a razón de $5.000 hora. El porcentaje de
retención en la fuente es del 12,5% del salario bruto. Se desea saber cuál es el salario bruto,
la retención en la fuente y el salario neto del trabajador. 
"""

def solution() -> str:
    
    print(f"Ingrese el # de horas trabajadas en la semana")
    horas = int(input())
    tasa = 5
    retencion = 0.125
    
    calc_retencion = horas * tasa * retencion
    print(f"El salario bruto es ${horas*tasa}")
    print(f"La retención es ${calc_retencion}")
    print(f"El salario neto es ${(horas*tasa) - (calc_retencion)}")
    
if __name__ == '__main__':
    solution()