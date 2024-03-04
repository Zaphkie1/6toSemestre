package Ejercicios;
import java.util.regex.Pattern;

//genera un validador de expresiones regulares para fechas

public class validarfecha {
    public static void main(String[] args) {
        String dateRegex = "^\\d{4}/(0[1-9]|1[0-2])/(0[1-9]|[1-2][0-9]|3[0-1])";
        String date = "2020/01/24";
        if (Pattern.matches(dateRegex, date)) {
            System.out.println("Correcto");
        } else {
            System.out.println("Incorrecto");
        }
    }
}