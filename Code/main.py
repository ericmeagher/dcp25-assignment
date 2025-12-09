from database import (
    load_tunes_dataframe,
    get_tunes_by_book,
    get_tunes_by_type,
    search_tunes_by_title,
)
from gui import run_gui   # Tkinter GUI

def print_tunes_summary(df, limit=20):
    """Print a small table of tunes to the terminal"""
    if df.empty:
        print("No tunes found.")
        return
    cols = ["id", "book_number", "x", "title", "rtype", "key"]
    print(df[cols].head(limit))


def menu():
    """Text menu that lets me choose what to do."""
    while True:
        print("\n=== ABC Tunes Menu ===")
        print("1. List first 20 tunes")
        print("2. Search tunes by title")
        print("3. Get tunes by book number")
        print("4. Get tunes by type")
        print("5. Start GUI")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        # 1 – list first 20 tunes
        if choice == "1":
            df = load_tunes_dataframe()
            print_tunes_summary(df, limit=20)

        # 2 – search by title
        elif choice == "2":
            term = input("Title search term: ").strip()
            df = load_tunes_dataframe()
            result = search_tunes_by_title(df, term)
            print_tunes_summary(result)

        # 3 – get tunes by book number
        elif choice == "3":
            book_text = input("Book number: ").strip()
            if not book_text.isdigit():
                print("Invalid book number.")
                continue
            book = int(book_text)
            df = load_tunes_dataframe()
            result = get_tunes_by_book(df, book)
            print_tunes_summary(result)

        # 4 – get tunes by type
        elif choice == "4":
            ttype = input("Tune type (e.g. reel, jig): ").strip()
            df = load_tunes_dataframe()
            result = get_tunes_by_type(df, ttype)
            print_tunes_summary(result)

        # 5 – start the GUI window
        elif choice == "5":
            print("Launching GUI...")
            run_gui()

        # 0 – exit the program
        elif choice == "0":
            print("Goodbye.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    menu()

                print(f"  Found abc file: {file}")
                process_file(file_path)
                
