import tkinter as tk
import math

class FiguraGeometrica:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def calcular_area(self):
        pass
    
    def calcular_perimetro(self):
        pass

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * (self.radio ** 2)
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        super().__init__("Cuadrado")
        self.lado = lado
    
    def calcular_area(self):
        return self.lado ** 2
    
    def calcular_perimetro(self):
        return 4 * self.lado

class TrianguloRectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        super().__init__("Triángulo Rectángulo")
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return (self.base * self.altura) / 2
    
    def calcular_perimetro(self):
        hipotenusa = math.sqrt((self.base ** 2) + (self.altura ** 2))
        return self.base + self.altura + hipotenusa
    
    def determinar_tipo(self):
        if self.base == self.altura:
            return "Equilátero"
        elif self.base == self.altura or self.base == self.altura:
            return "Isósceles"
        else:
            return "Escaleno"

def calcular():
    figura_seleccionada = figura_combobox.get()
    if figura_seleccionada == "Círculo":
        radio = float(valor_entry.get())
        figura = Circulo(radio)
    elif figura_seleccionada == "Rectángulo":
        base = float(base_entry.get())
        altura = float(altura_entry.get())
        figura = Rectangulo(base, altura)
    elif figura_seleccionada == "Cuadrado":
        lado = float(lado_entry.get())
        figura = Cuadrado(lado)
    elif figura_seleccionada == "Triángulo Rectángulo":
        base = float(base_entry.get())
        altura = float(altura_entry.get())
        figura = TrianguloRectangulo(base, altura)
    
    area_label.config(text=f"Área: {figura.calcular_area()} cm²")
    perimetro_label.config(text=f"Perímetro: {figura.calcular_perimetro()} cm")
    
    if figura_seleccionada == "Triángulo Rectángulo":
        tipo_label.config(text=f"Tipo de Triángulo: {figura.determinar_tipo()}")
    else:
        tipo_label.config(text="")

root = tk.Tk()
root.title("Calculadora de Figuras Geométricas")

figura_label = tk.Label(root, text="Selecciona una figura:")
figura_combobox = tk.StringVar()
figura_combobox.set("Círculo")
figura_optionmenu = tk.OptionMenu(root, figura_combobox, "Círculo", "Rectángulo", "Cuadrado", "Triángulo Rectángulo")

valor_label = tk.Label(root, text="Valor (radio, base, lado, etc.):")
valor_entry = tk.Entry(root)

base_label = tk.Label(root, text="Base:")
base_entry = tk.Entry(root)

altura_label = tk.Label(root, text="Altura:")
altura_entry = tk.Entry(root)

lado_label = tk.Label(root, text="Lado:")
lado_entry = tk.Entry(root)

calcular_button = tk.Button(root, text="Calcular", command=calcular)

area_label = tk.Label(root, text="Área:")
perimetro_label = tk.Label(root, text="Perímetro:")
tipo_label = tk.Label(root, text="")

figura_label.pack()
figura_optionmenu.pack()
valor_label.pack()
valor_entry.pack()
base_label.pack()
base_entry.pack()
altura_label.pack()
altura_entry.pack()
lado_label.pack()
lado_entry.pack()
calcular_button.pack()
area_label.pack()
perimetro_label.pack()
tipo_label.pack()

root.mainloop()
