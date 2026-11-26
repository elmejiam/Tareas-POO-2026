import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog


class Empleado:
    def __init__(self, nombre, apellidos, cargo, genero, salario_dia, dias_trabajados, otros_ingresos, pagos_salud, aporte_pensiones):
        self.nombre = nombre
        self.apellidos = apellidos
        self.cargo = cargo
        self.genero = genero
        self.salario_dia = salario_dia
        self.dias_trabajados = dias_trabajados
        self.otros_ingresos = otros_ingresos
        self.pagos_salud = pagos_salud
        self.aporte_pensiones = aporte_pensiones

    def calcular_sueldo(self):
        return (self.dias_trabajados * self.salario_dia) + self.otros_ingresos - self.pagos_salud - self.aporte_pensiones


class ListaEmpleados:
    def __init__(self):
        self.lista = []

    def agregar_empleado(self, empleado):
        self.lista.append(empleado)

    def calcular_total_nomina(self):
        total = 0
        for emp in self.lista:
            total += emp.calcular_sueldo()
        return total

    def convertir_texto(self):
        texto = ""
        for emp in self.lista:
            texto += f"Nombre = {emp.nombre}\n"
            texto += f"Apellidos = {emp.apellidos}\n"
            texto += f"Cargo = {emp.cargo}\n"
            texto += f"Género = {emp.genero}\n"
            texto += f"Salario = ${emp.salario_dia:.2f}\n"
            texto += f"Días trabajados = {emp.dias_trabajados}\n"
            texto += f"Otros ingresos = ${emp.otros_ingresos:.2f}\n"
            texto += f"Pagos salud = ${emp.pagos_salud:.2f}\n"
            texto += f"Aportes pensiones = ${emp.aporte_pensiones:.2f}\n"
            texto += f"Sueldo mensual = ${emp.calcular_sueldo():.2f}\n"
            texto += "---------\n"
        texto += f"Total nómina = ${self.calcular_total_nomina():.2f}\n"
        return texto


