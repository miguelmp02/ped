//import static org.junit.jupiter.api.Assertions.assertEquals;

//import org.junit.jupiter.api.Test;
import static org.junit.Assert.*;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class Test_bolos {
    @Test
    public void testIniciarPartida() {
        Partida partida = new Partida();
        //partida.iniciarPartida();
        assertEquals(10, partida.getRondas());
        System.out.println("Se ha iniciado la partida");
    }
    @Test
    public void testPasarRonda() {
        Partida partida = new Partida();
        //int rondas = 10;
        //partida.iniciarPartida();
        for (int i = 0; i==partida.getRondas(); i++) {
            partida.tirar_bola(2);
            partida.tirar_bola(4);
            System.out.println("Quedan" + partida.getRondas() + "rondas restantes");
        }
        assertEquals(partida.getRondas(), 0);

    }
}
