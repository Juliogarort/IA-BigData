class Libro:
# Clase que declara la estructura y atributos de libros
    
    def __init__(self, id_libro, titulo, autor, anyo, n_pags, genero, editorial, estado, disponible):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.anyo = anyo
        self.n_pags = n_pags
        self.genero = genero
        self.editorial = editorial
        self.estado = estado
        self.disponible = disponible
    
    def a_diccionario(self):
#  Obtiene los datos del csv
        return {
            'id_libro': self.id_libro,
            'titulo': self.titulo,
            'autor': self.autor,
            'anyo': self.anyo,
            'n_pags': self.n_pags,
            'genero': self.genero,
            'editorial': self.editorial,
            'estado': self.estado,
            'disponible': self.disponible
        }
    
    @staticmethod
    def desde_diccionario(datos):
#  Mediante el objeto del csv crea los libros
        return Libro(
            datos['id_libro'],
            datos['titulo'],
            datos['autor'],
            datos['anyo'],
            datos['n_pags'],
            datos['genero'],
            datos['editorial'],
            datos['estado'],
            datos['disponible']
        )
    
    def __str__(self):
#  Se muestran los datos del libro
        disponibilidad = "Disponible" if self.disponible == "True" else "No disponible"
        return (f"ID: {self.id_libro} | {self.titulo} - {self.autor} ({self.anyo}) | "
                f"Género: {self.genero} | Páginas: {self.n_pags} | {disponibilidad}")