class VentanaAgregarEmpleado:
    def __init__(self, padre, lista_empleados):
        self.lista_empleados = lista_empleados
        self.ventana = tk.Toplevel(padre)
        self.ventana.title("Agregar Empleado")
        self.ventana.geometry("360x440")
        self.ventana.resizable(False, False)
        self.ventana.grab_set()

        tk.Label(self.ventana, text="Nombre:").grid(row=0, column=0, sticky="w", padx=15, pady=6)
        self.txt_nombre = tk.Entry(self.ventana, width=22)
        self.txt_nombre.grid(row=0, column=1, pady=6)

        tk.Label(self.ventana, text="Apellidos:").grid(row=1, column=0, sticky="w", padx=15, pady=6)
        self.txt_apellidos = tk.Entry(self.ventana, width=22)
        self.txt_apellidos.grid(row=1, column=1, pady=6)

        tk.Label(self.ventana, text="Cargo:").grid(row=2, column=0, sticky="nw", padx=15, pady=6)
        self.lista_cargo = tk.Listbox(self.ventana, height=3, width=22, exportselection=False)
        for cargo in ["Directivo", "Estratégico", "Operativo"]:
            self.lista_cargo.insert(tk.END, cargo)
        self.lista_cargo.selection_set(0)
        self.lista_cargo.grid(row=2, column=1, pady=6)

        tk.Label(self.ventana, text="Género:").grid(row=3, column=0, sticky="w", padx=15, pady=6)
        frame_genero = tk.Frame(self.ventana)
        frame_genero.grid(row=3, column=1, sticky="w", pady=6)
        self.var_masculino = tk.BooleanVar(value=True)
        self.var_femenino = tk.BooleanVar(value=False)
        self.chk_masculino = tk.Checkbutton(frame_genero, text="Masculino", variable=self.var_masculino, command=self.seleccionar_masculino)
        self.chk_masculino.pack(side="left")
        self.chk_femenino = tk.Checkbutton(frame_genero, text="Femenino", variable=self.var_femenino, command=self.seleccionar_femenino)
        self.chk_femenino.pack(side="left")

        tk.Label(self.ventana, text="Salario por día:").grid(row=4, column=0, sticky="w", padx=15, pady=6)
        self.txt_salario = tk.Entry(self.ventana, width=22)
        self.txt_salario.grid(row=4, column=1, pady=6)

        tk.Label(self.ventana, text="Días trabajados:").grid(row=5, column=0, sticky="w", padx=15, pady=6)
        self.spn_dias = tk.Spinbox(self.ventana, from_=1, to=31, width=20)
        self.spn_dias.grid(row=5, column=1, pady=6)

        tk.Label(self.ventana, text="Otros ingresos:").grid(row=6, column=0, sticky="w", padx=15, pady=6)
        self.txt_otros = tk.Entry(self.ventana, width=22)
        self.txt_otros.grid(row=6, column=1, pady=6)

        tk.Label(self.ventana, text="Pagos por salud:").grid(row=7, column=0, sticky="w", padx=15, pady=6)
        self.txt_salud = tk.Entry(self.ventana, width=22)
        self.txt_salud.grid(row=7, column=1, pady=6)

        tk.Label(self.ventana, text="Aporte pensiones:").grid(row=8, column=0, sticky="w", padx=15, pady=6)
        self.txt_pensiones = tk.Entry(self.ventana, width=22)
        self.txt_pensiones.grid(row=8, column=1, pady=6)

        frame_botones = tk.Frame(self.ventana)
        frame_botones.grid(row=9, column=0, columnspan=2, pady=15)

        btn_agregar = tk.Button(frame_botones, text="Agregar", width=12, command=self.guardar_empleado)
        btn_agregar.pack(side="left", padx=10)

        btn_limpiar = tk.Button(frame_botones, text="Limpiar", width=12, command=self.limpiar_campos)
        btn_limpiar.pack(side="left", padx=10)

    def seleccionar_masculino(self):
        if self.var_masculino.get():
            self.var_femenino.set(False)
        else:
            self.var_femenino.set(True)

    def seleccionar_femenino(self):
        if self.var_femenino.get():
            self.var_masculino.set(False)
        else:
            self.var_masculino.set(True)

    def limpiar_campos(self):
        self.txt_nombre.delete(0, tk.END)
        self.txt_apellidos.delete(0, tk.END)
        self.lista_cargo.selection_clear(0, tk.END)
        self.lista_cargo.selection_set(0)
        self.var_masculino.set(True)
        self.var_femenino.set(False)
        self.txt_salario.delete(0, tk.END)
        self.spn_dias.delete(0, tk.END)
        self.spn_dias.insert(0, "1")
        self.txt_otros.delete(0, tk.END)
        self.txt_salud.delete(0, tk.END)
        self.txt_pensiones.delete(0, tk.END)

    def guardar_empleado(self):
        nombre = self.txt_nombre.get().strip()
        apellidos = self.txt_apellidos.get().strip()

        if not nombre or not apellidos:
            messagebox.showwarning("Campo vacío", "El nombre y los apellidos son obligatorios.", parent=self.ventana)
            return

        seleccion = self.lista_cargo.curselection()
        if not seleccion:
            messagebox.showwarning("Selección", "Debe seleccionar un cargo.", parent=self.ventana)
            return
        cargo = self.lista_cargo.get(seleccion[0])

        genero = "Masculino" if self.var_masculino.get() else "Femenino"

        try:
            salario_dia = float(self.txt_salario.get().strip())
            dias_trabajados = int(self.spn_dias.get().strip())
            otros_ingresos = float(self.txt_otros.get().strip())
            pagos_salud = float(self.txt_salud.get().strip())
            aporte_pensiones = float(self.txt_pensiones.get().strip())

            if dias_trabajados < 1 or dias_trabajados > 31:
                messagebox.showerror("Error", "Los días trabajados deben estar entre 1 y 31.", parent=self.ventana)
                return

            empleado = Empleado(
                nombre, apellidos, cargo, genero,
                salario_dia, dias_trabajados, otros_ingresos,
                pagos_salud, aporte_pensiones
            )
            self.lista_empleados.agregar_empleado(empleado)
            messagebox.showinfo("Mensaje", "El empleado ha sido agregado.", parent=self.ventana)
            self.limpiar_campos()

        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número.", parent=self.ventana)


