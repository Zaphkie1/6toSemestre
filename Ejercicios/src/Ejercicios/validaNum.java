package Ejercicios;

import java.util.regex.Pattern;

public class validaNum {
    public static void main(String[] args) {
        String dateRegex = "^\\d{3} \\d{3} \\d{3}";
        String date = "123 456 789";
        if (Pattern.matches(dateRegex, date)) {
            System.out.println("Correcto");
        } else {
            System.out.println("Incorrecto");
        }
    }
}
