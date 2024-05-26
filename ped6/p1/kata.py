class Partida:
    rondas_totales = 10
    bolos_ronda = 10

    def __init__(self):
        self.lanzamientos = [0] * 21
        self.lanzamiento_actual = 0

    def tirar_bola(self, bolos):
        if self.lanzamiento_actual >= 20 and not self.es_strike(self.lanzamiento_actual - 2) and not self.es_spare(self.lanzamiento_actual - 1):  
            raise ValueError("No se pueden realizar más lanzamientos")
        if self.lanzamiento_actual == 18 and self.es_strike(self.lanzamiento_actual - 2):  
            self.lanzamientos[self.lanzamiento_actual] = bolos
            self.lanzamiento_actual += 1
        elif self.lanzamiento_actual == 19 and (self.es_strike(self.lanzamiento_actual - 3) or self.es_spare(self.lanzamiento_actual - 2)):  
            self.lanzamientos[self.lanzamiento_actual] = bolos
            self.lanzamiento_actual += 1
        elif self.lanzamiento_actual < 20:
            self.lanzamientos[self.lanzamiento_actual] = bolos
            self.lanzamiento_actual += 1
        else:
            raise ValueError("No se pueden realizar más lanzamientos")


    def calcular_resultado(self):
        resultado = 0
        index_ronda = 0
        for ronda in range(self.rondas_totales):
            if self.es_strike(index_ronda):
                resultado  += self.bolos_ronda + self.bonus_strike(index_ronda)
                index_ronda += 1
            elif self.es_spare(index_ronda):
                resultado += self.bolos_ronda + self.bonus_spare(index_ronda)
                index_ronda += 2
            else:
                resultado += self.lanzamientos[index_ronda] + self.lanzamientos[index_ronda + 1]
                index_ronda += 2

        return resultado
    
    def es_spare(self, index_ronda):
        return self.lanzamientos[index_ronda] + self.lanzamientos[index_ronda + 1] == self.bolos_ronda
    
    def bonus_spare(self, index_ronda):
        return self.lanzamientos[index_ronda + 2]
    
    def es_strike(self, index_ronda):
        return self.lanzamientos[index_ronda] == self.bolos_ronda
    
    def bonus_strike(self, index_ronda):
        return self.lanzamientos[index_ronda + 1] + self.lanzamientos[index_ronda + 2]