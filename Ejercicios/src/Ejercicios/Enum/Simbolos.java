package Ejercicios.Enum;

public enum Simbolos {
    PORTERO("OChoa", 23),
    DEFENSA("RMarquez", 4),
    MEDIO("GdosSantos", 18),
    DELANTERO("CHernandez", 14),
    MAYORQUE(">",10),
    MENORQUE("<",11);
    private String nombre;
    private int valor;
    private Simbolos(String nombre, int valor){
        this.nombre = nombre;
        this.valor = valor;
    }
    public String getNombre(){
        return nombre;
    }
    public int getValor(){
        return valor;
    }

}
