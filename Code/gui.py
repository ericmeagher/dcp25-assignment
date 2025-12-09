import tkinter as tk

from database import load_tunes_dataframe, search_tunes_by_title


def run_gui():
    # load all tunes once when GUI starts
    full_df = load_tunes_dataframe()

    root = tk.Tk()
    root.title("ABC Tunes Browser")
    root.geometry("500x400")

    # title search label + entry
    tk.Label(root, text="Title contains:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    title_var = tk.StringVar()
    title_entry = tk.Entry(root, textvariable=title_var, width=40)
    title_entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")

    # listbox to show results
    listbox = tk.Listbox(root, width=80, height=20)
    listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    # status label
    status_var = tk.StringVar()
    status_label = tk.Label(root, textvariable=status_var, anchor="w")
    status_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    # function to run search
    def do_search():
        term = title_var.get().strip()
        if term:
            df = search_tunes_by_title(full_df, term)
        else:
            df = full_df

        listbox.delete(0, tk.END)

        if df.empty:
            status_var.set("No tunes found.")
            return

        for index, row in df.iterrows():
            line = f"{row['book_number']} | {row['x']} | {row['title']}"
            listbox.insert(tk.END, line)

        status_var.set(f"{len(df)} tune(s) shown.")

    # search button
    tk.Button(root, text="Search", command=do_search).grid(
        row=0, column=2, padx=5, pady=5, sticky="we"
    )
    
    # window formatting
    root.columnconfigure(1, weight=1)
    root.rowconfigure(1, weight=1)
    
    # show all tunes at the start
    do_search()

    root.mainloop()
