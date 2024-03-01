package IdentificadorVar;

import javax.swing.UIManager;
import javax.swing.UnsupportedLookAndFeelException;

public class EjemploTry {

    public static void main(String[] args) {
          try {
              UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
          } catch (ClassNotFoundException | InstantiationException | IllegalAccessException | UnsupportedLookAndFeelException ex) {
              ex.printStackTrace();
          }

        // Crear la ventana y realizar otras acciones
        Ventana v = new Ventana();
        Acciones ac = new Acciones(v.getTxtArchivo(), v.getErrArchivo());
        v.setVisible(true);
    }
}
