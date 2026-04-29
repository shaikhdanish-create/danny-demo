"""Modern 3D-style login page in Python.

This version uses customtkinter for a more modern UI (MUI-like look)
with layered cards and glow accents.
"""

import tkinter as tk
from tkinter import messagebox

try:
    import customtkinter as ctk
except ImportError as exc:  # noqa: F841
    raise SystemExit(
        "customtkinter is required. Install it with: pip install customtkinter"
    )


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class ModernLogin3D(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("MUI 3D Login")
        self.geometry("980x640")
        self.resizable(False, False)

        self._build_background()
        self._build_card()

    def _build_background(self) -> None:
        self.bg = tk.Canvas(self, width=980, height=640, highlightthickness=0, bg="#090f1f")
        self.bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Gradient-like bands
        shades = ["#070b17", "#0d1326", "#111b33", "#162447", "#1a2c57", "#21386d"]
        band_h = 640 // len(shades)
        for i, color in enumerate(shades):
            y0 = i * band_h
            self.bg.create_rectangle(0, y0, 980, y0 + band_h + 3, fill=color, outline="")

        # Soft blobs for depth
        blobs = [
            (130, 110, 170, "#233667"),
            (860, 120, 130, "#2c4686"),
            (840, 520, 190, "#1b2c5c"),
            (140, 520, 130, "#324f94"),
        ]
        for x, y, r, color in blobs:
            self.bg.create_oval(x - r, y - r, x + r, y + r, fill=color, outline="")

    def _build_card(self) -> None:
        # Shadow layers
        self.shadow_1 = ctk.CTkFrame(self, width=430, height=420, fg_color="#0a0f23", corner_radius=28)
        self.shadow_1.place(x=286, y=126)

        self.shadow_2 = ctk.CTkFrame(self, width=430, height=420, fg_color="#111a3a", corner_radius=26)
        self.shadow_2.place(x=278, y=118)

        # Main panel
        self.card = ctk.CTkFrame(
            self,
            width=430,
            height=420,
            fg_color="#1b2958",
            corner_radius=24,
            border_width=2,
            border_color="#4c78ff",
        )
        self.card.place(x=270, y=110)

        ctk.CTkLabel(
            self.card,
            text="Welcome Back",
            font=ctk.CTkFont(size=30, weight="bold"),
            text_color="#e4edff",
        ).place(relx=0.5, y=56, anchor="center")

        ctk.CTkLabel(
            self.card,
            text="Sign in to continue",
            font=ctk.CTkFont(size=14),
            text_color="#9fb8ff",
        ).place(relx=0.5, y=90, anchor="center")

        self.username = ctk.StringVar()
        self.password = ctk.StringVar()

        ctk.CTkLabel(self.card, text="Username", text_color="#cfe0ff", font=ctk.CTkFont(size=13)).place(x=70, y=140)
        self.user_entry = ctk.CTkEntry(
            self.card,
            width=290,
            height=42,
            textvariable=self.username,
            corner_radius=12,
            fg_color="#283a73",
            border_color="#7ea0ff",
            text_color="#f1f6ff",
            placeholder_text="Enter username",
        )
        self.user_entry.place(x=70, y=168)

        ctk.CTkLabel(self.card, text="Password", text_color="#cfe0ff", font=ctk.CTkFont(size=13)).place(x=70, y=228)
        self.pass_entry = ctk.CTkEntry(
            self.card,
            width=290,
            height=42,
            textvariable=self.password,
            show="•",
            corner_radius=12,
            fg_color="#283a73",
            border_color="#7ea0ff",
            text_color="#f1f6ff",
            placeholder_text="Enter password",
        )
        self.pass_entry.place(x=70, y=256)

        self.login_btn = ctk.CTkButton(
            self.card,
            text="LOGIN",
            width=290,
            height=46,
            corner_radius=14,
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#3f6fff",
            hover_color="#5c86ff",
            command=self._on_login,
        )
        self.login_btn.place(x=70, y=330)

    def _on_login(self) -> None:
        user = self.username.get().strip()
        pwd = self.password.get().strip()

        if not user or not pwd:
            messagebox.showwarning("Missing fields", "Please fill in both username and password.")
            return

        messagebox.showinfo("Login success", f"Welcome, {user}! (Demo)")


def main() -> None:
    app = ModernLogin3D()
    app.mainloop()


if __name__ == "__main__":
    main()
