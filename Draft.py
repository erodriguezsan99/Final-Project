"""
Author: Edgar Rodriguez Sanchez
Name: Results tracker
LastModified: 02/29/2024

This is a GUI soccer program that is used to track game results of my top 4 watched teams.
It will allow the user to input the game results for any of the 4 teams, then append that data into a text file.
"""
import tkinter as tk
from tkinter import messagebox

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x600")
        self.root.title("Results Tracker")

        # Create buttons for each team
        self.teams = ["FC Bayern Munich", "FC Barcelona", "Liverpool FC", "Juventus FC"]
        self.buttons = []
        for team in self.teams:
            teamButton = tk.Button(root, text=team, width=30, height=8, command=lambda t=team: self.open_team_window(t))
            teamButton.pack(pady=10)
            self.buttons.append(teamButton)

    def open_team_window(self, team_name):
        team_window = TeamWindow(self.root, team_name)



class TeamWindow:
    def __init__(self, master, team_name):
        self.master = master
        self.team_name = team_name

        # Team information (year founded, league titles, current record)
        team_info = {
            "FC Bayern Munich": {"Year Founded": 1900, "League Titles": 30, "Current Record": "W-D-L: 20-5-3"},
            "FC Barcelona": {"Year Founded": 1899, "League Titles": 26, "Current Record": "W-D-L: 18-7-3"},
            "Liverpool FC": {"Year Founded": 1892, "League Titles": 19, "Current Record": "W-D-L: 16-8-4"},
            "Juventus FC": {"Year Founded": 1897, "League Titles": 36, "Current Record": "W-D-L: 22-4-4"}
        }

        self.team_window = tk.Toplevel(master)
        self.team_window.geometry("250x250")
        self.team_window.title(f"{team_name} Details")

        # Display team information
        for key, value in team_info[team_name].items():
            tk.Label(self.team_window, text=f"{key}: {value}").pack(pady=2)

def main():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
