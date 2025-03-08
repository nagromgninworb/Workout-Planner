import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel, PhotoImage
import json
import os

# File to store data
DATA_FILE = "workout_data.json"

# Load existing data or create a new file if it does not exist
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as file:
        json.dump({"workout_plans": [], "workout_logs": []}, file)

# Read the data from the file, handling errors if the file is empty or corrupted
with open(DATA_FILE, "r") as file:
    try:
        data = json.load(file)
    except json.JSONDecodeError:
        data = {"workout_plans": [], "workout_logs": []}

# Function to save workout data to the JSON file
def save_data():
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Function to add a new workout plan
def add_workout_plan():
    plan = simpledialog.askstring("Workout Plan", "Enter your workout plan:")
    if plan and plan.strip():  # Ensure input is not empty
        data["workout_plans"].append(plan.strip())
        save_data()
        messagebox.showinfo("Success", "Workout plan saved successfully!")
    else:
        messagebox.showwarning("Input Error", "Please enter a valid workout plan.")

# Function to view saved workout plans
def view_workout_plans():
    plans = "\n".join(data["workout_plans"]) or "No workout plans saved."
    messagebox.showinfo("Workout Plans", plans)

# Function to log a workout session
def log_workout():
    log = simpledialog.askstring("Workout Log", "Enter details of your completed workout:")
    if log and log.strip():  # Ensure input is valid
        data["workout_logs"].append(log.strip())
        save_data()
        messagebox.showinfo("Success", "Workout log saved successfully!")
    else:
        messagebox.showwarning("Input Error", "Please enter valid workout details.")

# Function to view saved workout logs
def view_workout_logs():
    logs = "\n".join(data["workout_logs"]) or "No workouts logged yet."
    messagebox.showinfo("Workout Logs", logs)

# Function for the settings window (placeholder for future updates)
def open_settings():
    settings_window = Toplevel(root)
    settings_window.title("Settings")
    settings_window.geometry("300x200")

    tk.Label(settings_window, text="Settings", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(settings_window, text="Feature coming soon!").pack()

# Create main application window
root = tk.Tk()
root.title("Workout Planner")
root.geometry("400x400")

# Load images (NOT USING IMAGES, SO THESE WILL BE IGNORED)
try:
    img1 = PhotoImage(file="workout1.png")  
    img2 = PhotoImage(file="workout2.png")  
except:
    img1 = img2 = None  # Ignore images if they don’t exist

# Main Label
title_label = tk.Label(root, text="Workout Planner", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Additional Labels for guidance
tk.Label(root, text="Track your fitness journey easily!", font=("Arial", 10)).pack()
tk.Label(root, text="Use the buttons below to navigate.", font=("Arial", 10)).pack()

# Buttons for navigation
tk.Button(root, text="Add Workout Plan", command=add_workout_plan, width=20).pack(pady=5)
tk.Button(root, text="View Workout Plans", command=view_workout_plans, width=20).pack(pady=5)
tk.Button(root, text="Log Workout", command=log_workout, width=20).pack(pady=5)
tk.Button(root, text="View Workout Logs", command=view_workout_logs, width=20).pack(pady=5)
tk.Button(root, text="Settings", command=open_settings, width=20).pack(pady=5)

# Run the application
root.mainloop()

