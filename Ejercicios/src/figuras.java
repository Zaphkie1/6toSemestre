import java.util.Scanner;
import org.apache.commons.math3.geometry.euclidean.twod.Vector2D;
import org.apache.commons.math3.geometry.euclidean.twod.PolygonsSet;
import org.apache.commons.math3.geometry.euclidean.twod.Polygon;
import org.apache.commons.math3.geometry.euclidean.twod.Line;
import org.apache.commons.math3.geometry.euclidean.twod.Vector2D;
import org.apache.commons.math3.geometry.euclidean.twod.SubLine;
import org.apache.commons.math3.geometry.partitioning.Region.Location;
import org.apache.commons.math3.geometry.euclidean.twod.HalfSpace;
import org.apache.commons.math3.geometry.euclidean.twod.Line;
import org.apache.commons.math3.geometry.partitioning.BSPTree;
import org.apache.commons.math3.geometry.partitioning.Region;
import org.apache.commons.math3.geometry.partitioning.SubHyperplane;
import org.apache.commons.math3.geometry.euclidean.twod.Euclidean2D;
import org.apache.commons.math3.geometry.euclidean.twod.SubLine;

import org.apache.commons.math3.geometry.euclidean.twod.Line;
import org.apache.commons.math3.geometry.euclidean.twod.Vector2D;

import org.apache.commons.math3.geometry.euclidean.twod.SubLine;
import org.apache.commons.math3.geometry.partitioning.Region;
import org.apache.commons.math3.geometry.partitioning.SubHyperplane;
import org.apache.commons.math3.geometry.partitioning.BSPTree;
import org.apache.commons.math3.geometry.partitioning.Region.Location;
import org.apache.commons.math3.geometry.euclidean.twod.Euclidean2D;
import org.apache.commons.math3.geometry.euclidean.twod.HalfSpace;
import org.apache.commons.math3.geometry.euclidean.twod.Line;
import org.apache.commons.math3.geometry.euclidean.twod.Vector2D;
import org.apache.commons.math3.geometry.euclidean.twod.SubLine;

public class Main {
    // Función para trasladar un objeto en las coordenadas especificadas
    public static Polygon trasladarObjeto(Polygon objeto, double dx, double dy) {
        Vector2D[] vertices = new Vector2D[objeto.getVertices().length];
        for (int i = 0; i < objeto.getVertices().length; i++) {
            Vector2D vertex = objeto.getVertices()[i];
            vertices[i] = new Vector2D(vertex.getX() + dx, vertex.getY() + dy);
        }
        return new Polygon(vertices);
    }

