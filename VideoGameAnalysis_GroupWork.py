import tkinter as tk
from tkinter import StringVar, OptionMenu, Label, Button
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd

# Load dataset
df = pd.read_csv("VideoGames_DataAnalysis - Sheet1.csv")
df.columns = df.columns.str.strip().str.replace('\xa0', '')
df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")

# GUI setup
root = tk.Tk()
root.title("Game Performance Dashboard")
root.configure(bg="#f4f4f4")
root.geometry("1200x800")

# Dropdown setup
selected_game = StringVar(value=df["Game"].unique()[0])

Label(root, text="🎮 Select Game:", font=("Helvetica", 14),
      bg="#f4f4f4", fg="#1f2a44").pack(pady=(20, 5))

OptionMenu(root, selected_game, *df["Game"].unique()).pack()

# Game info labels
revenue_label = Label(root, text="", font=("Helvetica", 13, "bold"), bg="#f4f4f4", fg="#333333")
revenue_label.pack(pady=(10, 0))

maintenance_label = Label(root, text="", font=("Helvetica", 13, "bold"), bg="#f4f4f4", fg="#333333")
maintenance_label.pack()

def show_game_details():
    game = selected_game.get()
    latest = df[df["Game"] == game].sort_values("Date").iloc[-1]
    revenue_label.config(text=f"Revenue: ${latest['Revenue']:.2f} M")
    maintenance_label.config(text=f"Maintenance Cost: ${latest['Maintenance Cost']:.2f} M")

Button(root, text="📊 View Game Data", font=("Helvetica", 11), bg="#4a6fa5", fg="white",
       command=show_game_details).pack(pady=(10, 20))

# KPI charts
def plot_kpis():
    fig = Figure(figsize=(16, 5), dpi=100)
    kpi_map = {
        "Monthly Active Users (MAU by millions)": "Monthly Active Users (Millions)",
        "Session Length (min)": "Session Length (Minutes)",
        "User Acquisition Rate (%)": "User Acquisition Rate (%)"
    }

    for i, (col, ylabel) in enumerate(kpi_map.items(), start=1):
        ax = fig.add_subplot(1, 3, i)
        for game in df["Game"].unique():
            data = df[df["Game"] == game]
            ax.plot(data["Date"], data[col], label=game, marker="o", linewidth=2)
        ax.set_title(f"{ylabel} Over Time", fontsize=11, color="#1f2a44")
        ax.set_xlabel("Date", color="#333333")
        ax.set_ylabel(ylabel, color="#333333")
        ax.tick_params(axis="x", rotation=45, colors="#333333")
        ax.tick_params(axis="y", colors="#333333")
        ax.grid(True, linestyle="--", alpha=0.3)
        if i == 3:
            ax.legend(loc="upper left", fontsize=8)

    FigureCanvasTkAgg(fig, master=root).get_tk_widget().pack(pady=(10, 40))

plot_kpis()
root.mainloop()