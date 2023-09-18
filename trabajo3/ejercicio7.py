import tkinter as tk

class ComparadorNumerico:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def comparar(self):
        if self.a > self.b:
            return "A es mayor que B"
        elif self.a < self.b:
            return "A es menor que B"
        else:
            return "A es igual a B"

def comparar_valores():
    valor_a = float(valor_a_entry.get())
    valor_b = float(valor_b_entry.get())
    
    comparador = ComparadorNumerico(valor_a, valor_b)
    
    resultado_label.config(text=comparador.comparar())

# Crear la ventana principal
root = tk.Tk()
root.title("Comparador de Valores")

# Crear etiquetas y campos de entrada
valor_a_label = tk.Label(root, text="Valor A:")
valor_a_entry = tk.Entry(root)

valor_b_label = tk.Label(root, text="Valor B:")
valor_b_entry = tk.Entry(root)

comparar_button = tk.Button(root, text="Comparar", command=comparar_valores)

resultado_label = tk.Label(root, text="Resultado:")
resultado_label.config(font=("Helvetica", 12))

# Ubicar etiquetas y campos de entrada en la ventana
valor_a_label.pack()
valor_a_entry.pack()
valor_b_label.pack()
valor_b_entry.pack()
comparar_button.pack()
resultado_label.pack()

# Iniciar la aplicación
root.mainloop()