class Restaurante:
    def __init__(self, nombre, tipo_cocina):
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
        self.menu = []

    def anadir_plato(self, plato):
        self.menu.append(plato)
        return f"Plato '{plato}' añadido al menú."

    def mostrar_menu(self):
        if not self.menu:
            return "El menú está vacío."
        return f"Menú del restaurante {self.nombre}: {', '.join(self.menu)}"

    def pedir(self, indice):
        if 0 <= indice < len(self.menu):
            return f"Has pedido: {self.menu[indice]}"
        return "Plato no disponible."

r = Restaurante("Pastas Oc", "Italo Rinconero")
print(r.anadir_plato("Pizza Margarita"))
print(r.anadir_plato("Pasta Carbonara"))
print(r.mostrar_menu())
print(r.pedir(1))
