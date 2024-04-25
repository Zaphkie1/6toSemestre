package Ejercicios.Lexemas;

import java.util.ArrayList;

public class PruebaLexema {
        public static void main(String[] args) {
        ArrayList<Lexema> lexemas = new ArrayList();
        //Opcion 1
        Lexema a = new Lexema("hola", TablaSimbolos.getNumero("hola"));
        lexemas.add(a);
        //Opcion 2
        String variable = ">=";
        lexemas.add(new Lexema(variable, TablaSimbolos.getNumero(variable)));
        for (Lexema l : lexemas) {
            System.out.println(l);
        }
    }
}

//        public static void main(String[] args) {
//            String texto = "hola >= mundo 64";
//
//            ArrayList<Lexema> lexemas = analizarTexto(texto);
//
//            for (Lexema l : lexemas) {
//                System.out.println(l);
//            }
//        }
//
//        public static ArrayList<Lexema> analizarTexto(String texto) {
//            ArrayList<Lexema> lexemas = new ArrayList<>();
//
//            // Separar el texto en palabras
//            String[] palabras = texto.split("\\s+");
//
//            // Analizar cada palabra y agregar el lexema correspondiente a la lista
//            for (String palabra : palabras) {
//                int numero = TablaSimbolos.getNumero(palabra);
//                lexemas.add(new Lexema(palabra, numero));
//            }
//
//            return lexemas;
//        }
//    }