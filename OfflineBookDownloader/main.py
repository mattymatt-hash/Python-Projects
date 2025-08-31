import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import tkinter as tk
from gui import App
from storage import StorageManager

if __name__ == "__main__":
    StorageManager.initialize_db()
    root = tk.Tk()
    app = App(root)
    app.load_books()
    root.mainloop()
