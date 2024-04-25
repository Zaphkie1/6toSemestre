package Ejercicios.Lexemas;

public class TablaSimbolos {
    private TablaSimbolos() {
    }

    public static int getNumero(String dato) {
        int n = -1;
        switch (dato) {
            case "+":
                return 124;
            case "-":
                return 149;
            case "*":
                return 100;
            case "/":
                return 171;
            case ":=":
                return 115;
            case "==":
                return 197;
            case "<>":
                return 187;
            case ">":
                return 169;
            case ">=":
                return 123;
            case "<":
                return 162;
            case "<=":
                return 186;
            case "(":
                return 179;
            case ")":
                return 185;
            case ";":
                return 150;
            case ",":
                return 194;
            case "Start":
                return 64;
            case "Finish":
                return 51;
            case "begin":
                return 77;
            case "input":
                return 62;
            case "output":
                return 96;
            case "int":
                return 97;
            case "str":
                return 83;
            case "end":
                return 89;
            case "if":
                return 99;
            case "then":
                return 91;
            case "else":
                return 90;
            case "loop":
                return 60;
            case "do":
                return 74;
            case "repeat":
                return 52;
            default:
                return esReservada(dato);
        }
    }


    private static int esReservada(String dato) {
        try {
            int n = Integer.parseInt(dato);
        } catch (NumberFormatException e) {
            // TODO: handle exception
            System.out.println("No es un numero");
        }

        return 0;
    }
}