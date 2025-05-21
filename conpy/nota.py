import tkinter as tk
from tkinter import messagebox

# Datos iniciales
alumnos = [
    ['Juan', [['Matematicas', 8], ['Lengua', 9], ['Sociales', 7], ['Naturales', 7]]],
    ['Ana', [['Lengua', 9], ['Matematicas', 10], ['Sociales', 8], ['Naturales', 6]]],
    ['Luis', [['Lengua', 6], ['Sociales', 8], ['Matematicas', 7], ['Naturales', 6]]],
    ['María', [['Lengua', 9], ['Sociales', 10], ['Naturales', 10], ['Matematicas', 9]]]
]

def buscar_alumno(nombre):
    for alumno in alumnos:
        if alumno[0].lower() == nombre.lower():
            return alumno
    return None

def agregar_o_modificar():
    nombre = entry_nombre.get().strip()
    materia = entry_materia.get().strip()
    nota_texto = entry_nota.get().strip()

    if not nombre or not materia or not nota_texto:
        messagebox.showwarning("Faltan datos", "Por favor completá todos los campos.")
        return

    try:
        nota = int(nota_texto)
        if nota < 1 or nota > 10:
            raise ValueError
    except ValueError:
        messagebox.showerror("Nota inválida", "La nota debe ser un número entre 1 y 10.")
        return

    alumno = buscar_alumno(nombre)
    mensaje = ""

    if alumno:
        mensaje += f"👤 El alumno {nombre} ya existe.\n"
        for m in alumno[1]:
            if m[0].lower() == materia.lower():
                mensaje += f"✏️ Actualizando nota de {materia} de {m[1]} a {nota}.\n"
                m[1] = nota
                break
        else:
            alumno[1].append([materia, nota])
            mensaje += f"➕ Agregando nueva materia {materia} con nota {nota}.\n"
    else:
        alumnos.append([nombre, [[materia, nota]]])
        mensaje += f"🆕 Agregando alumno nuevo: {nombre} con {materia}: {nota}.\n"

    mostrar_resultado(mensaje)

def mostrar_resultado(mensaje):
    resultado = mensaje + "\n📋 Lista actualizada de alumnos:\n"
    for alumno in alumnos:
        resultado += f"- {alumno[0]}:\n"
        for materia, nota in alumno[1]:
            resultado += f"   • {materia}: {nota}\n"
    text_resultado.config(state='normal')
    text_resultado.delete("1.0", tk.END)
    text_resultado.insert(tk.END, resultado)
    text_resultado.config(state='disabled')

# Interfaz
root = tk.Tk()
root.title("Sistema de Calificaciones")

tk.Label(root, text="Nombre del alumno:").pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

tk.Label(root, text="Materia:").pack()
entry_materia = tk.Entry(root)
entry_materia.pack()

tk.Label(root, text="Nota (1-10):").pack()
entry_nota = tk.Entry(root)
entry_nota.pack()

tk.Button(root, text="Agregar / Modificar Nota", command=agregar_o_modificar).pack(pady=5)

text_resultado = tk.Text(root, width=60, height=20, state='disabled', wrap='word')
text_resultado.pack(pady=10)

root.mainloop()
