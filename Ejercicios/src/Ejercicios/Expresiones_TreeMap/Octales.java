/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Ejercicios.Expresiones_TreeMap;
import java.util.Scanner;

/**
 *
 * Edgar Israel Trejo Vazquez - 21450213
 * Validador de octale en java solo puede ser del 0 - 7 con entrada
 */
public class Octales {
    public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);
            System.out.print("Ingrena un valor en octal: ");
            String input = scanner.nextLine();

            if (ValidadorDeOct(input)) {
                System.out.println("Si es un numero en octal!");
            } else {
                System.out.println("No es un numero en octal!");
            }
        }

        public static boolean ValidadorDeOct(String input) {
            String pattern = "^[0-7]+$";
            return input.matches(pattern);
        }

    }
