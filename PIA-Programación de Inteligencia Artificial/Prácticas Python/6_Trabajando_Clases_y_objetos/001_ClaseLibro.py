class Libro:
    def __init__(self, titulo, autor, paginas, editorial, ano):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.editorial = editorial
        self.ano = ano

    def mostrar_info(self):
        return f"'{self.titulo}' de {self.autor} ({self.ano}) - {self.paginas} pág. - {self.editorial}"

    def es_largo(self):
        if self.paginas > 300:
            return f"Es un libro largo ({self.paginas} páginas)."
        else:
            return f"Es un libro corto ({self.paginas} páginas)."

libro = Libro("La rinconada Word Wide", "Oc Carlos Nuñez", 666, "La Rinconada", 2024)
print(libro.mostrar_info())
print(libro.es_largo())
