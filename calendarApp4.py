import tkinter as tk
import calendar
from datetime import datetime


class CalendarApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calendar App")

        # Create a calendar widget
        self.cal = calendar.Calendar()

        # Create a label for the month and year
        self.label = tk.Label(self.master, font=("Arial", 14))
        self.label.pack()

        # Create a frame to hold the calendar
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        # Create buttons to switch between months
        self.prev_button = tk.Button(self.master, text="<", command=self.prev_month)
        self.prev_button.pack(side=tk.LEFT)
        self.next_button = tk.Button(self.master, text=">", command=self.next_month)
        self.next_button.pack(side=tk.RIGHT)

        # Create a grid to display the days of the week
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for i, day in enumerate(days):
            label = tk.Label(self.frame, text=day, font=("Arial", 12))
            label.grid(row=0, column=i, padx=10, pady=10)

        # Display the current month
        now = datetime.now()
        self.current_month = calendar.month_name[now.month]
        self.current_year = now.year
        self.update_calendar()

    def update_calendar(self):
        # Update the label with the current month and year
        self.label.config(text=f"{self.current_month} {self.current_year}")

        # Clear the existing calendar
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Get the calendar data for the current month
        month_data = self.cal.monthdatescalendar(self.current_year, list(calendar.month_name).index(self.current_month))

        # Display the calendar data in a grid
        for row, week in enumerate(month_data):
            for col, day in enumerate(week):
                if day.month != list(calendar.month_name).index(self.current_month):
                    label = tk.Label(self.frame, text="", font=("Arial", 12))
                else:
                    label = tk.Label(self.frame, text=day.day, font=("Arial", 12))

                label.grid(row=row + 1, column=col, padx=10, pady=10)

    def prev_month(self):
        # Decrement the month and year
        prev_month_index = list(calendar.month_name).index(self.current_month) - 1
        if prev_month_index == 0:
            self.current_month = "December"
            self.current_year -= 1
        else:
            self.current_month = calendar.month_name[prev_month_index]

        # Update the calendar
        self.update_calendar()

    def next_month(self):
        # Increment the month and year
        next_month_index = list(calendar.month_name).index(self.current_month) + 1
        if next_month_index == 13:
            self.current_month = "January"
            self.current_year += 1
        else:
            self.current_month = calendar.month_name[next_month_index]

        # Update the calendar
        self.update_calendar()


root = tk.Tk()
app = CalendarApp(root)
root.mainloop()
