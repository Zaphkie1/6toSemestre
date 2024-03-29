package Ejercicios;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class MatcherPattern {
    public static void main(String[] args) {
        // Definir el patrón
        String patternString = "([1-9][0-9]*|[a-zA-Z_][a-zA-Z0-9_]*)|([1-9][0-9]|[a-zA-Z]\\w|_|0|[*/;.,-]|(?![0-9]|\\n)(==|<>|<=|>=|<|>))";
        Pattern pattern = Pattern.compile(patternString);

        // Definir la cadena de texto
        String input = "Hola Ale?+=cada*100.adios\r\n" + //
                        "Lopez/Loza_125-33\r\n" + //
                        "estaEs*unaVariable/666-23casa\r\n" + //
                        "nueva_123,mi_variable_456;fin3\r\n" + //
                        "luna@luna_123\r\n" + //
                        "0123==<>>=><<=";

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
