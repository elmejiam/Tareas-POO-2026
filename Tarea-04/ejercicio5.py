import os
import tkinter as tk
from tkinter import filedialog, messagebox


class LectorArchivo:
    def __init__(self, ruta_archivo="prueba.txt"):
        self.ruta_archivo = ruta_archivo

    def leer_contenido(self):
        if not os.path.exists(self.ruta_archivo):
            raise FileNotFoundError(f"No se encontró el archivo: {self.ruta_archivo}")

        # Lectura mediante flujo de bytes (equivalente a FileInputStream + InputStreamReader)
        try:
            with open(self.ruta_archivo, "rb") as flujo_bytes:
                contenido_bytes = flujo_bytes.read()
                return contenido_bytes.decode("utf-8")
        except UnicodeDecodeError:
            # Fallback en caso de codificación distinta
            return contenido_bytes.decode("latin-1")
        except IOError as error:
            raise IOError(f"Error de entrada/salida al leer el archivo: {error}")


class VentanaLector:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Lectura de Archivo")
        self.ventana.geometry("480x420")

        frame_control = tk.Frame(self.ventana, padx=10, pady=10)
        frame_control.pack(fill="x")

        tk.Label(frame_control, text="Ruta del archivo:").pack(anchor="w")

        frame_input = tk.Frame(frame_control)
        frame_input.pack(fill="x", pady=5)

        self.txt_ruta = tk.Entry(frame_input)
        self.txt_ruta.insert(0, "prueba.txt")
        self.txt_ruta.pack(side="left", fill="x", expand=True, padx=(0, 5))

        self.btn_buscar = tk.Button(frame_input, text="Examinar...", command=self.seleccionar_archivo)
        self.btn_buscar.pack(side="right")

        frame_botones = tk.Frame(frame_control)
        frame_botones.pack(pady=5)

        self.btn_leer = tk.Button(frame_botones, text="Leer Archivo", command=self.cargar_archivo)
        self.btn_leer.pack(side="left", padx=5)

        self.btn_crear_ejemplo = tk.Button(
            frame_botones,
            text="Crear prueba.txt de muestra",
            command=self.crear_archivo_muestra
        )
        self.btn_crear_ejemplo.pack(side="left", padx=5)

        frame_texto = tk.LabelFrame(self.ventana, text="Contenido del archivo", padx=10, pady=10)
        frame_texto.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        self.caja_texto = tk.Text(frame_texto, wrap="word")
        self.caja_texto.pack(fill="both", expand=True)

    def seleccionar_archivo(self):
        ruta = filedialog.askopenfilename(
            title="Seleccionar archivo de texto",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        if ruta:
            self.txt_ruta.delete(0, tk.END)
            self.txt_ruta.insert(0, ruta)

    def crear_archivo_muestra(self):
        try:
            with open("prueba.txt", "wb") as f:
                f.write("Línea 1: Archivo de texto leído como flujo de bytes.\n".encode("utf-8"))
                f.write("Línea 2: Ejercicio 6.8 de POO y excepciones.\n".encode("utf-8"))
                f.write("Línea 3: Flujo completado exitosamente.".encode("utf-8"))
            self.txt_ruta.delete(0, tk.END)
            self.txt_ruta.insert(0, "prueba.txt")
            messagebox.showinfo("Listo", "Se generó 'prueba.txt' en la carpeta actual.")
        except IOError as e:
            messagebox.showerror("Error", f"No se pudo crear el archivo: {e}")

    def cargar_archivo(self):
        ruta = self.txt_ruta.get().strip()
        if not ruta:
            messagebox.showwarning("Atención", "Especifique una ruta de archivo.")
            return

        lector = LectorArchivo(ruta)
        try:
            contenido = lector.leer_contenido()
            self.caja_texto.delete("1.0", tk.END)
            self.caja_texto.insert(tk.END, contenido)
        except (FileNotFoundError, IOError) as error_io:
            self.caja_texto.delete("1.0", tk.END)
            messagebox.showerror("IOException", str(error_io))

    def iniciar(self):
        self.ventana.mainloop()


app = VentanaLector()
app.iniciar()
