import tkinter as tk
from interface.app import GrafoApp

def main():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}")

    app = GrafoApp(root)

    # Encerrar aplicação corretamente ao fechar a janela
    root.protocol("WM_DELETE_WINDOW", lambda: (root.quit(), root.destroy()))

    root.mainloop()

if __name__ == "__main__":
    main()