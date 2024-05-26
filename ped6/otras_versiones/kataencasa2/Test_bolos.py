import unittest
from Partida import Partida

class TestBolos(unittest.TestCase):
    def test_iniciar_partida(self):
        partida = Partida()
        self.assertEqual(partida.rondas_totales, 10)
        self.assertEqual(partida.bolos_ronda, 10)
        print("Partida iniciada correctamente")

    def test_pasar_ronda(self):
        partida = Partida()
        self.assertEqual(partida.ronda_actual, 1)
        for _ in range(partida.rondas_totales - 1):
            self.assertTrue(partida.pasar_ronda())


    def test_ronda_sin_plenos_ni_semiplenos(self):
        partida = Partida()
        partida.tirar_bola(3)
        partida.tirar_bola(4)
        self.assertEqual(partida.calcula_resultado(), 7)

    def test_partida_sin_plenos_ni_semiplenos(self):
        partida = Partida()
        partida.tirar_bola(3)
        partida.tirar_bola(4)
        partida.pasar_ronda()
        partida.tirar_bola(3)
        partida.tirar_bola(3)
        partida.pasar_ronda()
        partida.tirar_bola(1)
        partida.tirar_bola(0)
        partida.pasar_ronda()
        partida.tirar_bola(2)
        partida.tirar_bola(5)
        partida.pasar_ronda()
        partida.tirar_bola(4)
        partida.tirar_bola(4)
        partida.pasar_ronda()
        partida.tirar_bola(1)
        partida.tirar_bola(5)
        partida.pasar_ronda()
        partida.tirar_bola(0)
        partida.tirar_bola(0)
        partida.pasar_ronda()
        partida.tirar_bola(0)
        partida.tirar_bola(4)
        partida.pasar_ronda()
        partida.tirar_bola(2)
        partida.tirar_bola(2)
        partida.pasar_ronda()
        partida.tirar_bola(1)
        partida.tirar_bola(7)
        print("Partida completada sin plenos ni semiplenos")
        self.assertEqual(partida.calcula_resultado(), 51)

    def test_con_pleno_en_primera_ronda(self):
        partida = Partida()
        partida.tirar_bola(10)
        partida.tirar_bola(0)
        partida.pasar_ronda()
        partida.tirar_bola(3)
        partida.tirar_bola(4)
        for _ in range(8):
            partida.tirar_bola(0)  
            partida.tirar_bola(0)  
            partida.pasar_ronda()
        print("Partida con un pleno al principio")
        self.assertEqual(partida.calcula_resultado(), 24)

    def test_con_semipleno_en_primera_ronda(self):
        partida = Partida()
        partida.tirar_bola(5)
        partida.tirar_bola(5)
        partida.pasar_ronda()
        partida.tirar_bola(3)
        partida.tirar_bola(4)
        for _ in range(8):
            partida.tirar_bola(0)  
            partida.tirar_bola(0)  
            partida.pasar_ronda()
        self.assertEqual(partida.calcula_resultado(), 20)
    
    def test_pleno_ultima_ronda(self):
        partida = Partida()
        for _ in range(9):
            partida.tirar_bola(0)  
            partida.tirar_bola(0)  
            partida.pasar_ronda()
        partida.tirar_bola(10)
        partida.tirar_bola(0)
        partida.tirar_bola(3)
        partida.tirar_bola(4)
        self.assertEqual(partida.calcula_resultado(), 17)

        


if __name__ == '__main__':
    unittest.main()