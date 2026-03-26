import tkinter as tk


def main() -> None:
    root = tk.Tk()
    root.title("Hola Mundo")
    root.geometry("320x120")

    label = tk.Label(root, text="¡Hola, mundo!", font=("Segoe UI", 18))
    label.pack(expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()
