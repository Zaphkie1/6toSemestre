package Ejercicios.Enum;

public class PruebaEnum {
    public static void main(String[] args) {
        Simbolos s = Simbolos.PORTERO;
        System.out.println(s);
        System.out.println(s.getNombre());
        System.out.println(s.getValor());
        Simbolos x = Simbolos.MAYORQUE;
        System.out.println(x);
        System.out.println(x.getNombre());
        System.out.println(x.getValor());
        Jugador y = new Jugador("Ochoa", Simbolos.PORTERO);
        System.out.println(y);
    }
}
