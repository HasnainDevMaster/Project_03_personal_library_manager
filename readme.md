# 📚 Personal Library Manager

A powerful yet simple **command-line tool** that helps you organize, track, and manage your personal book collection.  
Whether you're a passionate reader or just starting to build your bookshelf, this app provides everything you need — from adding and updating books to searching, sorting, and saving your reading progress effortlessly.

---

## ✨ Highlights & Key Features

- ➕ **Add Books** — Enter title, author, year, genre, and read status  
- 🗑 **Remove Books** — Delete books by title  
- 🔍 **Search** — Quickly find books by title or author  
- 📋 **View All Books** — Display your library in a neat table view  
- 📊 **Statistics Dashboard** — View total count, read percentage, and more  
- ✏ **Update & Edit** — Modify existing book details anytime  
- 🔠 **Sort Options** — Sort by title or publication year  
- ✅ **Mark Read / Unread** — Track your reading progress  
- 💾 **Persistent Storage** — Automatically saves your collection to `library.txt`  

---

## 📂 Project Structure

```

.
├── library_manager.py    # Main CLI application
├── library.txt           # Data file (JSON format, auto-created)
├── requirements.txt      # Required dependencies
└── README.md             # Project overview & usage guide

````

---

## 🛠 Requirements & Setup

**Requirements:**  
- Python 3.7 or higher  
- [Rich](https://pypi.org/project/rich) — for beautifully formatted terminal output  

**Setup:**

```bash
git clone https://github.com/HasnainDevMaster/Project_03_personal_library_manager.git
cd Project_03_personal_library_manager
pip install -r requirements.txt
````

---

## 🚀 Usage Guide

Run the program with:

```bash
python library_manager.py
```

You’ll be greeted with an interactive menu:

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

All changes are automatically saved when you exit.

---

## 🧠 How It Works

* On first run, the program creates a `library.txt` file with sample data.
* Your library data is stored locally in JSON format.
* The app uses `Rich` for colorful tables, progress bars, and improved CLI experience.
* Exiting the program automatically saves any updates you’ve made.

---


## 🤝 Contributing

Contributions are welcome!
If you have ideas for new features or improvements, feel free to open an issue or submit a pull request.

---


## 📝 Summary

The **Personal Library Manager** simplifies how you organize and track your reading list.
It’s fast, easy to use, and fully customizable — a perfect tool for anyone who loves reading and wants their library neatly managed right from the terminal. 📖✨
