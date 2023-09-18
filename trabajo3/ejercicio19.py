import tkinter as tk
import math

class TrianguloEquilatero:
    def __init__(self, lado):
        self.lado = lado
    
    def calcular_perimetro(self):
        perimetro = 3 * self.lado
        return perimetro
    
    def calcular_altura(self):
        altura = (math.sqrt(3) / 2) * self.lado
        return altura
    
    def calcular_area(self):
        area = (math.sqrt(3) / 4) * (self.lado ** 2)
        return area

def calcular_resultados():
    lado = float(lado_entry.get())
    
    triangulo = TrianguloEquilatero(lado)
    
    perimetro = triangulo.calcular_perimetro()
    altura = triangulo.calcular_altura()
    area = triangulo.calcular_area()
    
    resultado_label.config(text=f"Perímetro: {perimetro:.2f}\nAltura: {altura:.2f}\nÁrea: {area:.2f}")

root = tk.Tk()
root.title("Calculadora de Triángulo Equilátero")

lado_label = tk.Label(root, text="Valor del Lado:")
lado_entry = tk.Entry(root)

calcular_button = tk.Button(root, text="Calcular", command=calcular_resultados)

resultado_label = tk.Label(root, text="Resultados:")
resultado_label.config(font=("Helvetica", 12))

lado_label.pack()
lado_entry.pack()
calcular_button.pack()
resultado_label.pack()

root.mainloop()