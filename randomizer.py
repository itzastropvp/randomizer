import customtkinter as ctk
import random
app = ctk.CTk()
app.title("Рандомайзер")
app.geometry("500x200")
app.resizable(False, False)
def randomizer():
    randomka = random.randint(int(entry1.get()), int(entry2.get()))
    number.configure(text = randomka)
    return randomka
text1 = ctk.CTkLabel(app, text = "min", font = ("Arial", 18))
text1.place(x = 114, y = 5)
entry1 = ctk.CTkEntry(app, width = 100, font = ("Arial", 16))
entry1.place(x = 78, y = 30)
text2 = ctk.CTkLabel(app, text = "max", font = ("Arial", 18))
text2.place(x = 112, y = 114)
entry2 = ctk.CTkEntry(app, width = 100, font = ("Arial", 16))
entry2.place(x = 80, y = 140)
button = ctk.CTkButton(app, text="Генерувати", font = ("Arial", 20), width = 170, height = 50, corner_radius=8, fg_color="#004a99", hover_color="#003d7a", command=randomizer)
button.place(x = 270, y = 70)
number = ctk.CTkLabel(app, text = "", font = ("Arial", 40))
number.place(x = 20, y = 70)
app.mainloop()