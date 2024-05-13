import tkinter as tk
import random

class JuegoDel15(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.tablero = self.iniciar_tablero()
        self.botones = {}
        self.crear_interfaz()

    def iniciar_tablero(self):
        tablero = list(range(1, 16)) + [None]
        random.shuffle(tablero)
        while not self.es_resoluble(tablero):
            random.shuffle(tablero)
        return tablero

    def es_resoluble(self, tablero):
        inversiones = 0
        lista = [x for x in tablero if x is not None]
        for i in range(len(lista)):
            for j in range(i + 1, len(lista)):
                if lista[i] > lista[j]:
                    inversiones += 1
        return inversiones % 2 == 0

    def crear_interfaz(self):
        self.master.title("Juego del 15")
        for i in range(4):
            for j in range(4):
                idx = 4 * i + j
                texto = '' if self.tablero[idx] is None else str(self.tablero[idx])
                boton = tk.Button(self.master, text=texto, width=10, height=3, 
                                  command=lambda idx=idx: self.mover(idx))
                boton.grid(row=i, column=j)
                self.botones[idx] = boton

    def mover(self, idx):
        filas, columnas = idx // 4, idx % 4
        vecinos = []

        # Agregar vecinos potenciales con comprobación de límites
        if filas > 0:  # Puede mover hacia arriba
            vecinos.append(idx - 4)
        if filas < 3:  # Puede mover hacia abajo
            vecinos.append(idx + 4)
        if columnas > 0:  # Puede mover hacia la izquierda
            vecinos.append(idx - 1)
        if columnas < 3:  # Puede mover hacia la derecha
            vecinos.append(idx + 1)

        for vecino in vecinos:
            if self.tablero[vecino] is None:
                self.tablero[idx], self.tablero[vecino] = self.tablero[vecino], self.tablero[idx]
                self.actualizar_interfaz()
                if self.juego_ganado():
                    print("¡Felicidades! Has ganado el juego.")
                break


    def actualizar_interfaz(self):
        for idx, boton in self.botones.items():
            texto = '' if self.tablero[idx] is None else str(self.tablero[idx])
            boton.config(text=texto)

    def juego_ganado(self):
        return self.tablero[:-1] == list(range(1, 16))

def main():
    root = tk.Tk()
    juego = JuegoDel15(master=root)
    juego.mainloop()

if __name__ == "__main__":
    main()
