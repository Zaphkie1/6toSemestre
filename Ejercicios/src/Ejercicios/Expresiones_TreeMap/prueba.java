package Ejercicios;

import java.util.Arrays;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;
import java.util.TreeSet;

public class prueba {
    public static void main(String args[]) {
        Map<String, Set<String>> dictionary = new TreeMap<>();
        Set<String> a = new TreeSet<>(Arrays.asList("Actual", "Arrival", "Actuary"));
        Set<String> b = new TreeSet<>(Arrays.asList("Bump", "Bravo", "Basic"));

        dictionary.put("B", b);
        dictionary.put("A", a);

        System.out.println(dictionary);
    }

}
