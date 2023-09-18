import tkinter as tk

class Estudiante:
    def __init__(self, numero_inscripcion, nombres, patrimonio, estrato):
        self.numero_inscripcion = numero_inscripcion
        self.nombres = nombres
        self.patrimonio = patrimonio
        self.estrato = estrato
    
    def calcular_pago_matricula(self):
        costo_base = 50000
        
        if self.patrimonio > 2000000 and self.estrato > 3:
            incremento = self.patrimonio * 0.03
        else:
            incremento = 0
        
        pago_matricula = costo_base + incremento
        return pago_matricula

def calcular_matricula():
    numero_inscripcion = numero_inscripcion_entry.get()
    nombres = nombres_entry.get()
    patrimonio = float(patrimonio_entry.get())
    estrato = int(estrato_entry.get())
    
    estudiante = Estudiante(numero_inscripcion, nombres, patrimonio, estrato)
    
    pago_matricula = estudiante.calcular_pago_matricula()
    
    resultado_label.config(text=f"Número de Inscripción: {numero_inscripcion}\nNombres: {nombres}\nPago de Matrícula: ${pago_matricula:.2f}")

root = tk.Tk()
root.title("Calculadora de Matrícula")

numero_inscripcion_label = tk.Label(root, text="Número de Inscripción:")
numero_inscripcion_entry = tk.Entry(root)

nombres_label = tk.Label(root, text="Nombres:")
nombres_entry = tk.Entry(root)

patrimonio_label = tk.Label(root, text="Patrimonio:")
patrimonio_entry = tk.Entry(root)

estrato_label = tk.Label(root, text="Estrato Social:")
estrato_entry = tk.Entry(root)

calcular_button = tk.Button(root, text="Calcular Matrícula", command=calcular_matricula)

resultado_label = tk.Label(root, text="Resultado:")
resultado_label.config(font=("Helvetica", 12))

numero_inscripcion_label.pack()
numero_inscripcion_entry.pack()
nombres_label.pack()
nombres_entry.pack()
patrimonio_label.pack()
patrimonio_entry.pack()
estrato_label.pack()
estrato_entry.pack()
calcular_button.pack()
resultado_label.pack()

root.mainloop()