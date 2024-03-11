"""
Author: Edgar Rodriguez Sanchez
Name: Results tracker
LastModified: 03/10/2024

This is a GUI soccer program that is used to track game results of my top 4 watched teams.
The user picks a team button and can input game results. These results get saved to a text file.
All results saved after the first will be appended to the text file.

"""

# Extensions used for the program
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

# Main window class
class MainWindow:
    """
    The main application window.
    """


    def __init__(self, root):
        """
        Initialize the main window and create buttons for each team.
        """
        self.root = root
        root.geometry("600x600")
        root.state("zoomed")
        root.title("Soccer Results Tracker")
        root.iconbitmap("soccerIcon.ico")
        
        self.main_window_title = tk.Label(root, text="Results Tracker\nChoose a team:", font="bold")
        self.main_window_title.pack(pady=2)


        # List of team names
        self.team_name = ["FC Bayern Munich", "FC Barcelona", "Liverpool FC", "Juventus FC"]
        self.buttons = []


        # Create buttons for each team using a for loop
        for team in self.team_name:
            team_button = tk.Button(root, width=40, height=7, text=team, command=lambda t=team: self.open_team_window(t))
            team_button.pack(pady=10)
            self.buttons.append(team_button)


        # Button to exit the program
        self.exit_program_button = tk.Button(root, text="Exit Program", command=self.exit_program)
        self.exit_program_button.pack(pady=3)


    def exit_program(self):
        """
        Exit the program.
        """
        self.root.destroy()


    def open_team_window(self, team_name):
        """
        Open the team window for the selected team.
        """


        # Check if team window is already open
        if not hasattr(self, "team_windows"):
            self.team_windows = {}

        if team_name not in self.team_windows:
            self.team_windows[team_name] = TeamWindow(self.root, team_name)



class TeamWindow(MainWindow):
    """
    The team details window.
    """


    def __init__(self, master, team_name):
        """
        Initialize the team window with team details and entry fields.
        """
        self.master = master
        self.team_name = team_name


        # Team information (year founded, league titles, current record)
        team_info = {
            "FC Bayern Munich": {"Year Founded": 1900, "League Titles": 30, "Current Record": "W-D-L: 20-5-3"},
            "FC Barcelona": {"Year Founded": 1899, "League Titles": 26, "Current Record": "W-D-L: 18-7-3"},
            "Liverpool FC": {"Year Founded": 1892, "League Titles": 19, "Current Record": "W-D-L: 16-8-4"},
            "Juventus FC": {"Year Founded": 1897, "League Titles": 36, "Current Record": "W-D-L: 22-4-4"}
        }
        # Details for the team windows
        master = tk.Toplevel(master)
        master.geometry("350x600")
        master.title(f"{team_name} Details")
        master.iconbitmap("soccerIcon.ico")
        
        # Team logos used for the team windows
        master.team_logo = ImageTk.PhotoImage(Image.open(f"{team_name}.png"))
        master.window_logo = tk.Label(master, image=master.team_logo)
        master.window_logo.pack()


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
        self.opponent_score_label = tk.Label(master, text="Opponent's Score:")
        self.opponent_score_label.pack()
        self.opponent_score_entry = tk.Entry(master)
        self.opponent_score_entry.pack()
        

        # Button to save Data
        self.save_button = tk.Button(master, text="Save Data", command=self.save_data)
        self.save_button.pack(pady=15)


        # Button to close the team window
        self.close_button = tk.Button(master, text="Close", command=master.destroy)
        self.close_button.pack(pady=5)


    def save_data(self):
        """
        Save the entered game data.
        """
        game_date = self.game_date_entry.get()
        opponent_name = self.opponent_name_entry.get()
        team_score = self.team_score_entry.get()
        opponent_score = self.opponent_score_entry.get()


        # Error handling for game data
        if not team_score.isdigit() or not opponent_score.isdigit():
            messagebox.showerror("Error", "Unable to save: Invalid Entries, try again")
        else:
            # Save data to a text file or perform other actions
            with open("soccer_results.txt", "a") as file:
                file.write(f"{self.team_name} vs. {opponent_name}: {team_score}-{opponent_score}, Date: {game_date}\n")
            messagebox.showinfo("Success", "Data saved successfully!")


# Main function
def main():
    """
    Main function to run the application.
    """
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()


# Run the main function
if __name__ == "__main__":
    main()





