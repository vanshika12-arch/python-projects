import tkinter as tk
import validators

def check_url():
    url = entry.get()

    if not validators.url(url):
        result_label.config(text="❌ Invalid URL", fg="red")
        return

    if not url.startswith("https"):
        result_label.config(text="⚠ HTTPS missing – Possible phishing", fg="orange")

    elif "@" in url:
        result_label.config(text="⚠ '@' found – Possible phishing", fg="orange")

    elif "-" in url:
        result_label.config(text="⚠ Suspicious domain detected", fg="orange")

    elif "login" in url or "verify" in url or "bank" in url or "secure" in url:
        result_label.config(text="⚠ Suspicious keywords detected", fg="orange")

    elif len(url) > 75:
        result_label.config(text="⚠ URL too long – Possible phishing", fg="orange")

    else:
        result_label.config(text="✔ This link looks safe", fg="green")


# Create window
window = tk.Tk()
window.title("AI Phishing Detection Tool")
window.geometry("450x250")

title = tk.Label(window, text="Phishing Detection Tool", font=("Arial", 16))
title.pack(pady=10)

entry = tk.Entry(window, width=40)
entry.pack(pady=10)

scan_button = tk.Button(window, text="Scan URL", command=check_url)
scan_button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=20)

window.mainloop()