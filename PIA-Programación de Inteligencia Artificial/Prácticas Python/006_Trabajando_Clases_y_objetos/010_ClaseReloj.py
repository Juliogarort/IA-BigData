class Reloj:
    def __init__(self, hora=0, minuto=0, segundo=0):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
    
    def ajustar_hora(self, hora, minuto, segundo):
        # """Ajusta la hora del reloj"""
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
    
    def avanzar_segundo(self):
        # """Avanza un segundo en el reloj"""
        self.segundo += 1
        if self.segundo >= 60:
            self.segundo = 0
            self.minuto += 1
            if self.minuto >= 60:
                self.minuto = 0
                self.hora += 1
                if self.hora >= 24:
                    self.hora = 0
    
    def avanzar_minuto(self):
        # """Avanza un minuto en el reloj"""
        self.minuto += 1
        if self.minuto >= 60:
            self.minuto = 0
            self.hora += 1
            if self.hora >= 24:
                self.hora = 0
    
    def mostrar_hora(self):
        # """Muestra la hora en formato hh:mm:ss"""
        return f"{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"
    
reloj = Reloj(20, 59, 30)
reloj.avanzar_segundo()
reloj.avanzar_segundo()
print(reloj.mostrar_hora())