class VentanaNomina:
    def __init__(self, padre, lista_empleados):
        self.lista_empleados = lista_empleados
        self.ventana = tk.Toplevel(padre)
        self.ventana.title("Nómina de Empleados")
        self.ventana.geometry("450x340")
        self.ventana.resizable(False, False)
        self.ventana.grab_set()

        tk.Label(self.ventana, text="Empleados registrados:", font=("Arial", 10, "bold")).pack(pady=(12, 8))

        columnas = ("nombre", "apellidos", "sueldo")
        self.tabla = ttk.Treeview(self.ventana, columns=columnas, show="headings", height=9)
        self.tabla.heading("nombre", text="NOMBRE")
        self.tabla.heading("apellidos", text="APELLIDOS")
        self.tabla.heading("sueldo", text="SUELDO")

        self.tabla.column("nombre", width=130, anchor="center")
        self.tabla.column("apellidos", width=150, anchor="center")
        self.tabla.column("sueldo", width=120, anchor="center")
        self.tabla.pack(padx=15)

        for emp in self.lista_empleados.lista:
            self.tabla.insert("", tk.END, values=(emp.nombre, emp.apellidos, f"${emp.calcular_sueldo():.2f}"))

        total = self.lista_empleados.calcular_total_nomina()
        lbl_total = tk.Label(self.ventana, text=f"Total nómina mensual = $ {total:.2f}", font=("Arial", 11, "bold"))
        lbl_total.pack(pady=15)


class VentanaPrincipal:
    def __init__(self):
        self.empleados = ListaEmpleados()
        self.ventana = tk.Tk()
        self.ventana.title("Nómina")
        self.ventana.geometry("380x280")
        self.ventana.resizable(False, False)

        barra_menu = tk.Menu(self.ventana)
        menu_opciones = tk.Menu(barra_menu, tearoff=0)
        menu_opciones.add_command(label="Agregar empleado", command=self.abrir_agregar_empleado)
        menu_opciones.add_command(label="Calcular nómina", command=self.abrir_calcular_nomina)
        menu_opciones.add_separator()
        menu_opciones.add_command(label="Guardar archivo", command=self.guardar_archivo)

        barra_menu.add_cascade(label="Menú", menu=menu_opciones)
        self.ventana.config(menu=barra_menu)

        lbl_bienvenida = tk.Label(
            self.ventana,
            text="Sistema de Gestión de Nómina\n\nSeleccione una opción en el menú superior.",
            font=("Arial", 11)
        )
        lbl_bienvenida.pack(expand=True)

    def abrir_agregar_empleado(self):
        VentanaAgregarEmpleado(self.ventana, self.empleados)

    def abrir_calcular_nomina(self):
        if not self.empleados.lista:
            messagebox.showinfo("Nómina", "No hay empleados registrados todavía.")
            return
        VentanaNomina(self.ventana, self.empleados)

    def guardar_archivo(self):
        if not self.empleados.lista:
            messagebox.showwarning("Advertencia", "No hay datos de empleados para guardar.")
            return

        carpeta = filedialog.askdirectory(title="Seleccione la carpeta donde guardar la nómina")
        if carpeta:
            ruta_archivo = os.path.join(carpeta, "Nómina.txt")
            try:
                with open(ruta_archivo, "w", encoding="utf-8") as archivo:
                    archivo.write(self.empleados.convertir_texto())
                messagebox.showinfo("Mensaje", f"El archivo de la nómina Nómina.txt se ha creado en {carpeta}")
            except IOError:
                messagebox.showerror("Error", "No se pudo guardar el archivo en la carpeta seleccionada.")

    def iniciar(self):
        self.ventana.mainloop()


app = VentanaPrincipal()
app.iniciar()
