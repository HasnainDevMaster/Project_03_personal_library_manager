# Personal Library Manager

A simple command-line application to help you manage your personal book library.  
Easily add, remove, search, update, and track your books, with a user-friendly interface powered by Rich for beautiful terminal output.

---

## Features

- **Add Books:** Enter details like title, author, year, genre, and read status.
- **Remove Books:** Delete books by title.
- **Search:** Find books by title or author.
- **Display All Books:** View your library in a formatted table.
- **Statistics:** See total books and percentage read.
- **Update Books:** Edit book details.
- **Sort:** Sort your library by title or year.
- **Mark as Read/Unread:** Update the read status of any book.
- **Persistent Storage:** Your library is saved to `library.txt` in JSON format.

---

## Requirements

- Python 3.7+
- [Rich](https://pypi.org/project/rich/)

Install dependencies with:

```
pip install -r requirements.txt
```

---

## Usage

1. **Clone or Download** this repository.
2. **Install dependencies** (see above).
3. **Run the application:**

   ```
   python library_manager.py
   ```

4. **Follow the on-screen menu** to manage your library.

---

## File Structure

```
.
├── library_manager.py   # Main application script
├── library.txt          # Your saved library (auto-created)
├── requirements.txt     # Python dependencies
└── readme.md            # This file
```

---

## Example

```
Welcome to your Personal Library Manager!
1. Add a book
2. Remove a book
3. Search for a book
4. Display all books
5. Display statistics
6. Update a book
7. Sort books
8. Mark book as Read/Unread
9. Exit
```

---

## Notes

- The library is saved automatically when you exit.
- If `library.txt` does not exist, sample books are added on first run.
- All data is stored locally.

---
