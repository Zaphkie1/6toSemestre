package Ejercicios;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class MatcherPattern {
    public static void main(String[] args) {
        // Definir el patrón
        String patternString = "([1-9]\\d*|[a-zA-Z]\\w*)|([1-9]\\d|[a-zA-Z]\\w|_|0|[*/;.,\\-]|(?![0-9]|\\n)(==|<>|<=|>=|<|>))";
        Pattern pattern = Pattern.compile(patternString);

        // Definir la cadena de texto
        String input = "estaEs*unavariable/666-23casa\n" +
        "nueva_123,mi_variable_456;fin3\n" +
        "_33<>=0123.55\n";
        // Crear el objeto Matcher
        Matcher matcher = pattern.matcher(input);

        // Realizar la búsqueda y encontrar coincidencias
        while (matcher.find()) {
            // Acciones a realizar cuando se encuentra una coincidencia
            // Por ejemplo, imprimir la coincidencia encontrada
            System.out.println("Coincidencia encontrada: " + matcher.group());
        }
    }
}
