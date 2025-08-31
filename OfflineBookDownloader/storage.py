import csv
import sqlite3
import html
import os
from fpdf import FPDF

"""
* Name         : book downloader final assignment
* Author       : Matthew Stevens
* Created      : Creation Date 7-2025
* Course       : CIS189
* IDE          : Visual Studio Code
* Description  : The purpose of this program is... The input is... The output is...
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""
class StorageManager:
    """ storage functions like database interaction, 
    PDF/CSV file output, data retrieval/deletion   
    """

    DB_PATH = os.path.join(os.path.dirname(__file__), "books.db")

    @staticmethod
    def initialize_db():
        """
        Initializes d.b. and creates table 
        """
        try:
            conn = sqlite3.connect(StorageManager.DB_PATH)
            c = conn.cursor()

            # Create table 
            c.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    content TEXT NOT NULL
                )
            """)

            #adding the filepath column 
            try:
                c.execute("ALTER TABLE books ADD COLUMN filepath TEXT")
            except sqlite3.OperationalError:
                pass  # Column exists

            conn.commit()
        finally:
            conn.close()

    @staticmethod
    def get_book_by_id(book_id):
        """
        Retrieves book by ID

        Args:
            book_id (int):ID of book to retrieve.

        Returns:
            id, title, content, 
        """
        conn = sqlite3.connect(StorageManager.DB_PATH)
        c = conn.cursor()
        c.execute("SELECT id, title, content, filepath FROM books WHERE id = ?", (book_id,))
        result = c.fetchone()
        conn.close()
        return result

    @staticmethod
    def save_metadata_to_db(title, content, filepath):
        """
        Saves book metadata to DB.

        Args:
            title (str) title of the book.
            content (str) book's content.
            filepath (str) to the saved file (PDF/CSV/DB).
        """
        conn = sqlite3.connect(StorageManager.DB_PATH)
        c = conn.cursor()
        c.execute("INSERT INTO books (title, content, filepath) VALUES (?, ?, ?)",
                  (title, content, filepath))
        conn.commit()
        conn.close()

    @staticmethod
    def to_db(title, content):
        """
        Stores book in database/no file output.

        Args:
            title (str) Book title.
            content (str) Book content.
        """
        filepath = f"db://{title}"  # Symbolic placeholder path
        StorageManager.save_metadata_to_db(title, content, filepath)

    @staticmethod
    def get_all_books():
        """
        Retrieves books in database.

        Returns:
             A list containing (id, title, filepath) for each book.
        """
        conn = sqlite3.connect(StorageManager.DB_PATH)
        c = conn.cursor()
        c.execute("SELECT id, title, filepath FROM books")
        books = c.fetchall()
        conn.close()
        return books

    @staticmethod
    def delete_book(book_id):
        """
        Deletes book from database by ID.

        Args:
            ID of book to delete.
        """
        conn = sqlite3.connect(StorageManager.DB_PATH)
        c = conn.cursor()
        c.execute("DELETE FROM books WHERE id = ?", (book_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def to_pdf(title, content, filename):
        """
        Converts book content to PDF file.

        Args:
            title (str) title of the book.
            content (str) content of the book.
            filename (str) output PDF filename.
        """
        class BookPDF(FPDF):
            def footer(self):
                self.set_y(-15)
                self.set_font("Arial", "I", 8)
                self.set_text_color(128)
                self.cell(0, 10, f"Page {self.page_no()}", align='C')

        def clean_text(text):
            """
            Replaces special Unicode characters with simpler ASCII equivalent characters.
            """
            replacements = {
                '\u201c': '"', '\u201d': '"',
                '\u2018': "'", '\u2019': "'",
                '\u2014': '-', '\u2013': '-',
                '\u2026': '...'
            }
            for bad, good in replacements.items():
                text = text.replace(bad, good)
            return text

        # Decode HTML entities and clean up text
        content = html.unescape(content)
        content = clean_text(content)

        # Ensure encoding is safe for PDF output
        safe_content = content.encode('latin-1', 'replace').decode('latin-1')

        pdf = BookPDF()
        pdf.add_page()

        # Add title to PDF
        pdf.set_font("Arial", size=14)
        pdf.cell(0, 10, title, ln=True, align='C')
        pdf.ln(10)

        # Add content to PDF
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, safe_content)

        # Save PDF to file
        pdf.output(filename)

    @staticmethod
    def to_csv(title, content, filename):
        """
        Saves book title and content to CSV file.

        Args:
            title (str) Book title.
            content (str) Book content.
            filename (str) Output CSV filename.
        """
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Content"])
            writer.writerow([title, content])


# Optional debug view when running this file directly
if __name__ == "__main__":
    print("DB Path:", os.path.abspath(StorageManager.DB_PATH))
    StorageManager.initialize_db()
    books = StorageManager.get_all_books()
    print("Books in DB:")
    for book in books:
        print(book)

