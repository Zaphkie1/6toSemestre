package Ejercicios;

import java.util.regex.Pattern;

public class PruebaRFc {
    
    public static void main(String[] args) {

        String dateRegex = "^[A-Z]{4}\\d{6}[A-Z0-9]{3}$";
        String date = "991201AABCLT2";
        if (Pattern.matches(dateRegex, date)) {
            System.out.println("Correcto");
        } else {
            System.out.println("Incorrecto");
        }
    }
}
