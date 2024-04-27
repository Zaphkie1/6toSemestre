package Ejercicios.Expresiones_TreeMap;
import java.util.Collection;
import java.util.Set;
import java.util.TreeMap;

public class TestTreeMap {
    public static void main(String[] args) {
        // TreeMap<Integer, String> tm = new TreeMap<>();
        // tm.put(80, "Fruta");
        // tm.put(5, "Verdura");
        // int x = 888;
        // String v = "El valor";
        // tm.put(x, v);
        // Set<Integer> llaves = tm.keySet();
        // Collection<String> valores = tm.values();
        // System.out.println(llaves);
        // System.out.println(valores);
        // for (Integer key : llaves) {
        // System.out.println(tm.get(key));
        // }

        String cadena = "EstaEs.unA CadAna-dAtos";
        TreeMap<Integer, Character> ic = new TreeMap<>();
        for (int i = 0; i < cadena.length(); i++) {
            switch (Character.toLowerCase(cadena.charAt(i))) {
                case 'a', 'e', 'i', 'o', 'u' -> {
                    ic.put(i, Character.toLowerCase(cadena.charAt(i)));
                }
            }
        }
        Set<Integer> keyss = ic.keySet();
        Collection<Character> charss = ic.values();
        System.out.println(keyss);
        System.out.println(charss);
    }

}
