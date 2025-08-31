import tkinter as tk 
from tkinter import ttk, messagebox, filedialog
from scraper import BookScraper, HTMLBookScraper
from storage import StorageManager
import os
import re
import time
import sqlite3
import subprocess
from datetime import datetime

def log_message(*args):
   
    """
      Logs messages with timestamp to console
    """
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    print(timestamp, *args)

class App:
    """
    Main app gui
    Provides interface 
    """

    def __init__(self, root):
        """
        Initializes gui layout and widgets
        """
        self.root = root
        self.root.title("Offline Book Downloader")
        self.root.geometry("1000x600")
        self.root.configure(bg="#f0f0f0")
        self.last_saved_folder = None

        # Main layout 
        main_frame = tk.Frame(root, bg="#f0f0f0")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        left_frame = tk.Frame(main_frame, bg="#f0f0f0")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        right_frame = tk.Frame(main_frame, bg="#ffffff", bd=2, relief=tk.GROOVE)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Book list/controls
        tk.Label(left_frame, text="Saved Books (from DB):", bg="#f0f0f0", font=("Arial", 12, "bold")).pack(pady=(10, 0))
        self.book_listbox = tk.Listbox(left_frame, height=10, width=60)
        self.book_listbox.pack()
        self.book_count_label = tk.Label(left_frame, text="Total Books: 0", bg="#f0f0f0")
        self.book_count_label.pack()

        # buttons
        btn_frame = tk.Frame(left_frame, bg="#f0f0f0")
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text="Refresh List", command=self.load_books).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Delete Selected", command=self.delete_selected_book).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="View Content", command=self.view_selected_book).pack(side=tk.LEFT, padx=5)

        #input
        tk.Label(left_frame, text="Enter Book URLs (one per line):", bg="#f0f0f0", font=("Arial", 11)).pack()
        self.url_text = tk.Text(left_frame, height=6, width=60)
        self.url_text.pack()

        # save as selection
        tk.Label(left_frame, text="Save As:", bg="#f0f0f0").pack()
        self.format_var = tk.StringVar(value="pdf")
        self.format_menu = ttk.Combobox(left_frame, textvariable=self.format_var, values=["pdf", "csv", "db"])
        self.format_menu.pack()

        tk.Button(left_frame, text="Download", command=self.download).pack(pady=10)

        # Progress bar
        self.progress = ttk.Progressbar(left_frame, length=300, mode='determinate')
        self.progress.pack(pady=5)
        self.progress.pack_forget()

        # more buttons
        self.open_folder_button = tk.Button(left_frame, text="Open Saved Folder", command=self.open_saved_folder, state=tk.DISABLED)
        self.open_folder_button.pack(pady=5)
        tk.Button(left_frame, text="Open Database Folder", command=self.open_db_folder).pack(pady=5)
        tk.Button(left_frame, text="Clear URLs", command=self.clear_urls).pack(pady=5)

        # Book view box
        tk.Label(right_frame, text="Book Viewer", font=("Arial", 13, "bold"), bg="#ffffff").pack(pady=(10, 0))
        self.viewer_text = tk.Text(right_frame, wrap=tk.WORD)
        self.viewer_text.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
        self.viewer_text.config(state=tk.DISABLED)

    def clear_urls(self):
        """
        Clear input box
        """
        self.url_text.delete("1.0", tk.END)

    def open_db_folder(self):
        """
        Open folder containing db file.
        """
        db_path = os.path.abspath(StorageManager.DB_PATH)
        if os.path.exists(db_path):
            subprocess.Popen(f'explorer "{os.path.dirname(db_path)}"')
        else:
            messagebox.showerror("Not Found", "Database file (books.db) not found.")

    def open_saved_folder(self):
        """
        Open directory where books were saved
        """
        if self.last_saved_folder and os.path.isdir(self.last_saved_folder):
            subprocess.Popen(f'explorer "{self.last_saved_folder}"')
        else:
            messagebox.showerror("Error", "No saved folder found yet.")

    def sanitize_filename(self, name):
        """
        Converts title into safe filename.
        """
        return re.sub(r'[^a-zA-Z0-9_\-]', '_', name)[:50]

    def load_books(self):
        """
        Load/display books stored in db to the view box
        """
        self.book_listbox.delete(0, tk.END)
        try:
            self.books = sorted(StorageManager.get_all_books(), key=lambda b: b[1].lower())
            for book in self.books:
                self.book_listbox.insert(tk.END, f"{book[0]}: {book[1]}")
            self.book_count_label.config(text=f"Total Books: {len(self.books)}")
        except Exception as e:
            messagebox.showerror("Database Error", f"Could not load books:\n{str(e)}")

    def delete_selected_book(self):
        """
        Delete selected book from db and files
        """
        selections = self.book_listbox.curselection()
        if not selections:
            messagebox.showwarning("No selection", "Please select book(s) to delete.")
            return

        deleted_titles = []
        for index in reversed(selections):
            book_id = self.books[index][0]
            book = StorageManager.get_book_by_id(book_id)

            if book:
                _, title, _, filepath = book
                # Attempt to remove associated file if it exists
                if filepath and os.path.exists(filepath):
                    try:
                        os.remove(filepath)
                    except Exception as e:
                        print(f"Warning: Could not delete file {filepath}: {e}")

                StorageManager.delete_book(book_id)
                deleted_titles.append(title)

        self.load_books()

        if deleted_titles:
            messagebox.showinfo("Deleted", f"Deleted books:\n" + "\n".join(deleted_titles))

    def view_selected_book(self):
        """
        Load/display content of selected book in the view box
        """
        selection = self.book_listbox.curselection()
        if not selection:
            messagebox.showwarning("No selection", "Please select a book to view.")
            return

        index = selection[0]
        book_id = self.books[index][0]

        book = StorageManager.get_book_by_id(book_id)
        if book:
            _, title, content, _ = book
            self.viewer_text.config(state=tk.NORMAL)
            self.viewer_text.delete("1.0", tk.END)
            self.viewer_text.insert(tk.END, f"--- {title} ---\n\n{content}")
            self.viewer_text.config(state=tk.DISABLED)
        else:
            messagebox.showerror("Error", "Could not load book content.")

    def download(self):
        """
        Downloads books from URLs entered by user, saves in a chosen spot,
        and optionally stores metadata in the database.
        """
        urls_raw = self.url_text.get("1.0", tk.END).strip()
        fmt = self.format_var.get()

        if not urls_raw:
            messagebox.showerror("Error", "Please enter at least one URL.")
            return

        # Clean and split URLs
        urls = [u.strip() for u in urls_raw.splitlines() if u.strip()]
        total = len(urls)
        if total == 0:
            messagebox.showerror("Error", "No valid URLs found.")
            return

        output_dir = ""
        if fmt in ["pdf", "csv"]:
            output_dir = filedialog.askdirectory(title="Choose folder to save files")
            if not output_dir:
                return
            self.last_saved_folder = output_dir
            self.open_folder_button.config(state=tk.NORMAL)

        # Setup progress bar
        self.progress["maximum"] = total
        self.progress["value"] = 0
        self.progress.pack()
        self.root.update()

        success_count = 0
        errors = []

        for i, url in enumerate(urls):
            try:
                scraper = HTMLBookScraper(url)
                title, content = scraper.fetch()
                base_filename = self.sanitize_filename(title or f"book_{i+1}")
                full_path = os.path.join(output_dir, f"{base_filename}.{fmt}")

                # Output handling
                if fmt == "pdf":
                    StorageManager.to_pdf(title, content, full_path)
                elif fmt == "csv":
                    StorageManager.to_csv(title, content, full_path)

                # Save metadata
                if fmt in ["pdf", "csv"]:
                    StorageManager.save_metadata_to_db(title, content, full_path)
                elif fmt == "db":
                    StorageManager.save_metadata_to_db(title, content, None)

                success_count += 1

            except Exception as e:
                errors.append(f"{url} -> {str(e)}")

            self.progress["value"] = i + 1
            self.root.update_idletasks()
            time.sleep(0.1)

        self.progress.pack_forget()

        # Display success/failure message box
        summary = f" Success: {success_count}\n Failed: {len(errors)}"
        if errors:
            summary += "\n\nSample Errors:\n" + "\n".join(errors[:3])
        messagebox.showinfo("Download Summary", summary)