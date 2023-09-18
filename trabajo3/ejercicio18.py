import tkinter as tk

class Empleado:
    
    codigo_empleado: str
    nombres: str
    horas_trabajadas: int
    valor_hora: float
    retencion: str
        
    def calcular_retencion(self):
        horas_trabajadas = float(self.horas_trabajadas.get())
        valor_hora = float(self.valor_hora.get())
        retencion = float(self.retencion.get())
        
        salario_bruto = horas_trabajadas * valor_hora
        retencion_fuentes = (retencion / 100) * salario_bruto
        salario_neto = salario_bruto - retencion_fuentes
        
        resultado_label.config(text=f"Empleado: {self.nombres.get()}\nCódigo: {self.codigo_empleado.get()}\nSalario Bruto: ${salario_bruto:.2f}\nRetención en la Fuente: ${retencion_fuentes:.2f}\nSalario Neto: ${salario_neto:.2f}")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Salario")

empleado = Empleado()

# Crear etiquetas y campos de entrada
codigo_empleado_label = tk.Label(root, text="Código del Empleado:")
empleado.codigo_empleado = tk.Entry(root)

nombres_label = tk.Label(root, text="Nombres:")
empleado.nombres = tk.Entry(root)

horas_trabajadas_label = tk.Label(root, text="Horas Trabajadas al Mes:")
empleado.horas_trabajadas = tk.Entry(root)

valor_hora_label = tk.Label(root, text="Valor Hora Trabajada:")
empleado.valor_hora = tk.Entry(root)

retencion_label = tk.Label(root, text="Porcentaje de Retención en la Fuente:")
empleado.retencion = tk.Entry(root)

calcular_button = tk.Button(root, text="Calcular Salario", command=empleado.calcular_retencion)

resultado_label = tk.Label(root, text="Resultado:")
resultado_label.config(font=("Helvetica", 12))

# Ubicar etiquetas y campos de entrada en la ventana
codigo_empleado_label.pack()
empleado.codigo_empleado.pack()
nombres_label.pack()
empleado.nombres.pack()
horas_trabajadas_label.pack()
empleado.horas_trabajadas.pack()
valor_hora_label.pack()
empleado.valor_hora.pack()
retencion_label.pack()
empleado.retencion.pack()
calcular_button.pack()
resultado_label.pack()

# Iniciar la aplicación
root.mainloop()