'''
"-ESTE NO ES EL ARCHIVO DE LA ACTIVIDAD, SOLAMENTE ES UN SEMAFORO DE PRUEBA-"

Este programa solamente es un semaforo, fue lo primero que realize algo muy normal. Solamente es algo extra. Ya que 
este lo realice con tkinter viendo la documentacion para saber como utilizarlo y el sistema en si solamente
son contadores, se espera cada cierto tiempo y ya. No es como el otro codigo que realice que ese si esta creo todo correcto.
'''

import tkinter as tk

class TrafficLight:
    def __init__(self, master):
        self.master = master
        self.master.title("Semáforo")
        self.master.geometry("200x300")
        self.master.resizable(False, False)
        self.color = "red"
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=100, height=250)
        self.canvas.pack(pady=20)
        self.canvas.create_rectangle(25, 25, 75, 225, fill="black")
        self.red_light = self.canvas.create_oval(35, 35, 65, 65, fill="gray")
        self.yellow_light = self.canvas.create_oval(35, 95, 65, 125, fill="gray")
        self.green_light = self.canvas.create_oval(35, 155, 65, 185, fill="gray")
        self.change_color()

    def change_color(self):
        if self.color == "red":
            self.canvas.itemconfig(self.red_light, fill="red")
            self.canvas.itemconfig(self.yellow_light, fill="gray")
            self.canvas.itemconfig(self.green_light, fill="gray")
            self.color = "yellow"
            time = 3000
        elif self.color == "yellow":
            self.canvas.itemconfig(self.red_light, fill="gray")
            self.canvas.itemconfig(self.yellow_light, fill="yellow")
            time = 1000
            if not cambiarsemaforo():
                time *= 2
            self.color = "green"
        else:
            self.canvas.itemconfig(self.yellow_light, fill="gray")
            self.canvas.itemconfig(self.green_light, fill="green")
            time = 3000
            if cambiarsemaforo():
                time *= 2
            self.color = "red"
        self.master.after(time, self.change_color)

def cambiarsemaforo():
    return False

if __name__ == "__main__":
    root = tk.Tk()
    app = TrafficLight(root)
    root.mainloop()
