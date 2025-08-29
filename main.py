import pandas as pd
import tkinter as tk
from tkinter import filedialog


def main():
    print("Bitte wählen Sie eine Excel- oder CSV-Datei aus.")
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Datei auswählen",
        filetypes=[("Excel/CSV Files", "*.xlsx *.xls *.csv")]
    )
    if not file_path:
        return

    if file_path.lower().endswith(('.xlsx', '.xls')):
        df = pd.read_excel(file_path)
    elif file_path.lower().endswith('.csv'):
        df = pd.read_csv(file_path, sep=';')
    else:
        return

    print(f"Gefundene Zeilen: {df.shape[0]}")
    print(f"Gefundene Spalten: {df.shape[1]}")

    # ...keine weitere Aktion...


if __name__ == "__main__":
    main()
