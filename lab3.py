import tkinter as tk
from tkinter import messagebox
import random
import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("I'm A Believer.mp3")
pygame.mixer.music.play()

coding = []
for i in range(48, 58):
    coding.append(chr(i))
for i in range(65, 91):
    coding.append(chr(i))

def close():
    window.destroy()

def animation():
    color_now = lbl_key.cget("bg")
    new_color = "purple" if color_now == "pink" else "pink"
    lbl_key.config(bg=new_color, fg=color_now)
    
    window.after(700, animation)

def generate_key(offset):
    key = ''

    part_of_key = random.choices(population=coding, k=5)
    key += ''.join(part_of_key) + '-'

    for i in range(3):
        part_of_key = part_of_key[:-1]

        for j in range(4 - i):
            ind_letter = coding.index(part_of_key[j])
            part_of_key[j] = coding[(ind_letter + ((-1)**i)*int(offset[i]))%36]
            
        key += ''.join(part_of_key) + '-'

    key = key[:-1]

    return key

def calc():
    offset = str(number.get())

    if lbl_inf.cget("text") != 'You have a key!!! happy-happy':
        animation()
    if offset == '' or offset[0] == '0' or len(offset) > 3:
        tk.messagebox.showwarning('Error', 'Enter the number!')
    else:
        lbl_inf.configure(text='You have a key!!! happy-happy')
        lbl_inf.place(x=260, y=68)
        lbl_key.configure(text=generate_key(offset), font=("Georgia", 35), bg="pink", fg="purple")
        lbl_key.place(x=130, y=400)
    
    
window = tk.Tk()
window.title("Shrek's key (^з^)")

bg_image = tk.PhotoImage(file="image.png")
wind_width = bg_image.width()
wind_height = bg_image.height()

window.geometry(f"{wind_width}x{wind_height}")

bg_lbl = tk.Label(window, image=bg_image)
bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

number = tk.Entry(window)
number.insert(0, '123')
number.place(x=280, y=90)

lbl_inf = tk.Label(window, text="Enter a three digit number")
lbl_inf.place(x=270, y=68)

generation_btn = tk.Button(window, text="Your key is...", command=calc)
generation_btn.place(x=300, y=112)

lbl_key = tk.Label(window, text="I don't know...")
lbl_key.place(x=380, y=115)

window.mainloop()
