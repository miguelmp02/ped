class Partida:
    rondas_totales = 10
    bolos_ronda = 10
    #lanzamientos_por_ronda = 2


    def __init__(self):
        self.ronda_actual = 1
        self.lanzamientos = [0] * 22 #lista que contiene hasta 21 lanzamientos contando el bonus e inicialmente, todos los elementos de la lista se establecen en 0
        self.lanzamiento_actual = 0

    def pasar_ronda(self):
        if self.ronda_actual < self.rondas_totales:
            self.ronda_actual += 1
            print("Se ha pasado a la ronda", self.ronda_actual)
            return True
        else:
            print("La partida ha terminado")
            return False
    
    def tirar_bola(self, bolos_tirados):
        if self.lanzamiento_actual < 22:
            self.lanzamientos[self.lanzamiento_actual] = bolos_tirados #se registra el número de bolos derribados en el lanzamiento actual
            self.lanzamiento_actual += 1

    def calcula_resultado(self):
        resultado = 0
        i = 0
        for ronda in range(self.rondas_totales):
            if self.lanzamientos[i] == 10:  # Verifica si hay un lanzamiento de strike (10 bolos derribados)
                if ronda == self.rondas_totales - 1:  # Última ronda
                # Suma 10 + los dos próximos lanzamientos (lanzamiento extra)
                    resultado += 10 +  self.lanzamientos[i + 2] + self.lanzamientos[i + 3] 
                    break
                else:
                    resultado += 10 + self.lanzamientos[i + 2] + self.lanzamientos[i + 3] 
                    i += 2 
            elif self.lanzamientos[i] + self.lanzamientos[i + 1] == 10 and self.lanzamientos[i] != 10:  # Verifica si la suma de los dos lanzamientos sale 10 y no es 10 (primer lanzamiento) + 0
                resultado += 10 + self.lanzamientos[i + 2] # En la primera tirada del test, se hace el semipleno y por lo tanto entra por este elif
                #una vez que ya ha calculado el resultado, el test pasa de ronda y hace dos nuevos lanzamientos, lo que hace que se vuelva a entrar
                #a este método y el puntaje total acumulado se actualiza en cada iteración del bucle for que recorre las rondas. Cada vez que se suma un 
                #puntaje al resultado, este se actualiza con el nuevo valor. Esto garantiza que al final de todas las rondas, 
                #el resultado contenga el puntaje total de la partida. Es decir, suma 10 + lo que haya en la posición i+2, luego pasa al siguiente 
                # par de lanzamientos con i += 2 y luego entra por el else y suma lo de antes + lo de i + lo de i+1. 
                #Esto pasa ya que estamos en un bucle for que está recorriendo todas las rondas (son 10).
                i += 2 
            else:
                resultado += self.lanzamientos[i] + self.lanzamientos[i + 1] # agrega al resultado total el número de bolos derribados en dos lanzamientos consecutivos
                i += 2 #avanza al siguiente par de lanzamientos en la lista de lanzamientos de la partida
        return resultado





    
    

    


        
        