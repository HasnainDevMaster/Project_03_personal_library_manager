import os
from rich.console import Console
from rich.table import Table
from rich import print

# -----------------------------
# Personal Library Manager
# -----------------------------

import json

library = []
filename = "library.txt"
console = Console()

# Load library from file if exists
if os.path.exists(filename):
    with open(filename, "r") as f:
        try:
            library = json.load(f)
        except json.JSONDecodeError:
            library = []

# Add sample books if library is empty
if not library:
    sample_books = [
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960, "genre": "Fiction", "read": True},
        {"title": "1984", "author": "George Orwell", "year": 1949, "genre": "Dystopian", "read": False},
        {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813, "genre": "Romance", "read": True},
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925, "genre": "Fiction", "read": True},
        {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951, "genre": "Fiction", "read": False},
        {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932, "genre": "Science Fiction", "read": True},
        {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937, "genre": "Fantasy", "read": True},
        {"title": "War and Peace", "author": "Leo Tolstoy", "year": 1869, "genre": "Historical", "read": False},
        {"title": "The Book Thief", "author": "Markus Zusak", "year": 2005, "genre": "Historical Fiction", "read": True}
    ]
    library.extend(sample_books)
    with open(filename, "w") as f:
        json.dump(library, f, indent=4)

# --- Helper Functions ---
def save_library():
    with open(filename, "w") as f:
        json.dump(library, f, indent=4)

def format_book(book):
    status = "✅ Read" if book["read"] else "❌ Unread"
    return f'{book["title"]} by {book["author"]} ({book["year"]}) - {book["genre"]} - {status}'

def add_book():
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    try:
        year = int(input("Enter the publication year: "))
    except ValueError:
        print("[red]Invalid year. Please enter a number.[/red]")
        return
    genre = input("Enter the genre: ").strip()
    read = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

    library.append({
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    })
    print("[green]Book added successfully![/green]\n")

def remove_book():
    title = input("Enter the title of the book to remove: ").strip()
    global library
    updated = [book for book in library if book["title"].lower() != title.lower()]
    if len(updated) != len(library):
        library = updated
        print("[green]Book removed successfully![/green]\n")
    else:
        print("[red]Book not found.[/red]\n")

def search_book():
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ").strip()
    keyword = input("Enter search keyword: ").strip().lower()
    matches = []

    if choice == "1":
        matches = [book for book in library if keyword in book["title"].lower()]
    elif choice == "2":
        matches = [book for book in library if keyword in book["author"].lower()]
    else:
        print("[red]Invalid choice.[/red]")
        return

    if matches:
        table = Table(title="Matching Books")
        table.add_column("#", justify="center")
        table.add_column("Title")
        table.add_column("Author")
        table.add_column("Year")
        table.add_column("Genre")
        table.add_column("Status")

        for i, book in enumerate(matches, start=1):
            status = "✅ Read" if book["read"] else "❌ Unread"
            table.add_row(str(i), book["title"], book["author"], str(book["year"]), book["genre"], status)

        console.print(table)
    else:
        print("[yellow]No matching books found.[/yellow]")
    print()

def display_books():
    if not library:
        print("[yellow]Your library is empty.[/yellow]\n")
        return

    table = Table(title="Your Library")
    table.add_column("#", justify="center")
    table.add_column("Title")
    table.add_column("Author")
    table.add_column("Year")
    table.add_column("Genre")
    table.add_column("Status")

    for i, book in enumerate(library, start=1):
        status = "✅ Read" if book["read"] else "❌ Unread"
        table.add_row(str(i), book["title"], book["author"], str(book["year"]), book["genre"], status)

    console.print(table)
    print()

def display_statistics():
    total = len(library)
    read_books = sum(1 for book in library if book["read"])
    percentage = (read_books / total * 100) if total else 0

    print(f"[bold cyan]Total books:[/bold cyan] {total}")
    print(f"[bold cyan]Percentage read:[/bold cyan] {percentage:.1f}%\n")

def update_book():
    title = input("Enter the title of the book to update: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            print("Leave field blank to keep current value.")
            new_title = input(f"New title [{book['title']}]: ").strip()
            new_author = input(f"New author [{book['author']}]: ").strip()
            new_year = input(f"New year [{book['year']}]: ").strip()
            new_genre = input(f"New genre [{book['genre']}]: ").strip()
            new_read = input(f"Have you read it? (yes/no) [{ 'yes' if book['read'] else 'no' }]: ").strip().lower()

            if new_title: book['title'] = new_title
            if new_author: book['author'] = new_author
            if new_year.isdigit(): book['year'] = int(new_year)
            if new_genre: book['genre'] = new_genre
            if new_read in ['yes', 'no']: book['read'] = (new_read == 'yes')

            print("[green]Book updated successfully![/green]\n")
            return
    print("[red]Book not found.[/red]\n")

def sort_books():
    print("Sort by:\n1. Title\n2. Year")
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        library.sort(key=lambda x: x["title"].lower())
        print("[green]Books sorted by title.[/green]\n")
    elif choice == "2":
        library.sort(key=lambda x: x["year"])
        print("[green]Books sorted by year.[/green]\n")
    else:
        print("[red]Invalid choice.[/red]\n")

def update_read_status(book, status):
    if status == "read":
        book['read'] = True
        print("[green]Book marked as read.[/green]\n")
    elif status == "unread":
        book['read'] = False
        print("[green]Book marked as unread.[/green]\n")
    else:
        print("[red]Invalid choice. Please type 'read' or 'unread'.[/red]\n")

def mark_as_read_unread():
    title = input("Enter the title of the book: ").strip()
    for book in library:
        if book['title'].lower() == title.lower():
            status = input("Do you want to mark it as read or unread? (read/unread): ").strip().lower()
            update_read_status(book, status)
            return
    print("[red]Book not found.[/red]\n")

# --- Main Loop ---
while True:
    print("""
[bold blue]Welcome to your Personal Library Manager![/bold blue]  
1. Add a book  
2. Remove a book  
3. Search for a book  
4. Display all books  
5. Display statistics  
6. Update a book  
7. Sort books  
8. Mark book as Read/Unread  
9. Exit  
""")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_book()
    elif choice == "2":
        remove_book()
    elif choice == "3":
        search_book()
    elif choice == "4":
        display_books()
    elif choice == "5":
        display_statistics()
    elif choice == "6":
        update_book()
    elif choice == "7":
        sort_books()
    elif choice == "8":
        mark_as_read_unread()
    elif choice == "9":
        confirm = input("Are you sure you want to exit? (yes/no): ").strip().lower()
        if confirm == "yes":
            save_library()
            print("[bold green]Library saved to file. Goodbye![/bold green]")
            break
        else:
            print("[yellow]Exit canceled.[/yellow]\n")
    else:
        print("[red]Invalid choice. Please try again.[/red]\n")
