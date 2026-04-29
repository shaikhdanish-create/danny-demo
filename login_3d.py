import tkinter as tk
from tkinter import messagebox


class Login3DApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("3D Login Page")
        self.root.geometry("900x600")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(root, width=900, height=600, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self._draw_background()
        self._draw_login_card()

    def _draw_background(self) -> None:
        # Layered gradient-like backdrop using bands.
        colors = [
            "#070b1a", "#0a1024", "#0d1531", "#121b40", "#172252", "#1e2b66", "#27357c"
        ]
        band_height = 600 // len(colors)
        for i, color in enumerate(colors):
            y0 = i * band_height
            y1 = y0 + band_height + 2
            self.canvas.create_rectangle(0, y0, 900, y1, fill=color, outline="")

        # Floating decorative circles for depth.
        for x, y, r, color in [
            (140, 120, 120, "#24315f"),
            (760, 130, 90, "#2b3f7f"),
            (760, 470, 140, "#1f2d58"),
            (140, 470, 95, "#314b8f"),
        ]:
            self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=color, outline="")

    def _draw_login_card(self) -> None:
        # Faux 3D shadow layers.
        self.canvas.create_rectangle(248, 138, 652, 462, fill="#080d20", outline="", width=0)
        self.canvas.create_rectangle(242, 132, 646, 456, fill="#111935", outline="", width=0)

        # Foreground card.
        self.canvas.create_rectangle(235, 125, 640, 450, fill="#1a2550", outline="#4f79ff", width=2)

        self.canvas.create_text(
            438,
            175,
            text="WELCOME BACK",
            fill="#dce7ff",
            font=("Segoe UI", 24, "bold"),
        )
        self.canvas.create_text(
            438,
            210,
            text="Login to continue",
            fill="#9bb3ff",
            font=("Segoe UI", 12),
        )

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        # Entry frame with subtle depth effect.
        self._draw_labeled_entry("Username", self.username_var, 270)
        self._draw_labeled_entry("Password", self.password_var, 340, show="•")

        login_button = tk.Button(
            self.root,
            text="LOGIN",
            command=self._login,
            font=("Segoe UI", 12, "bold"),
            fg="#ffffff",
            bg="#3d6cff",
            activebackground="#5b84ff",
            activeforeground="#ffffff",
            bd=0,
            cursor="hand2",
            padx=28,
            pady=10,
        )
        self.canvas.create_window(438, 400, window=login_button)

    def _draw_labeled_entry(
        self,
        label: str,
        variable: tk.StringVar,
        y: int,
        show: str | None = None,
    ) -> None:
        self.canvas.create_text(305, y - 25, text=label, fill="#c4d3ff", font=("Segoe UI", 11), anchor="w")

        # Lower layer (shadow)
        self.canvas.create_rectangle(302, y + 6, 574, y + 46, fill="#0d1532", outline="")
        # Upper layer (input background)
        self.canvas.create_rectangle(298, y + 2, 570, y + 42, fill="#2a3970", outline="#7898ff", width=1)

        entry = tk.Entry(
            self.root,
            textvariable=variable,
            show=show,
            font=("Segoe UI", 12),
            fg="#e9f0ff",
            bg="#2a3970",
            insertbackground="#ffffff",
            relief="flat",
            bd=0,
            width=24,
        )
        self.canvas.create_window(434, y + 22, window=entry)

    def _login(self) -> None:
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()

        if not username or not password:
            messagebox.showwarning("Missing Data", "Please enter both username and password.")
            return

        messagebox.showinfo("Login", f"Welcome, {username}! (Demo login)")


def main() -> None:
    root = tk.Tk()
    Login3DApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
