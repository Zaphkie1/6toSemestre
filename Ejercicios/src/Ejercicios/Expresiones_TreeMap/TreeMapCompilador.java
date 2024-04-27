package Ejercicios.Expresiones_TreeMap;
import java.util.Collection;
import java.util.Set;
import java.util.TreeMap;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class TreeMapCompilador {
    public static void main(String[] args) {
        String cadena = "EstaEs.unA CadAna-dAtos";
        TreeMap<Integer, Character> ic = new TreeMap<>();

        // Expresión regular adaptada
        Pattern pattern = Pattern.compile(
                "([1-9][0-9]*|[a-zA-Z_][a-zA-Z0-9_]*)|([1-9][0-9]|[a-zA-Z]\\w|_|0|[*/;.,-]|(?![0-9]|\\n)(==|<>|<=|>=|<|>))");
        Matcher matcher = pattern.matcher(cadena);

        int index = 0;
        while (matcher.find()) {
            String match = matcher.group();
            if (match.length() == 1) { // Solo caracteres individuales
                char character = match.charAt(0);
                ic.put(index, character);
            }
            index++;
        }

        Set<Integer> keys = ic.keySet();
        Collection<Character> chars = ic.values();
        System.out.println(keys);
        System.out.println(chars);
    }
}
