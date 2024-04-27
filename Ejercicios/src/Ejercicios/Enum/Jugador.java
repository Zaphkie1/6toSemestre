package Ejercicios.Enum;

public class Jugador {
    private String nombre;
    private Simbolos posicion;

    public Jugador(String nombre, Simbolos posicion) {
        this.nombre = nombre;
        this.posicion = posicion;
    }

    @Override
    public String toString() {
        return "Jugador{" +
                "nombre='" + nombre + '\'' +
                ", posicion=" + posicion +
                '}';
    }
    
}
