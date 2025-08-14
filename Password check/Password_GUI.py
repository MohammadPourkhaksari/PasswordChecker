import tkinter as tk
from Password_check import check_password  # حتماً فایل منطق درست باشه

def evaluate_password(event=None):
    pwd = entry.get()
    score, strength = check_password(pwd)
    result_var.set(f"Score: {score} - {strength}")
    colors = {"Strong": "green", "Medium": "orange", "Weak": "red"}
    result_label.config(fg=colors.get(strength, "black"))

def toggle_password():
    if entry.cget("show") == "":
        entry.config(show="*")
        toggle_btn.config(text="Show")
    else:
        entry.config(show="")
        toggle_btn.config(text="Hide")

root = tk.Tk()
root.title("Password Checker")
root.geometry("450x250")  # اندازه بزرگتر
root.resizable(False, False)

# برچسب
tk.Label(root, text="Enter password:", font=("Segoe UI", 12)).pack(pady=10)

# فریم برای ورودی و دکمه
frame = tk.Frame(root)
frame.pack(fill="x", padx=20)

entry = tk.Entry(frame, show="*", font=("Segoe UI", 12))
entry.pack(side="left", fill="x", expand=True)
entry.bind("<Return>", evaluate_password)

toggle_btn = tk.Button(frame, text="Show", command=toggle_password)
toggle_btn.pack(side="left", padx=5)

# دکمه بررسی
tk.Button(root, text="Check", font=("Segoe UI", 12), command=evaluate_password).pack(pady=15)

# نمایش نتیجه
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Segoe UI", 14, "bold"))
result_label.pack(pady=10)

root.mainloop()
