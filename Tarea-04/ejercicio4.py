import tkinter as tk
from tkinter import messagebox


class Programador:
    def __init__(self, nombre, apellidos):
        self.validar_campo(nombre, "nombre")
        self.validar_campo(apellidos, "apellidos")
        self.nombre = nombre
        self.apellidos = apellidos

    def validar_campo(self, valor, nombre_campo):
        if not valor:
            raise ValueError(f"El campo {nombre_campo} no puede estar vacío.")
        if len(valor) >= 20:
            raise ValueError(f"El {nombre_campo} debe tener menos de 20 caracteres.")
        if any(char.isdigit() for char in valor):
            raise ValueError(f"El {nombre_campo} solo debe contener texto, no números.")

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"


class EquipoMaratonProgramacion:
    def __init__(self, nombre, universidad, lenguaje, tamano):
        if tamano < 2 or tamano > 3:
            raise ValueError("El tamaño del equipo debe ser de mínimo 2 y máximo 3 integrantes.")
        self.nombre = nombre
        self.universidad = universidad
        self.lenguaje = lenguaje
        self.tamano = tamano
        self.programadores = []

    def esta_completo(self):
        return len(self.programadores) == self.tamano

    def anadir_programador(self, programador):
        if self.esta_completo():
            raise Exception("El equipo ya está completo, no se pueden añadir más integrantes.")
        self.programadores.append(programador)


class VentanaMaraton:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Maratón de Programación")
        self.ventana.geometry("450x580")
        self.equipo = None

        frame_equipo = tk.LabelFrame(self.ventana, text="1. Datos del Equipo", padx=10, pady=10)
        frame_equipo.pack(fill="x", padx=15, pady=10)

        tk.Label(frame_equipo, text="Nombre del equipo:").grid(row=0, column=0, sticky="w", pady=2)
        self.txt_equipo = tk.Entry(frame_equipo, width=25)
        self.txt_equipo.grid(row=0, column=1, pady=2)

        tk.Label(frame_equipo, text="Universidad:").grid(row=1, column=0, sticky="w", pady=2)
        self.txt_universidad = tk.Entry(frame_equipo, width=25)
        self.txt_universidad.grid(row=1, column=1, pady=2)

        tk.Label(frame_equipo, text="Lenguaje:").grid(row=2, column=0, sticky="w", pady=2)
        self.txt_lenguaje = tk.Entry(frame_equipo, width=25)
        self.txt_lenguaje.grid(row=2, column=1, pady=2)

        tk.Label(frame_equipo, text="Tamaño (2 o 3):").grid(row=3, column=0, sticky="w", pady=2)
        self.txt_tamano = tk.Entry(frame_equipo, width=25)
        self.txt_tamano.grid(row=3, column=1, pady=2)

        self.btn_crear_equipo = tk.Button(frame_equipo, text="Crear Equipo", command=self.crear_equipo)
        self.btn_crear_equipo.grid(row=4, column=0, columnspan=2, pady=8)

        frame_prog = tk.LabelFrame(self.ventana, text="2. Agregar Programador", padx=10, pady=10)
        frame_prog.pack(fill="x", padx=15, pady=5)

        tk.Label(frame_prog, text="Nombre:").grid(row=0, column=0, sticky="w", pady=2)
        self.txt_nombre = tk.Entry(frame_prog, width=25)
        self.txt_nombre.grid(row=0, column=1, pady=2)

        tk.Label(frame_prog, text="Apellidos:").grid(row=1, column=0, sticky="w", pady=2)
        self.txt_apellidos = tk.Entry(frame_prog, width=25)
        self.txt_apellidos.grid(row=1, column=1, pady=2)

        self.btn_agregar = tk.Button(frame_prog, text="Añadir al Equipo", command=self.agregar_programador)
        self.btn_agregar.grid(row=2, column=0, columnspan=2, pady=8)

        frame_estado = tk.LabelFrame(self.ventana, text="Estado del Equipo", padx=10, pady=10)
        frame_estado.pack(fill="both", expand=True, padx=15, pady=10)

        self.lbl_estado = tk.Label(frame_estado, text="Equipo no creado todavía.", justify="left")
        self.lbl_estado.pack(anchor="w")

    def crear_equipo(self):
        nombre = self.txt_equipo.get().strip()
        universidad = self.txt_universidad.get().strip()
        lenguaje = self.txt_lenguaje.get().strip()
        tamano_str = self.txt_tamano.get().strip()

        if not nombre or not universidad or not lenguaje or not tamano_str:
            messagebox.showwarning("Atención", "Todos los campos del equipo son obligatorios.")
            return

        try:
            tamano = int(tamano_str)
            self.equipo = EquipoMaratonProgramacion(nombre, universidad, lenguaje, tamano)
            messagebox.showinfo("Éxito", f"Equipo '{nombre}' inicializado para {tamano} miembros.")
            self.actualizar_vista()
        except ValueError as e:
            if "invalid literal" in str(e):
                messagebox.showerror("Error", "El tamaño debe ser un número entero.")
            else:
                messagebox.showerror("Error", str(e))

    def agregar_programador(self):
        if not self.equipo:
            messagebox.showwarning("Atención", "Primero debe crear el equipo.")
            return

        nombre = self.txt_nombre.get().strip()
        apellidos = self.txt_apellidos.get().strip()

        try:
            nuevo_programador = Programador(nombre, apellidos)
            self.equipo.anadir_programador(nuevo_programador)

            self.txt_nombre.delete(0, tk.END)
            self.txt_apellidos.delete(0, tk.END)

            messagebox.showinfo("Agregado", f"Se agregó a {nuevo_programador}.")
            self.actualizar_vista()

            if self.equipo.esta_completo():
                messagebox.showinfo("Completado", "¡El equipo ha alcanzado su cupo máximo!")

        except (ValueError, Exception) as error:
            messagebox.showerror("Error de validación", str(error))

    def actualizar_vista(self):
        if not self.equipo:
            return

        lineas = [
            f"Equipo: {self.equipo.nombre}",
            f"Universidad: {self.equipo.universidad}",
            f"Lenguaje: {self.equipo.lenguaje}",
            f"Miembros ({len(self.equipo.programadores)}/{self.equipo.tamano}):"
        ]

        for i, prog in enumerate(self.equipo.programadores, 1):
            lineas.append(f"  {i}. {prog}")

        if self.equipo.esta_completo():
            lineas.append("\nEstado: Completo")
        else:
            lineas.append(f"\nEstado: Faltan {self.equipo.tamano - len(self.equipo.programadores)} integrante(s)")

        self.lbl_estado.config(text="\n".join(lineas))

    def iniciar(self):
        self.ventana.mainloop()


app = VentanaMaraton()
app.iniciar()
