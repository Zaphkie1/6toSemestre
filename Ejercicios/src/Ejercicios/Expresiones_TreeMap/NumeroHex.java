/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Ejercicios.Expresiones_TreeMap;
import java.util.Scanner;

/**
 * Edgar Israel Trejo Vazquez - 21450213
 * Valida si un numero es hexadecimal en java tiene que empezar en 0x puedes tener 
 * numeros y solo letras A - F
 */
public class NumeroHex {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrena un valor en Hexadecimal: ");
        String input = scanner.nextLine();
        
        if (ValidadorDeHex(input)) {
            System.out.println("Si es un numero en Hexadecimal!");
        } else {
            System.out.println("No es un numero en Hexadecimal!");
        }
    }
    
    public static boolean ValidadorDeHex(String input) {
        String pattern = "^0x[0-9A-Fa-f]+$";
        return input.matches(pattern);
    }

}

