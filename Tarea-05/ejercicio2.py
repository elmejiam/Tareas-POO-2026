from datetime import datetime
import tkinter as tk
from tkinter import messagebox


class Huesped:
    def __init__(self, nombres, apellidos, documento_identidad):
        self.nombres = nombres
        self.apellidos = apellidos
        self.documento_identidad = documento_identidad
        self.fecha_ingreso = None
        self.fecha_salida = None

    def obtener_dias_alojamiento(self):
        diferencia = self.fecha_salida - self.fecha_ingreso
        return diferencia.days


class Habitacion:
    def __init__(self, numero, disponible, precio_dia):
        self.numero = numero
        self.disponible = disponible
        self.precio_dia = precio_dia
        self.huesped = None


class Hotel:
    def __init__(self):
        self.lista_habitaciones = []
        for i in range(1, 11):
            precio = 120000 if i <= 5 else 160000
            self.lista_habitaciones.append(Habitacion(i, True, precio))

    def buscar_habitacion(self, numero):
        for habitacion in self.lista_habitaciones:
            if habitacion.numero == numero:
                return habitacion
        return None


class VentanaIngreso:
    def __init__(self, padre, hotel, numero_habitacion, callback_actualizar=None):
        self.hotel = hotel
        self.habitacion = hotel.buscar_habitacion(numero_habitacion)
        self.callback_actualizar = callback_actualizar

        self.ventana = tk.Toplevel(padre)
        self.ventana.title("Ingreso")
        self.ventana.geometry("350x300")
        self.ventana.resizable(False, False)
        self.ventana.grab_set()

        frame = tk.Frame(self.ventana, padx=15, pady=15)
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text=f"Habitación: {self.habitacion.numero}", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))

        tk.Label(frame, text="Fecha (aaaa-mm-dd):").grid(row=1, column=0, sticky="w", pady=5)
        self.txt_fecha = tk.Entry(frame, width=20)
        self.txt_fecha.grid(row=1, column=1, pady=5)

        tk.Label(frame, text="Huésped", font=("Arial", 9, "bold")).grid(row=2, column=0, columnspan=2, sticky="w", pady=(10, 5))

        tk.Label(frame, text="Nombre:").grid(row=3, column=0, sticky="w", pady=5)
        self.txt_nombre = tk.Entry(frame, width=20)
        self.txt_nombre.grid(row=3, column=1, pady=5)

        tk.Label(frame, text="Apellidos:").grid(row=4, column=0, sticky="w", pady=5)
        self.txt_apellidos = tk.Entry(frame, width=20)
        self.txt_apellidos.grid(row=4, column=1, pady=5)

        tk.Label(frame, text="Doc. Identidad:").grid(row=5, column=0, sticky="w", pady=5)
        self.txt_documento = tk.Entry(frame, width=20)
        self.txt_documento.grid(row=5, column=1, pady=5)

        frame_botones = tk.Frame(frame)
        frame_botones.grid(row=6, column=0, columnspan=2, pady=15)

        btn_aceptar = tk.Button(frame_botones, text="Aceptar", width=11, command=self.registrar_ingreso)
        btn_aceptar.pack(side="left", padx=8)

        btn_cancelar = tk.Button(frame_botones, text="Cancelar", width=11, command=self.ventana.destroy)
        btn_cancelar.pack(side="left", padx=8)

    def registrar_ingreso(self):
        fecha_texto = self.txt_fecha.get().strip()
        nombre = self.txt_nombre.get().strip()
        apellidos = self.txt_apellidos.get().strip()
        documento_texto = self.txt_documento.get().strip()

        if not fecha_texto or not nombre or not apellidos or not documento_texto:
            messagebox.showerror("Error", "Campo nulo o vacío. Todos los campos son obligatorios.", parent=self.ventana)
            return

        try:
            fecha_ingreso = datetime.strptime(fecha_texto, "%Y-%m-%d").date()
        except ValueError:
            messagebox.showerror("Error", "La fecha no está en el formato solicitado (aaaa-mm-dd).", parent=self.ventana)
            return

        try:
            documento = int(documento_texto)
        except ValueError:
            messagebox.showerror("Error", "El documento de identidad debe ser un valor numérico.", parent=self.ventana)
            return

        huesped = Huesped(nombre, apellidos, documento)
        huesped.fecha_ingreso = fecha_ingreso

        self.habitacion.huesped = huesped
        self.habitacion.disponible = False

        messagebox.showinfo("Mensaje", "El huésped ha sido registrado.", parent=self.ventana)
        if self.callback_actualizar:
            self.callback_actualizar()
        self.ventana.destroy()


