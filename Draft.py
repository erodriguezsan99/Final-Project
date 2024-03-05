"""
Author: Edgar Rodriguez Sanchez
Name: Results tracker
LastModified: 03/05/2024

This is a GUI soccer program that is used to track game results of my top 4 watched teams.

"""

import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

""""""
class MainWindow:
    
    """"""
    def __init__(self, root):
        self.root = root
        root.geometry("600x600")
        root.title("Soccer Results Tracker")
        root.iconbitmap("soccerIcon.ico")
        
        # Create buttons for each team
        self.team_name = ["FC Bayern Munich", "FC Barcelona", "Liverpool FC", "Juventus FC"]
        self.buttons = []
        for team in self.team_name:
            team_button = tk.Button(root, width=45, height=8, text=team, command=lambda t=team: self.open_team_window(t))
            team_button.pack(pady=10)
            self.buttons.append(team_button)

    """"""
    def open_team_window(self, team_name):
        self.team_name = team_name
        team_window = TeamWindow(self.root, team_name)

""""""
class TeamWindow(MainWindow):
    
    """"""
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

        master = tk.Toplevel(master)
        master.geometry("350x350")
        master.title(f"{team_name} Details")
        master.iconbitmap("soccerIcon.ico")
        

        # Display team information
        for key, value in team_info[team_name].items():
            tk.Label(master, text=f"{key}: {value}").pack(pady=2)


        # Label and Entry for Game Date
        self.game_date_label = tk.Label(master, text="Game Date:")
        self.game_date_label.pack()
        self.game_date_entry = tk.Entry(master)
        self.game_date_entry.pack()

        # Label and Entry for Opponent Name
        self.opponent_name_label = tk.Label(master, text="Opponent's Name:")
        self.opponent_name_label.pack()
        self.opponent_name_entry = tk.Entry(master)
        self.opponent_name_entry.pack()

        # Label and Entry for Team Score
        self.team_score_label = tk.Label(master, text=f"{team_name} Score:")
        self.team_score_label.pack()
        self.team_score_entry = tk.Entry(master)
        self.team_score_entry.pack()

        # Label and Entry for Opponent Score
        self.opponent_score_label = tk.Label(master, text=" Score:")
        self.opponent_score_label.pack()
        self.opponent_score_entry = tk.Entry(master)
        self.opponent_score_entry.pack()
        
        # Button to save Data
        self.save_button = tk.Button(master, text="Save Data", command=self.save_data)
        self.save_button.pack(pady=15)

        """"""
    def save_data(self):
        game_date = self.game_date_entry.get()
        opponent_name = self.opponent_name_entry.get()
        team_score = self.team_score_entry.get()
        opponent_score = self.opponent_score_entry.get()

        if not team_score.isdigit() or not opponent_score.isdigit():
            messagebox.showerror("Error", "Unable to save: Invalid Entries, try again")
        else:
            # Save data to a text file or perform other actions
            with open("soccer_results.txt", "a") as file:
                file.write(f"{self.team_name} vs. {opponent_name}: {team_score}-{opponent_score}, Date: {game_date}\n")
            messagebox.showinfo("Success", "Data saved successfully!")

""""""
def main():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

#
if __name__ == "__main__":
    main()


