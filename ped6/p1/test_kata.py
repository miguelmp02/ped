import unittest
from kata import Partida

class TestBolos(unittest.TestCase):

    def test_iniciar_partida(self):
        partida = Partida()
        self.assertEqual(partida.rondas_totales, 10)


    def test_primera_partida(self):
        partida = Partida()
        for i in range(10):
            partida.tirar_bola(0)
            partida.tirar_bola(0)

        print(f"{partida.lanzamientos}")
        self.assertEqual(partida.calcular_resultado(), 0)

    def test_segunda_partida(self):
        partida = Partida()
        for i in range(10):
            partida.tirar_bola(1)
            partida.tirar_bola(1)   
        self.assertEqual(partida.calcular_resultado(), 20)

    def test_tercera_partida(self):
        partida = Partida()
        rondas = 10
        for i in range(rondas):
            partida.tirar_bola(1)
            partida.tirar_bola(3)
            print(f"Este es la ronda número { int(partida.lanzamiento_actual / 2) } . Quendan { len(partida.lanzamientos) - partida.lanzamiento_actual } lanzamientos restantes.")
        self.assertEqual(partida.calcular_resultado(), 40)

    def test_pleno(self):
        partida = Partida()
        partida.tirar_bola(10) 
        partida.tirar_bola(5)  
        partida.tirar_bola(4)
        for i in range(8):
            partida.tirar_bola(0)
            partida.tirar_bola(0)  
        self.assertEqual(partida.calcular_resultado(), 28)

    
    def test_semipleno(self):
        partida = Partida()
        partida.tirar_bola(5)
        partida.tirar_bola(5)
        partida.tirar_bola(4)
        partida.tirar_bola(1)
        for i in range(8):
            partida.tirar_bola(0)
            partida.tirar_bola(0)
        self.assertEqual(partida.calcular_resultado(), 19)
    
    def test_partida_completa(self):
        partida = Partida()
        partida.tirar_bola(4)
        partida.tirar_bola(4)
        partida.tirar_bola(10)
        partida.tirar_bola(4)
        partida.tirar_bola(3)
        partida.tirar_bola(9)
        partida.tirar_bola(1)
        partida.tirar_bola(2)
        partida.tirar_bola(0)
        for i in range(5):
            partida.tirar_bola(2)
            partida.tirar_bola(2)
        self.assertEqual(partida.calcular_resultado(), 66)

    def test_partida_perfecta(self):
        partida = Partida()
        for i in range(12):
            partida.tirar_bola(10)
        self.assertEqual(partida.calcular_resultado(), 300)
    
    def test_maximo_lanzamientos(self):
        partida = Partida()
        for i in range(10):
            partida.tirar_bola(0)
            partida.tirar_bola(0)
        with self.assertRaises(ValueError):
            partida.tirar_bola(0)


'''
   
    def test_solo_tengo_2_intentos_por_ronda(self):
        partida = Partida()
        partida.iniciar_partida()
        partida.tirar_bola(1)
        partida.tirar_bola(1)  
        self.assertEqual(partida.rondas, 9)
'''
	
if __name__ == '__main__':
    unittest.main()
