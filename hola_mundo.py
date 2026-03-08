import tkinter as tk


def main() -> None:
    root = tk.Tk()
    root.title("Hola Mundo")
    root.geometry("320x180")

    label = tk.Label(root, text="Hola Mundo", font=("Segoe UI", 24))
    label.pack(expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()
