import tkinter as tk
from tkinter import ttk, scrolledtext, colorchooser, filedialog, messagebox
from PIL import Image, ImageTk
from datetime import datetime
import os

DIRECTORIO_BASE = os.path.dirname(os.path.abspath(__file__))

ANCHO_PANTALLA = 1024
ALTO_PANTALLA = 768
ALTURA_BARRA_TAREAS = 50
COLOR_FONDO = "#667eea"

# ==================== CLASES DE APLICACIONES ====================


class Calculadora:

    def __init__(self, padre):
        #  Contenedor para display de la calculadora
        self.ventana = tk.Toplevel(padre)
        self.ventana.title("Calculadora")
        self.ventana.geometry("320x480")
        self.ventana.resizable(False, False)


        self.variable_pantalla = tk.StringVar(value="0")

        pantalla = tk.Entry(
            self.ventana,
            textvariable=self.variable_pantalla,
            font=("Courier", 24),
            justify="right",
            bd=10,
        )
        pantalla.pack(fill=tk.X, padx=5, pady=5)

        # Tablero de la calculadora
        botones = [
            ["C", "←", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "="],
        ]

        for fila in botones:
            marco = tk.Frame(self.ventana)
            marco.pack(fill=tk.BOTH, expand=True, padx=5, pady=2)
            for boton in fila:
                ancho = 2 if boton != "=" else 4
                color_fondo = "#ff9500" if boton in ["+", "-", "*", "/", "="] else "#f0f0f0"
                tk.Button(
                    marco,
                    text=boton,
                    font=("Arial", 16),
                    width=ancho,
                    command=lambda b=boton: self.clic(b),
                    bg=color_fondo,
                ).pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=2)

    def clic(self, tecla):
        actual = self.variable_pantalla.get()
        if tecla == "C":
            self.variable_pantalla.set("0")
        elif tecla == "←":
            self.variable_pantalla.set(actual[:-1] or "0")
        elif tecla == "=":
            try:
                resultado = eval(actual)
                self.variable_pantalla.set(str(resultado))
            except:
                self.variable_pantalla.set("Error")
        else:
            if actual == "0" or actual == "Error":
                self.variable_pantalla.set(tecla)
            else:
                self.variable_pantalla.set(actual + tecla)


class BlocNotas:

    def __init__(self, padre):
        self.ventana = tk.Toplevel(padre)
        self.ventana.title("Bloc de Notas")
        self.ventana.geometry("600x500")
        self.archivo_actual = None

        # Barra de tareas donde controlo el funcionamiento del bloc de notas 
        barra_herramientas = tk.Frame(self.ventana, bg="#f0f0f0")
        barra_herramientas.pack(fill=tk.X)

        tk.Button(barra_herramientas, text="Nuevo", command=self.nuevo_archivo).pack(
            side=tk.LEFT, padx=2, pady=2
        )
        tk.Button(barra_herramientas, text="Abrir", command=self.abrir_archivo).pack(
            side=tk.LEFT, padx=2, pady=2
        )
        tk.Button(barra_herramientas, text="Guardar", command=self.guardar_archivo).pack(
            side=tk.LEFT, padx=2, pady=2
        )

        self.texto = scrolledtext.ScrolledText(self.ventana, font=("Consolas", 11))
        self.texto.pack(fill=tk.BOTH, expand=True)

        self.texto.bind("<Control-s>", lambda e: self.guardar_archivo())
        self.texto.bind("<Control-o>", lambda e: self.abrir_archivo())

    def nuevo_archivo(self):
        self.texto.delete("1.0", tk.END)
        self.archivo_actual = None
        self.ventana.title("Bloc de Notas - Nuevo")

    def abrir_archivo(self):
        archivo = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if archivo:
            with open(archivo, "r", encoding="utf-8") as f:
                self.texto.delete("1.0", tk.END)
                self.texto.insert("1.0", f.read())
            self.archivo_actual = archivo
            self.ventana.title(f"Bloc de Notas - {os.path.basename(archivo)}")

    def guardar_archivo(self):
        if not self.archivo_actual:
            self.archivo_actual = filedialog.asksaveasfilename(
                defaultextension=".txt", filetypes=[("Text files", "*.txt")]
            )
        if self.archivo_actual:
            try:
                with open(self.archivo_actual, "w", encoding="utf-8") as f:
                    f.write(self.texto.get("1.0", tk.END))
                messagebox.showinfo("Guardado", "Archivo guardado correctamente")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar: {e}")


