import tkinter as tk



import os



from tkinter import messagebox




timer_running = None




def run_command(cmd_type):


    global timer_running




    try:
        seconds = int(entry_time.get())
    except ValueError:
        messagebox.showerror("помилка", "Введіть число секунд!")
        return
    
    if cmd_type == "shutdown":
        if messagebox.askyesno("Підтвердження", f"Вимкнути ПК через {seconds} сек?"):
            os.system(f"shutdown /s /t {seconds}")
            start_ui_countdown(seconds)
    
    elif cmd_type == "restart":

        os.system(f"shutdown /r /t {seconds}")

        start_ui_countdown(seconds)

    elif cmd_type == "cancel":

        os.system("shutdown /a")


        if timer_running:
            root.after_cancel(timer_running)

            label_countdown.config(text="Таймер зупинено", fg="white")
            messagebox.showinfo("Скасовано", "Всі команди скасовані")
            timer_running = None

def start_ui_countdown(time_left):
    global timer_running

    if time_left > 0:


        label_countdown.config(text=f"До діі залишилось: {time_left} сек", fg="#e74c3c")
        



        timer_running = root.after(1000, start_ui_countdown, time_left - 1)
    else:

        label_countdown.config(text="Время вышло!", fg="white")

def open_folder():


    os.startfile(os.getcwd())


root = tk.Tk()
root.title("Ультра Менеджер Питання Pro")
root.geometry("450x600")
root.config(bg="#1a1a1a")

tk.Label(root, text="Управление системной", font=("Courier New", 20, "bold"),
             bg="#1a1a1a", fg="#00ff00").pack(pady=20)



tk.Label(root, text="Введите время в секундах:", bg="#1a1a1a", fg="white").pack()



entry_time = tk.Entry(root, font=("Arial", 14), justify="center", width=10)


entry_time.insert(0, "60")


entry_time.pack(pady=10)


label_countdown = tk.Label(root, text="Таймер не запущен", font=("Arial", 12),
                            bg="#1a1a1a", fg="gray")
label_countdown.pack(pady=10)



btn_style = {"width": 25, "height": 2, "font": ("Arial", 10, "bold")}



tk.Button(root, text="Выключить пк", bg="#c0392b", fg="white",
          command=lambda: run_command("shutdown"), **btn_style).pack(pady=5)


tk.Button(root, text="Открыть папку проекта", bg="#2980b9", fg="white",
          command=open_folder, **btn_style).pack(pady=5)


tk.Button(root, text="отменить", bg="#27ae60", fg="white",
          command=lambda: run_command("cancel"), **btn_style).pack(pady=20)


info_text = f"Пользователь: {os.getlogin()} ОС: {os.name}"



tk.Label(root, text=info_text, bg="#1a1a1a", fg="#555", font=("Arial", 8)).pack(side="bottom")


root.mainloop()





















































