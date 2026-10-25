import tkinter as tk
import random
import pygame

def generate_block():
    letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    block = random.choices(letters, k=3)+random.choices(numbers, k=2)
    random.shuffle(block)
    return ''.join(block)

def generate_code():
    return f'{generate_block()}-{generate_block()}-{generate_block()}'

def quit():
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    window.destroy()

colors = ['red', 'yellow', 'green', 'blue']
color=0

def animate():
    global color
    label1.config(bg=colors[color])
    color = (color+1)%len(colors)
    window.after(500, animate)


window = tk.Tk()
window.title('Water and Fire')
window.geometry('640x360')
window.resizable(0, 0)
bg_img = tk.PhotoImage(file = 'bg.png')


pygame.mixer.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

bg_label = tk.Label(window, image=bg_img)
bg_label.place(x=0, y=0, relwidth = 1, relheight=1)

label1 = tk.Label(window, text='Welcome', font = 'Arial 20')
label1.grid(row=0, column=0, columnspan=3, pady=30, sticky='n')

key_label = tk.Label(window, text = f'шифр: {generate_code()}', font = 'Arial 20')
key_label.grid(row=1, column = 0, columnspan=3, pady=20, sticky='n')

def update_key():
    key_label.config(text=f'шифр: {generate_code()}')

btn_gen = tk.Button(window, text='Generate Key', width=15, command=update_key)
btn_gen.grid(row=4, column=0, columnspan=3, pady=40, sticky='n')

btn = tk.Button(window, text='Exit', width=15, command=quit)

window.grid_rowconfigure(2, weight=5)
btn.grid(row=5, column=0, columnspan=3, pady=40, sticky='n')

animate()
window.mainloop()