class Configuracion:

# Ajustes para cambiar color de fondo de pantalla o añadir imagen para el fondo
    def __init__(self, padre, escritorio):
        self.ventana = tk.Toplevel(padre)
        self.ventana.title("Configuración")
        self.ventana.geometry("650x800")
        self.escritorio = escritorio
        
        # Crear canvas con scrollbar para que todo quepa
        canvas = tk.Canvas(self.ventana)
        scrollbar = tk.Scrollbar(self.ventana, orient="vertical", command=canvas.yview)
        self.marco_contenido = tk.Frame(canvas)
        
        self.marco_contenido.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.marco_contenido, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Ahora usamos self.marco_contenido en lugar de self.ventana para los widgets

        # Sección colores
        tk.Label(self.marco_contenido, text="Colores Sólidos", font=("Arial", 14, "bold")).pack(
            pady=10
        )

        # Colores a elegir para el fondo
        colores = [
            ("#2b5797", "Azul"),
            ("#1e1e1e", "Negro"),
            ("#4a148c", "Púrpura"),
            ("#0d47a1", "Azul Oscuro"),
            ("#1b5e20", "Verde"),
            ("#b71c1c", "Rojo"),
        ]

        marco = tk.Frame(self.marco_contenido)
        marco.pack(pady=10)
        for i, (color, nombre) in enumerate(colores):
            boton = tk.Button(
                marco,
                bg=color,
                width=10,
                height=2,
                command=lambda c=color: escritorio.establecer_fondo(c),
            )
            boton.grid(row=i // 3, column=i % 3, padx=5, pady=5)

        # Selector personalizado

        tk.Button(
            self.marco_contenido, text="Elegir Color Personalizado", command=self.elegir_color
        ).pack(pady=10)

        # Selector para importar imagen de fondo
        tk.Label(
            self.marco_contenido, text="Fondos de Pantalla", font=("Arial", 14, "bold")
        ).pack(pady=10)
        
        tk.Label(
            self.marco_contenido, text="Haz clic en una imagen para establecerla como fondo", 
            font=("Arial", 9), fg="gray"
        ).pack(pady=(0, 10))

        # Cargar todos los wallpapers disponibles en la carpeta
        carpeta_wallpapers = os.path.join(DIRECTORIO_BASE, "resources", "wallpapers")
        marco_fondos = tk.Frame(self.marco_contenido, bg="#f0f0f0", relief=tk.SUNKEN, bd=2)
        marco_fondos.pack(pady=10, padx=10)

        # Obtener todas las imágenes de la carpeta wallpapers
        if os.path.exists(carpeta_wallpapers):
            archivos_imagenes = [f for f in os.listdir(carpeta_wallpapers) 
                                if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
            
            if archivos_imagenes:
                for i, archivo in enumerate(archivos_imagenes):
                    ruta_completa = os.path.join(carpeta_wallpapers, archivo)
                    try:
                        # Crear miniatura con mejor calidad
                        imagen = Image.open(ruta_completa)
                        imagen.thumbnail((180, 120), Image.Resampling.LANCZOS)
                        foto = ImageTk.PhotoImage(imagen)
                        
                        # Botón con borde visible y efecto
                        boton = tk.Button(
                            marco_fondos,
                            image=foto,
                            command=lambda p=ruta_completa: escritorio.establecer_fondo(p),
                            relief=tk.RAISED,
                            bd=3,
                            bg="white",
                            activebackground="#e0e0e0",
                            cursor="hand2",
                            width=180,
                            height=120
                        )
                        boton.image = foto  # Mantener referencia
                        boton.grid(row=i // 3, column=i % 3, padx=8, pady=8)
                        
                        # Tooltip con nombre del archivo
                        def crear_tooltip(widget, texto):
                            def mostrar(event):
                                widget.config(relief=tk.SUNKEN)
                            def ocultar(event):
                                widget.config(relief=tk.RAISED)
                            widget.bind("<Enter>", mostrar)
                            widget.bind("<Leave>", ocultar)
                        
                        crear_tooltip(boton, archivo)
                        
                    except Exception as e:
                        print(f"Error cargando {archivo}: {e}")
            else:
                tk.Label(
                    marco_fondos, 
                    text="No se encontraron imágenes en la carpeta wallpapers",
                    fg="red"
                ).pack(pady=20)
        else:
            tk.Label(
                marco_fondos, 
                text="Carpeta wallpapers no encontrada",
                fg="red"
            ).pack(pady=20)

        # Cargar imagen
        tk.Button(
            self.marco_contenido, text="📁 Cargar Imagen Personalizada", command=self.cargar_imagen
        ).pack(pady=10)

    def elegir_color(self):
        color = colorchooser.askcolor(title="Elegir color")[1]
        if color:
            self.escritorio.establecer_fondo(color)

    def cargar_imagen(self):
        archivo = filedialog.askopenfilename(
            filetypes=[("Images", "*.png *.jpg *.jpeg *.bmp")]
        )
        if archivo:
            self.escritorio.establecer_fondo(archivo)


class Reloj:

    def __init__(self, padre):
        self.ventana = tk.Toplevel(padre)
        self.ventana.title("Reloj Digital")
        self.ventana.geometry("400x250")

     
        self.etiqueta_hora = tk.Label(
            self.ventana, font=("Courier", 48, "bold"), fg="white", bg="#667eea"
        )
        self.etiqueta_hora.pack(fill=tk.X, pady=20)

        self.etiqueta_fecha = tk.Label(
            self.ventana, font=("Arial", 14), fg="white", bg="#667eea"
        )
        self.etiqueta_fecha.pack()

        self.actualizar_reloj()

    def actualizar_reloj(self):
        ahora = datetime.now()
        self.etiqueta_hora.config(text=ahora.strftime("%H:%M:%S"))
        self.etiqueta_fecha.config(text=ahora.strftime("%A, %d de %B de %Y"))
        self.ventana.after(1000, self.actualizar_reloj)


# ==================== CLASE PRINCIPAL ====================


class Escritorio:

    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Windows IA - Simple")
        self.raiz.geometry(f"{ANCHO_PANTALLA}x{ALTO_PANTALLA}")
        self.escritorio = tk.Frame(raiz, bg=COLOR_FONDO)
        self.escritorio.pack(fill=tk.BOTH, expand=True)
        self.crear_iconos()
        self.crear_barra_tareas()
        self.actualizar_reloj_sistema()

    def crear_iconos(self):
        aplicaciones = [
            ("🖩", "Calculadora", Calculadora),
            ("📝", "Bloc de Notas", BlocNotas),
            ("⚙️", "Configuración", lambda p: Configuracion(p, self)),
            ("🕐", "Reloj", Reloj),
        ]

        for i, (icono, nombre, clase_app) in enumerate(aplicaciones):
            marco = tk.Frame(self.escritorio, bg=COLOR_FONDO)
            marco.place(x=20, y=20 + i * 100)

            boton = tk.Button(
                marco,
                text=icono,
                font=("Arial", 32),
                bg=COLOR_FONDO,
                relief=tk.FLAT,
                command=lambda a=clase_app: a(self.raiz),
            )
            boton.pack()

            tk.Label(
                marco, text=nombre, bg=COLOR_FONDO, fg="white", font=("Arial", 10)
            ).pack()

    def crear_barra_tareas(self):
        self.barra_tareas = tk.Frame(self.raiz, bg="#1f1f1f", height=ALTURA_BARRA_TAREAS)
        self.barra_tareas.pack(side=tk.BOTTOM, fill=tk.X)

        # Botón inicio
        tk.Button(
            self.barra_tareas,
            text="🪟 Inicio",
            bg="#1f1f1f",
            fg="white",
            relief=tk.FLAT,
            command=self.mostrar_menu,
        ).pack(side=tk.LEFT, padx=10)

        # Reloj del sistema
        self.etiqueta_reloj = tk.Label(
            self.barra_tareas, text="", bg="#1f1f1f", fg="white", font=("Arial", 10)
        )
        self.etiqueta_reloj.pack(side=tk.RIGHT, padx=15)

    def actualizar_reloj_sistema(self):
#  Actualiza reloj del sistema en barra de tareas
        ahora = datetime.now()
        self.etiqueta_reloj.config(text=ahora.strftime("%H:%M:%S\n%d/%m/%Y"))
        self.raiz.after(1000, self.actualizar_reloj_sistema)

    def mostrar_menu(self):
#  Boton del task bar para mostrar el menu
        menu = tk.Menu(self.raiz, tearoff=0)
        menu.add_command(label="🖩 Calculadora", command=lambda: Calculadora(self.raiz))
        menu.add_command(label="📝 Bloc de Notas", command=lambda: BlocNotas(self.raiz))
        menu.add_command(
            label="⚙️ Configuración", command=lambda: Configuracion(self.raiz, self)
        )
        menu.add_command(label="🕐 Reloj", command=lambda: Reloj(self.raiz))
        menu.add_separator()
        menu.add_command(label="❌ Salir", command=self.raiz.quit)
        menu.post(10, ALTO_PANTALLA - ALTURA_BARRA_TAREAS - 200)

    def establecer_fondo(self, valor):
 
        if valor.endswith((".png", ".jpg", ".jpeg", ".bmp")):
            try:
                # Eliminar la etiqueta de imagen anterior si existe
                for widget in self.escritorio.winfo_children():
                    if isinstance(widget, tk.Label) and hasattr(widget, 'image'):
                        widget.destroy()
                
                # Cargar y redimensionar imagen
                imagen = Image.open(valor).resize((ANCHO_PANTALLA, ALTO_PANTALLA))
                foto = ImageTk.PhotoImage(imagen)

                # Crear etiqueta de fondo
                etiqueta = tk.Label(self.escritorio, image=foto)
                etiqueta.image = foto
                etiqueta.place(x=0, y=0, relwidth=1, relheight=1)
                etiqueta.lower()  # Enviar al fondo
                
                # Asegurar que los iconos estén siempre por encima
                for widget in self.escritorio.winfo_children():
                    if isinstance(widget, tk.Frame):
                        widget.lift()  # Traer al frente
                                
            except Exception as e:
                messagebox.showerror("Error", f"Error cargando imagen: {e}")
        else:
            # Eliminar cualquier imagen de fondo antes de aplicar color
            for widget in self.escritorio.winfo_children():
                if isinstance(widget, tk.Label) and hasattr(widget, 'image'):
                    widget.destroy()
            
            # Aplicar color sólido al escritorio
            self.escritorio.config(bg=valor)
            
            # Actualizar color de los marcos de iconos para que coincidan
            for widget in self.escritorio.winfo_children():
                if isinstance(widget, tk.Frame):
                    widget.config(bg=valor)
                    for child in widget.winfo_children():
                        if isinstance(child, (tk.Button, tk.Label)):
                            child.config(bg=valor)


# ==================== EJECUCIÓN ====================

if __name__ == "__main__":
    print("=" * 60)
    print("WINDOWS IA ")
    print("Inicializando entorno gráfico...")
    print("=" * 60)

    raiz = tk.Tk()
    escritorio = Escritorio(raiz)
    raiz.mainloop()
