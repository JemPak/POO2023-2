import tkinter as tk

class Empleado:
    def __init__(self, nombre, salario_por_hora, horas_trabajadas):
        self.nombre = nombre
        self.salario_por_hora = salario_por_hora
        self.horas_trabajadas = horas_trabajadas
    
    def calcular_salario_mensual(self):
        salario_mensual = self.salario_por_hora * self.horas_trabajadas
        return salario_mensual

def calcular_salario():
    nombre = nombre_entry.get()
    salario_por_hora = float(salario_por_hora_entry.get())
    horas_trabajadas = float(horas_trabajadas_entry.get())
    
    empleado = Empleado(nombre, salario_por_hora, horas_trabajadas)
    
    salario_mensual = empleado.calcular_salario_mensual()
    
    if salario_mensual > 450000:
        resultado_label.config(text=f"Nombre: {nombre}\nSalario Mensual: ${salario_mensual:.2f}")
    else:
        resultado_label.config(text=f"Nombre: {nombre}")

root = tk.Tk()
root.title("Calculadora de Salario Mensual")

nombre_label = tk.Label(root, text="Nombre del Empleado:")
nombre_entry = tk.Entry(root)

salario_por_hora_label = tk.Label(root, text="Salario por Hora:")
salario_por_hora_entry = tk.Entry(root)

horas_trabajadas_label = tk.Label(root, text="Horas Trabajadas en el Mes:")
horas_trabajadas_entry = tk.Entry(root)

calcular_button = tk.Button(root, text="Calcular Salario", command=calcular_salario)

resultado_label = tk.Label(root, text="Resultado:")
resultado_label.config(font=("Helvetica", 12))

nombre_label.pack()
nombre_entry.pack()
salario_por_hora_label.pack()
salario_por_hora_entry.pack()
horas_trabajadas_label.pack()
horas_trabajadas_entry.pack()
calcular_button.pack()
resultado_label.pack()

root.mainloop()