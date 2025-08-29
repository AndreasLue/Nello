import pandas as pd
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt


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
    print("Überschriften:", list(df.columns))

    if df.shape[1] >= 2:
        x_col = df.columns[0]
        y_col = df.columns[1]
        plt.figure()
        ax1 = plt.gca()
        ax1.plot(df[x_col], df[y_col], label=y_col, color='blue')
        ax1.set_xlabel(x_col)
        ax1.set_ylabel(y_col, color='blue')
        ax1.tick_params(axis='y', labelcolor='blue')

        # Überplotte mit der 7. Spalte, falls vorhanden
        if df.shape[1] >= 7:
            y2_col = df.columns[6]
            ax2 = ax1.twinx()
            ax2.plot(df[x_col], df[y2_col], label=y2_col, color='green')
            ax2.set_ylabel(y2_col, color='green')
            ax2.tick_params(axis='y', labelcolor='green')

        plt.title(f"{y_col} und ggf. {df.columns[6]} vs. {x_col}")
        plt.grid(True)
        plt.savefig("plot.png")
        plt.close()
        print("Plot gespeichert als plot.png.")

        # Zweite Grafik nur bis zur Zeit 3600
        df_bis_3600 = df[df[x_col] <= 3600]
        plt.figure()
        ax1 = plt.gca()
        ax1.plot(df_bis_3600[x_col], df_bis_3600[y_col], label=y_col, color='blue')
        ax1.set_xlabel(x_col)
        ax1.set_ylabel(y_col, color='blue')
        ax1.tick_params(axis='y', labelcolor='blue')

        if df.shape[1] >= 7:
            ax2 = ax1.twinx()
            ax2.plot(df_bis_3600[x_col], df_bis_3600[y2_col], label=y2_col, color='green')
            ax2.set_ylabel(y2_col, color='green')
            ax2.tick_params(axis='y', labelcolor='green')

        plt.title(f"{y_col} und ggf. {df.columns[6]} vs. {x_col} (bis 3600)")
        plt.grid(True)
        plt.savefig("plot_bis_3600.png")
        print("Plot gespeichert als plot_bis_3600.png.")

        # Interaktives Fenster mit Maus-Click-Event
        def onclick(event):
            if event.inaxes:
                print(f"Mausposition: x={event.xdata}, y={event.ydata}")
                plt.close(event.canvas.figure)  # Fenster schließen nach erstem Klick

        fig = plt.figure()
        ax1 = fig.gca()
        ax1.plot(df_bis_3600[x_col], df_bis_3600[y_col], label=y_col, color='blue')
        ax1.set_xlabel(x_col)
        ax1.set_ylabel(y_col, color='blue')
        ax1.tick_params(axis='y', labelcolor='blue')
        if df.shape[1] >= 7:
            ax2 = ax1.twinx()
            ax2.plot(df_bis_3600[x_col], df_bis_3600[y2_col], label=y2_col, color='green')
            ax2.set_ylabel(y2_col, color='green')
            ax2.tick_params(axis='y', labelcolor='green')
        plt.title(f"{y_col} und ggf. {df.columns[6]} vs. {x_col} (bis 3600)")
        plt.grid(True)
        fig.canvas.mpl_connect('button_press_event', onclick)
        plt.show()

    else:
        print("Nicht genügend Spalten zum Plotten.")

    # ...keine weitere Aktion...


if __name__ == "__main__":
    main()
