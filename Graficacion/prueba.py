import sys

def print_pixel(rgb):
    sys.stdout.write("\x1b[48;2;{};{};{}m \x1b[0m".format(rgb[0], rgb[1], rgb[2]))

def main():
    print("Bienvenido al generador de píxeles inspirado en Asteroids de Atari")
    sequence = input("Por favor ingresa la secuencia de colores (por ejemplo, 1): ")
    
    try:
        sequence = int(sequence)
    except ValueError:
        print("La secuencia debe ser un número entero.")
        return
    
    if sequence < 1 or sequence > 255:
        print("La secuencia debe estar entre 1 y 255.")
        return
    
    color = [0, 0, 0]

    for i in range(256):
        print_pixel(color)
        color[2] += sequence

        if color[2] > 255:
            color[2] = color[2] % 256
            color[1] += 1

        if color[1] > 255:
            color[1] = color[1] % 256
            color[0] += 1

        if color[0] > 255:
            break
        
        if i % 64 == 63:
            print()

if __name__ == "__main__":
    main()