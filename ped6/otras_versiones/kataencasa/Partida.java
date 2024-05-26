import java.util.ArrayList;
import java.util.List;

public class Partida {
    private int rondas;
    private int resultado;
    private int intentos;
    private List<Integer> turno;
    private List<List<Integer>> historial;

   
    public Partida() {
	    iniciarPartida();
    }

    public void iniciarPartida() {
        rondas = 10;
        resultado = 0;
        intentos = 2;
        turno = new ArrayList<>(); // Para guardar los resultados de cada tiro en la ronda actual
        historial = new ArrayList<>(); //Para guardar el historial completo de tiros
    }
    public int getRondas() {
        return rondas;
    }
    public void pasar_ronda() {
        if (rondas > 0){
            rondas = rondas -1;
            intentos = 2;
            historial.add(turno); //se mete el turno en la lista historial para contabilizarlos
        }
    }
    public void tirar_bola(int numero_bolos) {
        if(0<=numero_bolos && numero_bolos<=10) {
            intentos = intentos -1;
        }else {
            throw new IllegalArgumentException("El número de bolos debe estar entre 0 y 10 ambos incluidos.");
        }

    }


}
