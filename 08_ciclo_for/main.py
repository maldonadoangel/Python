import turtle
import time

def configurar_pantalla():
    """Configura las dimensiones y el título de la ventana."""
    pantalla = turtle.Screen()
    pantalla.title("Mi primer script de con ciclo for")
    pantalla.setup(width=800, height=600)
    return pantalla

def crear_tortuga(color_trazo, velocidad):
    """Crea y personaliza el objeto tortuga."""
    t = turtle.Turtle()
    t.speed(velocidad)
    t.color(color_trazo)
    t.shape("turtle") # Le damos forma de tortuga
    return t

def dibujar_cuadrado(t, lado):
    """Recibe una tortuga y dibuja un cuadrado del tamaño especificado."""
    for i in range(4):
        t.forward(lado)
        t.right(90)
        print(f"Lado {i+1} completado")

def main():
    """Función principal que orquestará el dibujo."""
    # 1. Preparación
    configurar_pantalla()
    mi_tortuga = crear_tortuga("blue", 1)
    
    print("Iniciando dibujo...")
    time.sleep(2)
    
    # 2. Ejecución
    dibujar_cuadrado(mi_tortuga, 100)
    
    # 3. Finalización
    print("Dibujo finalizado.")
    time.sleep(5)

if __name__ == "__main__":
    main()