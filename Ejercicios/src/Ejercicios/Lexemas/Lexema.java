package Ejercicios.Lexemas;

public class Lexema {
    private String dato;
    private int token;

    public Lexema(String dato, int token) {
        this.dato = dato;
        this.token = token;
    }

    public String getDato() {
        return this.dato;
    }

    public void setDato(String dato) {
        this.dato = dato;
    }

    public int getToken() {
        return this.token;
    }

    public void setToken(int token) {
        this.token = token;
    }

    @Override
    public String toString() {
        return " [" + dato + "," + token + "]";
    }

}
