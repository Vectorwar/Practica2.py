import tkinter as tk
from tkinter import Label


class EventApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Estos son los eventos con sus coordenadas")
        self.root.geometry("500x500")

        self.event_label = Label(self.root, text="Aqui se mostrarán los eventos", bg="white", fg="black",
                                 font=("Arial", 12), wraplength=450)
        self.event_label.pack(pady=20, fill="both", expand=True)

        self.root.bind("<Button-1>", self.mouse_click)
        self.root.bind("<Button-2>", self.mouse_middle_click)
        self.root.bind("<Button-3>", self.mouse_right_click)
        self.root.bind("<Motion>", self.mouse_motion)
        self.root.bind("<Double-1>", self.double_click)
        self.root.bind("<Key>", self.key_press)
        self.root.bind("<space>", self.clear_text)

    def mouse_click(self, event):
        text = f"Clic izquierdo en ({event.x}, {event.y})"
        self.update_label(text)

    def mouse_middle_click(self, event):
        text = f"Clic botón central en ({event.x}, {event.y})"
        self.update_label(text)

    def mouse_right_click(self, event):
        text = f"Clic derecho en ({event.x}, {event.y})"
        self.update_label(text)

    def mouse_motion(self, event):
        text = f"Movimiento del ratón en ({event.x}, {event.y})"
        self.update_label(text)

    def double_click(self, event):
        text = "Doble clic detectado: Cambiando color de fondo"
        self.update_label(text)
        self.root.config(bg="pink")

    def key_press(self, event):
        text = f"Tecla presionada: {event.keysym}"
        self.update_label(text)

    def clear_text(self, event):
        self.update_label("Etiqueta limpiada")
        self.root.config(bg="white")

    def update_label(self, text):
        self.event_label.config(text=text)

if __name__ == "__main__":
    root = tk.Tk()
    app = EventApp(root)
    root.mainloop()
