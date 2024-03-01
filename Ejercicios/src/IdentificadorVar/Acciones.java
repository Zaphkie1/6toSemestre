/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package IdentificadorVar;

import javax.swing.JFileChooser;
import javax.swing.JTextArea;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

/**
 *
 * @author TheWi
 */
public class Acciones {

    private JTextArea txtArchivo;
    private JTextArea errArchivo;

    public Acciones(JTextArea txtArchivo, JTextArea errArchivo) {
        this.txtArchivo = txtArchivo;
        this.errArchivo = errArchivo;
    }

    public void abrirArchivo() {
        JFileChooser fileChooser = new JFileChooser();
        int seleccion = fileChooser.showOpenDialog(null);

        if (seleccion == JFileChooser.APPROVE_OPTION) {
            File archivo = fileChooser.getSelectedFile();
            try {
                FileReader fr = new FileReader(archivo);
                BufferedReader br = new BufferedReader(fr);
                StringBuilder contenido = new StringBuilder();
                String linea = br.readLine();
                while (linea != null) {
                    contenido.append(linea).append("\n");
                    linea = br.readLine();
                }
                br.close();
                txtArchivo.setText(contenido.toString());
                errArchivo.setText("");
            } catch (FileNotFoundException ex) {
                txtArchivo.setText("");
                errArchivo.setText("Error: Archivo no encontrado");
            } catch (IOException ioe) {
                txtArchivo.setText("");
                errArchivo.setText("Error al leer el archivo");
            }
        } else if (seleccion == JFileChooser.CANCEL_OPTION) {
            txtArchivo.setText("");
            errArchivo.setText("Operación cancelada");
        } else if (seleccion == JFileChooser.ERROR_OPTION) {
            txtArchivo.setText("");
            errArchivo.setText("Error al seleccionar el archivo");
        }
    }
}
