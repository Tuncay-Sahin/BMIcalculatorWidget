import tkinter as tk
from tkinter import messagebox
from tkinter import font

window = tk.Tk()
window.title("BMI Calculator")

#widget boyutunu ayarla
window.geometry("400x300")

#yazı fontunu ayarla
font_label = font.Font(size=12, weight="bold")
font_button = font.Font(size=12)

label = font_label
label_weight = tk.Label(window, text="Weight (kg): ", font=font_label)
label_weight.pack()

entry_weight = tk.Entry(window, font=font_label)
entry_weight.pack()

label_height = tk.Label(window, text="Height (cm): ", font=font_label)
label_height.pack()

entry_height = tk.Entry(window, font=font_label)
entry_height.pack()

def calculate_bmi():
    weight_entry = entry_weight.get()
    height_entry = entry_height.get()

    if weight_entry == "" or height_entry == "":
        messagebox.showerror("Hata", "Lütfen kilunuzu ve boyunuzu girin.")
        return

    try:
        weight = float(weight_entry)
        height = float(height_entry) / 100

        if weight <= 0 or height <= 0:
            messagebox.showerror("Hata", "Geçerli bir kilo ve boy değeri girin.")
            return

        bmi = weight / (height * height)

        if bmi < 18.5:
            category = "Zayıf"
        elif 18.5 <= bmi < 25:
            category = "Normal"
        elif 25 <= bmi < 30:
            category = "Fazla Kilolu"
        elif 30 <= bmi < 35:
            category = "Şişman (Obezite - Tip 1)"
        elif 35 <= bmi < 40:
            category = "Şişman (Obezite - Tip 2)"
        else:
            category = "Şişman (Aşırı Obezite)"


        result_label.config(text="BMI: %2f (%s)" % (bmi, category), font=font_label)

    except ValueError:
        messagebox.showerror("Hata", "Geçerli bir kilo ve boy değeri girin.")

calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi, font=font_button, bg="grey", fg="black")
calculate_button.pack()

result_label = tk.Label(window, font=font_label)
result_label.pack()

window.mainloop()