    // Función para dibujar un objeto
    public static void dibujarObjeto(Polygon objeto, String color) {
        Vector2D[] vertices = objeto.getVertices();
        for (int i = 0; i < vertices.length - 1; i++) {
            System.out.println("Dibujando línea de " + vertices[i] + " a " + vertices[i + 1] + " de color " + color);
        }
        System.out.println("Dibujando línea de " + vertices[vertices.length - 1] + " a " + vertices[0] + " de color " + color);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Pedir al usuario las dimensiones de las figuras
        System.out.print("Ingrese la cantidad de figuras que desea generar: ");
        int numFiguras = scanner.nextInt();
        scanner.nextLine(); // Consumir la nueva línea

        // Almacenar las figuras
        Polygon[] figuras = new Polygon[numFiguras];

        for (int i = 0; i < numFiguras; i++) {
            System.out.print("Ingrese el nombre de la figura " + (i + 1) + " (cuadrado, triangulo, rectangulo, pentagono, hexagono): ");
            String figura = scanner.nextLine().toLowerCase();

            if (figura.equals("cuadrado")) {
                System.out.print("Ingrese el tamaño del lado del cuadrado: ");
                double lado = scanner.nextDouble();
                System.out.print("Ingrese la coordenada x del punto de partida: ");
                double x = scanner.nextDouble();
                System.out.print("Ingrese la coordenada y del punto de partida: ");
                double y = scanner.nextDouble();
                figuras[i] = trasladarObjeto(crearCuadrado(lado), x, y);
            } else if (figura.equals("triangulo")) {
                System.out.print("Ingrese la longitud de la base del triángulo: ");
                double base = scanner.nextDouble();
                System.out.print("Ingrese la altura del triángulo: ");
                double altura = scanner.nextDouble();
                System.out.print("Ingrese la coordenada x del punto de partida: ");
                double x = scanner.nextDouble();
                System.out.print("Ingrese la coordenada y del punto de partida: ");
                double y = scanner.nextDouble();
                figuras[i] = trasladarObjeto(crearTriangulo(base, altura), x, y);
            } else if (figura.equals("rectangulo")) {
                System.out.print("Ingrese la longitud de la base del rectángulo: ");
                double base = scanner.nextDouble();
                System.out.print("Ingrese la altura del rectángulo: ");
                double altura = scanner.nextDouble();
                System.out.print("Ingrese la coordenada x del punto de partida: ");
                double x = scanner.nextDouble();
                System.out.print("Ingrese la coordenada y del punto de partida: ");
                double y = scanner.nextDouble();
                figuras[i] = trasladarObjeto(crearRectangulo(base, altura), x, y);
            } else if (figura.equals("pentagono")) {
                System.out.print("Ingrese el tamaño del lado del pentágono: ");
                double lado = scanner.nextDouble();
                System.out.print("Ingrese la coordenada x del punto de partida: ");
                double x = scanner.nextDouble();
                System.out.print("Ingrese la coordenada y del punto de partida: ");
                double y = scanner.nextDouble();
                figuras[i] = trasladarObjeto(crearPentagono(lado), x, y);
            } else if (figura.equals("hexagono")) {
                System.out.print("Ingrese el tamaño del lado del hexágono: ");
                double lado = scanner.nextDouble();
                System.out.print("Ingrese la coordenada x del punto de partida: ");
                double x = scanner.nextDouble();
                System.out.print("Ingrese la coordenada y del punto de partida: ");
                double y = scanner.nextDouble();
                figuras[i] = trasladarObjeto(crearHexagono(lado), x, y);
            } else {
                System.out.println("Figura no reconocida.");
                i--; // Intentar nuevamente para la misma posición
            }
            scanner.nextLine(); // Consumir la nueva línea
        }

        // Pedir al usuario las distancias de traslación
        System.out.print("Ingrese la distancia dx para la traslación: ");
        double dx = scanner.nextDouble();
        System.out.print("Ingrese la distancia dy para la traslación: ");
        double dy = scanner.nextDouble();

        // Dibujar los objetos originales
        for (Polygon figura : figuras) {
            dibujarObjeto(figura, "azul");
        }

        // Dibujar los objetos trasladados
        for (Polygon figura : figuras) {
            Polygon objetoTrasladado = trasladarObjeto(figura, dx, dy);
            dibujarObjeto(objetoTrasladado, "rojo");
        }
    }

    // Definir los objetos disponibles para dibujar con el tamaño personalizado
    public static Polygon crearCuadrado(double lado) {
        Vector2D[] vertices = { new Vector2D(0, 0), new Vector2D(lado, 0), new Vector2D(lado, lado),
                new Vector2D(0, lado) };
        return new Polygon(vertices);
    }

    public static Polygon crearTriangulo(double base, double altura) {
        Vector2D[] vertices = { new Vector2D(0, 0), new Vector2D(base, 0), new Vector2D(base / 2, altura) };
        return new Polygon(vertices);
    }

    public static Polygon crearRectangulo(double base, double altura) {
        Vector2D[] vertices = { new Vector2D(0, 0), new Vector2D(base, 0), new Vector2D(base, altura),
                new Vector2D(0, altura) };
        return new Polygon(vertices);
    }

    public static Polygon crearPentagono(double lado) {
        double apotema = lado / (2 * Math.tan(Math.PI / 5));
        double alpha = (Math.PI * 2) / 5;
        Vector2D[] vertices = new Vector2D[5];
        for (int i = 0; i < 5; i++) {
            vertices[i] = new Vector2D(lado * Math.cos(alpha * i), lado * Math.sin(alpha * i));
        }
        return new Polygon(vertices);
    }

    public static Polygon crearHexagono(double lado) {
        double apotema = lado * Math.sqrt(3) / 2;
        double alpha = (Math.PI * 2) / 6;
        Vector2D[] vertices = new Vector2D[6];
        for (int i = 0; i < 6; i++) {
            vertices[i] = new Vector2D(lado * Math.cos(alpha * i), lado * Math.sin(alpha * i));
        }
        return new Polygon(vertices);
    }
}
