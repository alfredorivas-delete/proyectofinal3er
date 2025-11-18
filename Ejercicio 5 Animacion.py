#Ejercicio 5

import os
import tkinter as tk
from PIL import Image, ImageTk,ImageSequence
import threading

 #try:
 #   from playsound import playsound
 #except ImportError:
 #    from playsound3 import playsound

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
class AnimatedGif(tk.Label):
    def __init__(self, master, gif_path: str, delay: int = 80): 
        image = Image.open(gif_path)
        self.frames = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(image)] 
        self.delay = delay 
        self.idx = 0 
        super().__init__(master, image=self.frames[0])
        self.after(self.delay, self._animate)
    def _animate(self):
        self.idx = (self.idx + 1) % len(self.frames) 
        self.configure(image=self.frames[self.idx])
        self.after(self.delay, self._animate)
def main():
    root = tk.Tk()
    root.title('Animación con sonido')
    root.geometry('400x400')
    gif_path = os.path.join(BASE_DIR, 'animation.gif')
    sound_path = os.path.join(BASE_DIR, 'boing.wav')
    gif_widget = AnimatedGif(root, gif_path, delay=80)
    gif_widget.pack(expand=True)

    gif_path = os.path.join(BASE_DIR, 'animation2.gif')
    sound_path = os.path.join(BASE_DIR, 'boing.wav')
    gif_widget = AnimatedGif(root, gif_path, delay=80)
    gif_widget.pack(expand=True)
    root.mainloop()

if __name__ == '__main__':
    main()