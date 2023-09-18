import tkinter as tk
import math

class EcuacionSegundoGrado:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def calcular_soluciones(self):
        discriminante = self.b ** 2 - 4 * self.a * self.c
        
        if discriminante > 0:
            raiz1 = (-self.b + math.sqrt(discriminante)) / (2 * self.a)
            raiz2 = (-self.b - math.sqrt(discriminante)) / (2 * self.a)
            return f"Soluciones reales: {raiz1:.2f} y {raiz2:.2f}"
        elif discriminante == 0:
            raiz = -self.b / (2 * self.a)
            return f"Solución real única: {raiz:.2f}"
        else:
            parte_real = -self.b / (2 * self.a)
            parte_imaginaria = math.sqrt(abs(discriminante)) / (2 * self.a)
            return f"Soluciones complejas: {parte_real:.2f} + {parte_imaginaria:.2f}i y {parte_real:.2f} - {parte_imaginaria:.2f}i"

def calcular_soluciones_ecuacion():
    valor_a = float(valor_a_entry.get())
    valor_b = float(valor_b_entry.get())
    valor_c = float(valor_c_entry.get())
    
    ecuacion = EcuacionSegundoGrado(valor_a, valor_b, valor_c)
    
    soluciones = ecuacion.calcular_soluciones()
    
    resultado_label.config(text=soluciones)

root = tk.Tk()
root.title("Calculadora de Ecuación de Segundo Grado")

valor_a_label = tk.Label(root, text="Valor A:")
valor_a_entry = tk.Entry(root)

valor_b_label = tk.Label(root, text="Valor B:")
valor_b_entry = tk.Entry(root)

valor_c_label = tk.Label(root, text="Valor C:")
valor_c_entry = tk.Entry(root)

calcular_button = tk.Button(root, text="Calcular Soluciones", command=calcular_soluciones_ecuacion)

resultado_label = tk.Label(root, text="Resultado:")
resultado_label.config(font=("Helvetica", 12))

valor_a_label.pack()
valor_a_entry.pack()
valor_b_label.pack()
valor_b_entry.pack()
valor_c_label.pack()
valor_c_entry.pack()
calcular_button.pack()
resultado_label.pack()

root.mainloop()