class VentanaHabitaciones:
    def __init__(self, padre, hotel):
        self.hotel = hotel
        self.ventana = tk.Toplevel(padre)
        self.ventana.title("Habitaciones")
        self.ventana.geometry("620x290")
        self.ventana.resizable(False, False)
        self.ventana.grab_set()

        frame_grid = tk.Frame(self.ventana, padx=15, pady=15)
        frame_grid.pack(fill="both", expand=True)

        self.labels_estado = {}

        for indice, hab in enumerate(self.hotel.lista_habitaciones):
            fila = 0 if indice < 5 else 1
            columna = indice if indice < 5 else indice - 5

            celda = tk.Frame(frame_grid, bd=1, relief="groove", padx=8, pady=8)
            celda.grid(row=fila, column=columna, padx=5, pady=5, sticky="nsew")

            tk.Label(celda, text=f"Habitación {hab.numero}", font=("Arial", 9, "bold")).pack()
            estado_texto = "Disponible" if hab.disponible else "No disponible"
            color_texto = "green" if hab.disponible else "red"
            lbl_estado = tk.Label(celda, text=estado_texto, fg=color_texto)
            lbl_estado.pack(pady=(4, 0))
            self.labels_estado[hab.numero] = lbl_estado

        frame_inferior = tk.Frame(self.ventana, pady=12)
        frame_inferior.pack(fill="x")

        tk.Label(frame_inferior, text="Habitación a reservar:").pack(side="left", padx=(65, 8))
        self.spn_habitacion = tk.Spinbox(frame_inferior, from_=1, to=10, width=8)
        self.spn_habitacion.pack(side="left", padx=8)

        btn_aceptar = tk.Button(frame_inferior, text="Aceptar", width=12, command=self.seleccionar_habitacion)
        btn_aceptar.pack(side="left", padx=15)

    def actualizar_estados(self):
        for hab in self.hotel.lista_habitaciones:
            lbl = self.labels_estado[hab.numero]
            if hab.disponible:
                lbl.config(text="Disponible", fg="green")
            else:
                lbl.config(text="No disponible", fg="red")

    def seleccionar_habitacion(self):
        try:
            numero = int(self.spn_habitacion.get().strip())
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número de habitación válido.", parent=self.ventana)
            return

        habitacion = self.hotel.buscar_habitacion(numero)
        if not habitacion:
            messagebox.showerror("Error", "El número de habitación debe estar entre 1 y 10.", parent=self.ventana)
            return

        if not habitacion.disponible:
            messagebox.showinfo("Mensaje", "La habitación está ocupada.", parent=self.ventana)
            return

        VentanaIngreso(self.ventana, self.hotel, numero, self.actualizar_estados)


