import tkinter as tk
from time import strftime


root = tk.Tk()
root.title("Classy Digital Clock by Suraj")
root.geometry("800x400")
root.configure(bg="#0a0a0a")
root.resizable(False, False)


is_24hr = False  # toggle variable

def time():
    if is_24hr:
        string = strftime('%H:%M:%S')
    else:
        string = strftime('%I:%M:%S %p')
    label_time.config(text=string)
    label_time.after(1000, time)
    update_greeting()


def update_greeting():
    hour = int(strftime('%H'))
    if 5 <= hour < 12:
        greet = "Good Morning, Suraj ☀️"
    elif 12 <= hour < 18:
        greet = "Good Afternoon, Suraj 🌤️"
    else:
        greet = "Good Evening, Suraj 🌙"
    label_greet.config(text=greet)


def toggle_format():
    global is_24hr
    is_24hr = not is_24hr
    btn_toggle.config(text="24-Hour Format" if not is_24hr else "12-Hour Format")


label_time = tk.Label(
    root,
    font=('ds-digital', 90, 'bold'),
    background='#0a0a0a',
    foreground='#00ffff'
)
label_time.pack(pady=(60, 10))


label_greet = tk.Label(
    root,
    font=('Segoe UI', 20, 'italic'),
    background='#0a0a0a',
    foreground='#d4d4d4'
)
label_greet.pack()


label_date = tk.Label(
    root,
    text=strftime("%A, %B %d, %Y"),
    font=('Consolas', 16),
    background='#0a0a0a',
    foreground='#888'
)
label_date.pack(pady=(10, 20))


btn_toggle = tk.Button(
    root,
    text="24-Hour Format",
    command=toggle_format,
    font=('Arial', 12, 'bold'),
    bg="#111",
    fg="cyan",
    activebackground="#222",
    activeforeground="white",
    relief="flat",
    cursor="hand2"
)
btn_toggle.pack(pady=5)


def glow_text():
    current = label_time.cget("foreground")
    new_color = "#00ffff" if current == "#00cccc" else "#00cccc"
    label_time.config(foreground=new_color)
    root.after(700, glow_text)


time()
glow_text()
root.mainloop()
