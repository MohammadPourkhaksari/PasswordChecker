import tkinter as tk
from Password_check import check_password  # مطمئن شو فایل اسمش همینه

def evaluate_password(event=None):
    pwd = entry.get()
    score, strength, feedback, crack_time, brute_time = check_password(pwd)

    # نمایش امتیاز و قدرت
    result_var.set(f"Score: {score} - {strength}")

    # رنگ‌بندی بر اساس قدرت
    colors = {"Strong": "green", "Medium": "orange", "Weak": "red"}
    result_label.config(fg=colors.get(strength, "black"))

    # نمایش تخمین زمان کرک شدن
    time_text = f"Estimated crack time: {crack_time}\nBrute-force @1B guesses/sec: {brute_time}"
    time_var.set(time_text)

    # نمایش پیشنهادها
    feedback_text = "\n".join(feedback) if feedback else "✅ No suggestions, your password looks strong!"
    feedback_var.set(feedback_text)

def toggle_password():
    if entry.cget("show") == "":
        entry.config(show="*")
        toggle_btn.config(text="Show")
    else:
        entry.config(show="")
        toggle_btn.config(text="Hide")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("550x400")
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

# نمایش نتیجه (امتیاز + قدرت)
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Segoe UI", 14, "bold"))
result_label.pack(pady=10)

# نمایش زمان تقریبی کرک
time_var = tk.StringVar()
time_label = tk.Label(root, textvariable=time_var, font=("Segoe UI", 10), fg="purple", justify="left")
time_label.pack(pady=5)

# نمایش پیشنهادها
feedback_var = tk.StringVar()
feedback_label = tk.Label(root, textvariable=feedback_var, font=("Segoe UI", 10), fg="blue", justify="left")
feedback_label.pack(pady=5)

root.mainloop()
