package Sintactico;

public class Sintactico {
    private int token;

    // <Programa>->start<A><Sentencia>finish
    // <Programa>->101<A><Sentencia>103

    public void Programa() {
        token = gettoken();

        if (token != 101) {
            // Lanza un error
        }
        token = gettoken();
        A();
        sentencia();
        if (token != 103) {
            // Lanza un error
        } else {
            System.out.println("Finalizo correctamente");
        }
    }

    // produce nulo
    // <A> -> <Tipo><List_id>
    // <A> -> ε
    // Follow(A) = {begin,identificador,input,output,if,loop,repeat}
    // Follow(A) = {102,1,106,107,108,111,114}

    public void A() {
        if (token == 102 || token == 1 || token == 106 || token == 107 || token == 108 || token == 111
                || token == 114) {
        return;
        }
        Tipo();
        List_id();
        if (token != 401){
            // Lanza un error
        }
        token = gettoken();
        A();
    }
    private void Condicion(){

    }

    public void nueva1(){
        switch (token){
            case 301:
            case 302:
            case 303:
            case 304:
            case 305:
            case 306:

            break;

            default:
        }
    }
}