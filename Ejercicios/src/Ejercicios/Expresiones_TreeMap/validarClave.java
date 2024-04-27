package Ejercicios.Expresiones_TreeMap;
import java.util.regex.Pattern;

public class validarClave {
    public static void main(String[] args) {
        String dateRegex = "^\\d{18}";
        String date = "202023423423423428";
        if (Pattern.matches(dateRegex, date)) {
            System.out.println("Correcto");
        } else {
            System.out.println("Incorrecto");
        }
    }
}
