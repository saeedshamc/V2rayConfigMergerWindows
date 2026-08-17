# -*- coding: utf-8 -*-
"""
V2Ray Config Merger
دانلود و ادغام کانفیگ‌های V2Ray از دو منبع
"""
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import urllib.request
import threading
import os

SOURCE_1 = {
    "name": "V2RAYCONFIGSPOOL/V2RAY_SUB",
    "url_template": "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/main/v2ray_configs_no{i}.txt",
    "count": 10,
    "label_template": "v2ray_configs_no{i}.txt",
}

SOURCE_2 = {
    "name": "barry-far/V2ray-Config",
    "url_template": "https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub{i}.txt",
    "count": 12,
    "label_template": "barry-far_Sub{i}.txt",
}

SOURCES = [SOURCE_1, SOURCE_2]


class MergerApp:
    def __init__(self, root):
        self.root = root
        root.title("V2Ray Config Merger")
        root.geometry("560x420")
        root.resizable(False, False)

        title = tk.Label(root, text="ادغام‌کننده کانفیگ‌های V2Ray", font=("Tahoma", 14, "bold"))
        title.pack(pady=10)

        subtitle = tk.Label(
            root,
            text="دانلود و ادغام از دو منبع:\n1) V2RAYCONFIGSPOOL/V2RAY_SUB\n2) barry-far/V2ray-Config",
            font=("Tahoma", 10),
            justify="center",
        )
        subtitle.pack(pady=5)

        out_frame = tk.Frame(root)
        out_frame.pack(pady=10, fill="x", padx=20)

        tk.Label(out_frame, text="مسیر خروجی:", font=("Tahoma", 10)).pack(side="left")
        self.output_path = tk.StringVar(value=os.path.join(os.getcwd(), "merged.txt"))
        entry = tk.Entry(out_frame, textvariable=self.output_path, font=("Tahoma", 9))
        entry.pack(side="left", fill="x", expand=True, padx=5)
        tk.Button(out_frame, text="انتخاب...", command=self.choose_path).pack(side="left")

        self.progress = ttk.Progressbar(root, length=500, mode="determinate")
        self.progress.pack(pady=15)

        self.log = tk.Text(root, height=10, width=68, font=("Consolas", 9))
        self.log.pack(padx=20)
        self.log.config(state="disabled")

        self.start_btn = tk.Button(
            root, text="شروع دانلود و ادغام", font=("Tahoma", 11, "bold"),
            bg="#2d7", fg="white", command=self.start_thread
        )
        self.start_btn.pack(pady=10)

    def choose_path(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            initialfile="merged.txt",
            filetypes=[("Text file", "*.txt")],
        )
        if path:
            self.output_path.set(path)

    def log_line(self, text):
        self.log.config(state="normal")
        self.log.insert("end", text + "\n")
        self.log.see("end")
        self.log.config(state="disabled")
        self.root.update_idletasks()

    def start_thread(self):
        self.start_btn.config(state="disabled")
        threading.Thread(target=self.run, daemon=True).start()

    def run(self):
        out_path = self.output_path.get()
        total = sum(s["count"] for s in SOURCES)
        self.progress["maximum"] = total
        self.progress["value"] = 0

        try:
            if os.path.exists(out_path):
                os.remove(out_path)

            with open(out_path, "a", encoding="utf-8") as f:
                for source in SOURCES:
                    for i in range(1, source["count"] + 1):
                        url = source["url_template"].format(i=i)
                        label = source["label_template"].format(i=i)
                        self.log_line(f"در حال دانلود: {url}")
                        try:
                            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
                            with urllib.request.urlopen(req, timeout=15) as resp:
                                content = resp.read().decode("utf-8", errors="ignore")
                            f.write(f"===== {label} =====\n")
                            f.write(content)
                            f.write("\n\n")
                            self.log_line(f"  موفق: {label}")
                        except Exception as e:
                            self.log_line(f"  ناموفق: {label} ({e})")
                        self.progress["value"] += 1
                        self.root.update_idletasks()

            self.log_line(f"\nپایان یافت! خروجی ذخیره شد در:\n{out_path}")
            messagebox.showinfo("انجام شد", f"فایل ادغام‌شده ذخیره شد:\n{out_path}")
        except Exception as e:
            messagebox.showerror("خطا", str(e))
        finally:
            self.start_btn.config(state="normal")


if __name__ == "__main__":
    root = tk.Tk()
    MergerApp(root)
    root.mainloop()