class VentanaSalida:
    def __init__(self, padre, hotel, numero_habitacion):
        self.hotel = hotel
        self.habitacion = hotel.buscar_habitacion(numero_habitacion)

        self.ventana = tk.Toplevel(padre)
        self.ventana.title("Salida huéspedes")
        self.ventana.geometry("330x290")
        self.ventana.resizable(False, False)
        self.ventana.grab_set()

        frame = tk.Frame(self.ventana, padx=20, pady=15)
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text=f"Habitación: {self.habitacion.numero}", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=2, sticky="w", pady=4)
        tk.Label(frame, text=f"Fecha de ingreso: {self.habitacion.huesped.fecha_ingreso}").grid(row=1, column=0, columnspan=2, sticky="w", pady=4)

        tk.Label(frame, text="Fecha de salida (aaaa-mm-dd):").grid(row=2, column=0, sticky="w", pady=(10, 4))
        self.txt_fecha_salida = tk.Entry(frame, width=14)
        self.txt_fecha_salida.grid(row=2, column=1, pady=(10, 4))

        btn_calcular = tk.Button(frame, text="Calcular", width=18, command=self.calcular_total)
        btn_calcular.grid(row=3, column=0, columnspan=2, pady=10)

        self.lbl_dias = tk.Label(frame, text="Cantidad de días: ")
        self.lbl_dias.grid(row=4, column=0, columnspan=2, sticky="w", pady=4)

        self.lbl_total = tk.Label(frame, text="Total: $", font=("Arial", 9, "bold"))
        self.lbl_total.grid(row=5, column=0, columnspan=2, sticky="w", pady=4)

        self.btn_registrar_salida = tk.Button(
            frame,
            text="Registrar salida",
            width=18,
            state="disabled",
            command=self.registrar_salida
        )
        self.btn_registrar_salida.grid(row=6, column=0, columnspan=2, pady=14)

    def calcular_total(self):
        fecha_texto = self.txt_fecha_salida.get().strip()
        if not fecha_texto:
            messagebox.showerror("Error", "Debe ingresar la fecha de salida.", parent=self.ventana)
            return

        try:
            fecha_salida = datetime.strptime(fecha_texto, "%Y-%m-%d").date()
        except ValueError:
            messagebox.showerror("Error", "La fecha no está en el formato solicitado (aaaa-mm-dd).", parent=self.ventana)
            return

        fecha_ingreso = self.habitacion.huesped.fecha_ingreso
        if fecha_salida <= fecha_ingreso:
            messagebox.showerror("Mensaje", "La fecha de salida es menor o igual que la de ingreso.", parent=self.ventana)
            self.btn_registrar_salida.config(state="disabled")
            return

        self.habitacion.huesped.fecha_salida = fecha_salida
        dias = self.habitacion.huesped.obtener_dias_alojamiento()
        total = dias * self.habitacion.precio_dia

        self.lbl_dias.config(text=f"Cantidad de días: {dias}")
        self.lbl_total.config(text=f"Total: ${total}")
        self.btn_registrar_salida.config(state="normal")

    def registrar_salida(self):
        self.habitacion.huesped = None
        self.habitacion.disponible = True
        messagebox.showinfo("Mensaje", "Se ha registrado la salida del huésped.", parent=self.ventana)
        self.ventana.destroy()


class VentanaSolicitarSalida:
    def __init__(self, padre, hotel):
        self.hotel = hotel
        self.ventana = tk.Toplevel(padre)
        self.ventana.title("Salida de huéspedes")
        self.ventana.geometry("300x140")
        self.ventana.resizable(False, False)
        self.ventana.grab_set()

        frame = tk.Frame(self.ventana, padx=15, pady=15)
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="Número de habitación a entregar:").pack(pady=(0, 8))
        self.txt_numero = tk.Entry(frame, width=15)
        self.txt_numero.pack(pady=4)

        btn_aceptar = tk.Button(frame, text="Aceptar", width=12, command=self.validar_habitacion)
        btn_aceptar.pack(pady=10)

    def validar_habitacion(self):
        texto = self.txt_numero.get().strip()
        try:
            numero = int(texto)
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número.", parent=self.ventana)
            return

        habitacion = self.hotel.buscar_habitacion(numero)
        if not habitacion:
            messagebox.showinfo("Mensaje", "El número de habitación debe estar entre 1 y 10.", parent=self.ventana)
            return

        if habitacion.disponible:
            messagebox.showinfo("Mensaje", "La habitación no está ocupada.", parent=self.ventana)
            return

        self.ventana.destroy()
        VentanaSalida(self.ventana.master, self.hotel, numero)


class VentanaPrincipal:
    def __init__(self):
        self.hotel = Hotel()
        self.ventana = tk.Tk()
        self.ventana.title("Hotel")
        self.ventana.geometry("340x240")
        self.ventana.resizable(False, False)

        barra_menu = tk.Menu(self.ventana)
        menu_opciones = tk.Menu(barra_menu, tearoff=0)
        menu_opciones.add_command(label="Consultar habitaciones", command=self.abrir_consultar_habitaciones)
        menu_opciones.add_command(label="Salida de huéspedes", command=self.abrir_salida_huespedes)

        barra_menu.add_cascade(label="Menú", menu=menu_opciones)
        self.ventana.config(menu=barra_menu)

        lbl_info = tk.Label(
            self.ventana,
            text="Gestión de Hotel\n\nUse el menú superior para consultar\nhabitaciones o registrar salidas.",
            font=("Arial", 10)
        )
        lbl_info.pack(expand=True)

    def abrir_consultar_habitaciones(self):
        VentanaHabitaciones(self.ventana, self.hotel)

    def abrir_salida_huespedes(self):
        VentanaSolicitarSalida(self.ventana, self.hotel)

    def iniciar(self):
        self.ventana.mainloop()


app = VentanaPrincipal()
app.iniciar()

