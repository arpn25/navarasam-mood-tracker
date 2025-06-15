"""
Navarasam Mood Tracker
----------------------
This program is an interactive mood journal based on the Navarasas (nine emotions) from 
Bharatanatyam (An Indian Classical Dance Form).
Users can record their daily mood by selecting one of the nine rasas, 
optionally respond to a creative writing prompt with their own verses describing the emotion of the day,
and save their entries to a CSV file.

Features include:
- Learning about Navarasas and their meanings.
- Starting a journaling session with mood selection and creative prompts.
- Viewing monthly mood summaries with visual representation using Tkinter graphics.
- Viewing all journal entries filtered by a selected rasa.

The program uses standard libraries such as csv, datetime, random, os, calendar, and tkinter for visualization.

Author: Namita
Date: 2025-06-14
"""
# =================== Libraries imported ===================
from datetime import datetime,date
import csv
import random
import os
import calendar
import tkinter as tk

# =================== Dictionary ===================
# Dictionary defining the nine Navarasas with their meanings, associated colors, and creative prompts
rasa_dict = {1: {"rasa":"shringaram",
                 "meaning":"love",
                 "color":"pink",
                 "prompts":["a moment that felt full of love",
                            "longing or waiting",
                            "a scent or sound that reminds you of affection",
                            "if love were a season",
                            "love in silence"]},
             2:{"rasa":"hasyam",
                "meaning":"laughter/happiness",
                "color":"yellow",
                "prompts":["happiest moment today",
                           "how does nature giggle?",
                           "if happiness had a shape what would it be?",
                           "joy full mess",
                           "stages of laughter"]},
             3:{"rasa":"karunam",
                "meaning":"compassion/sadness",
                "color":"blue",
                "prompts":["a moment of empathy or sadness",
                           "sorrow through a windowpane",
                           "a metaphor for tears",
                           "if grief could speak, what does it whisper?",
                           "something that you miss"]},
             4:{"rasa":"raudram",
                "meaning":"anger",
                "color":"red",
                "prompts":["a moment of frustration",
                           "anger as fire",
                           "if rage was a storm what would thunder be?",
                           "steps of cooling down",
                           "if anger were a person",
                           "what would you say to it?"]},
             5:{"rasa":"veeram",
                "meaning":"heroism/courage",
                "color":"orange",
                "prompts":["a moment of bravery",
                           "a battlecry",
                           "a metaphor for your bravery today",
                           "heroism according to you",
                           "stomping on despite fear"]},
             6:{"rasa":"bhayanakam",
                "meaning":"fear",
                "color":"purple",
                "prompts":["a moment of fear",
                           "what do shadows say?",
                           "fear as a sound",
                           "lines about uncertainity",
                           "your perfect sanctuary"]},
             7:{"rasa":"bibhatsam",
                "meaning":"disgust",
                "color":"green",
                "prompts":["an unsettling moment",
                           "unwelcome news",
                           "when comfort fades away",
                           "taste of unease",
                           "whisper of disgust"]},
             8:{"rasa":"adbhutam",
                "meaning":"wonder",
                "color":"turquoise",
                "prompts":["a moment of amazement",
                           "wonder in nature",
                           "what makes you go 'wow'?",
                           "spark of magic in real life",
                           "wonder as a painting"]},
             9:{"rasa":"shantam",
                "meaning":"peace/tranquility",
                "color":"grey",
                "prompts":["a moment of peace",
                           "you as still water",
                           "sound of silence",
                           "your idea of tranquility",
                           "peace as a color"]}}


# =================== Functions defined ===================
def learn_more():
    """
    Display information about the nine Navarasas (nine emotions) from Indian classical dance Bharatanatyam.

    Prints an introduction to the Navarasas, their meanings, associated emojis, and traditional colors.
    Provides a reference link for further reading.
    Returns to main menu if user presses 'Enter'.
    """

    # Introduction to Navarasas in Indian classical dance
    print("\nABOUT NAVARASAM\n")
    print("In Indian classical dance forms like Bharatanatyam, 'Navarasam' refers to the nine fundamental emotions or 'rasas' that capture the full spectrum of human feelings.")
    print("Each rasa represents a specific emotional state, often expressed through facial expressions, gestures, and storytelling in dance.")
    
    # Listing the nine traditional rasas with emojis and meanings
    print("\nThe traditional nine rasas are:")
    print("1. 😍 Sringaram - Love / Romance")
    print("2. 😄 Hasyam - Joy / Laughter")
    print("3. 😢 Karunam - Compassion / Sadness")
    print("4. 😡 Raudram - Anger")
    print("5. 💪 Veeram - Courage / Heroism")
    print("6. 😨 Bhayanakam - Fear")
    print("7. 🤢 Bibhatsam - Disgust")
    print("8. 😲 Adbhutam - Wonder / Surprise")
    print("9. 😐 Shantam - Peace / Tranquility")

    # Additional notes about associated colors and further reading
    print("\nTraditionally, each rasa has an associated color.")
    print("This tracker follows a contemporary color code for better clarity and modern aesthetics.")
    print("To read more about the Navarasas in classical dance, you can visit:")
    print("https://bharatanatyamnataraja.wordpress.com/navarasam/")

    # Pause for user input before returning to the main menu
    input("\nPress Enter to return to the main menu.")


def start_journaling():
    """
    Guide the user to select a mood from the Navarasam list, optionally provide a creative prompt, 
    and record a user response along with the mood details in a CSV file.

    Steps:
    1. Display the list of moods (Navarasas) with their numbers, names, and meanings.
    2. Prompt the user to enter a mood number.
    3. If valid, display the selected mood details.
    4. Ask the user if they want a creative prompt related to that mood.
       - If yes, show a random prompt and allow the user to write a short verse (2-3 lines, max 100 chars).
       - Validate that the verse is not blank and within the character limit.
       - If no, record 'No prompt' and 'No verse today.'
    5. Save the mood, prompt, verse, and current date to "mood_tracking.csv".
    6. Confirm to the user that the entry has been recorded.
    """
    # Display mood legend with mood numbers, names, and meanings
    print("\nWhat mood stood out in your day today?:\n")
    for key,value in rasa_dict.items():
        print(f"    {key}.{value['rasa'].title()} - {value['meaning'].title()}")

    # Prompt user to select mood by number
    try:
        mood_today = int(input("\nEnter mood number: "))
        if mood_today not in rasa_dict:
            print("Invalid number. Please try again.")
            return
        
        # Retrieve and display mood details
        rasa = rasa_dict[mood_today]['rasa'].title()
        meaning = rasa_dict[mood_today]['meaning'].title()
        color = rasa_dict[mood_today]['color'].lower()
        print(f"Today's mood: {rasa} - {meaning}\n")

    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    # Ask if user wants a creative prompt for journaling
    prompt_choice = input("\nWould you like a creative prompt? (y/n): ").lower().strip()

    if prompt_choice == "y":
        # Select random prompt for the chosen mood
        prompt = random.choice(rasa_dict[mood_today]['prompts'])
        print(f"\nPrompt: {prompt.title()}\n")

        while True:
            # Loop to get valid user verse input
            user_verse = input("Write a short verse of 2-3 lines (100 char max) using the given prompt:\n").strip()

            if user_verse == "":
                print("Response cannot be blank")
                continue

            # Limit user verse to 100 characters
            if len(user_verse) > 100:
                print("Exceeding word limit. Please try again\n")
                continue                
            
            break

    elif prompt_choice == "n":
        prompt = "No prompt"
        user_verse = "No verse today."
    else:
        print("Invalid input. Please enter y/n.")
        return

    # Get today's date formatted as DD MMM YYYY
    current_date = date.today().strftime('%d %b %Y')

    # Define CSV file path and check if it exists
    file_path = "mood_tracking.csv"
    file_exists = os.path.exists(file_path)

    # Append new entry to CSV file, write headers if file is new
    with open("mood_tracking.csv","a",newline='',encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Date","Mood","Meaning","Color","Prompt","Verse"])
        writer.writerow([current_date,rasa,meaning,color,prompt,user_verse])

    # Confirm entry recording
    print("\nEntry recorded!")
    input("\nPress Enter to return to the main menu.")


def view_stats():
    """
    Display mood statistics for a user-specified month and year.

    Steps:
    - Checks if the mood tracking CSV file exists; if not, prompts user to add entries first.
    - Prompts the user to input a month (3-letter abbreviation) and year.
    - Reads and filters mood entries from the CSV file for the specified month and year.
    - Calculates the frequency of each mood recorded in that period.
    - Identifies and displays the most frequently expressed mood (rasa) and its meaning.
    - Uses Tkinter to create a graphical calendar view:
      - Each day of the month is represented by a colored circle corresponding to the mood recorded on that day.
      - Days without entries are shown as white circles.
    """

    # Check if the CSV file exists; if not, notify user and exit
    file_path = "mood_tracking.csv"
    if not os.path.exists(file_path):
        print("No data found. Please enter data into the journal first.")
        return
    
    # Prompt user for the month (3-letter abbreviation) and year to view stats
    try:
        user_month = input("Enter the month to view (E.g.: Apr): ").strip().title()
        user_year = int(input("Enter the year to view: ").strip())

        # Validate month input length
        if len(user_month) != 3:
            print("Please type only the first three alphabets of the month name.")
            return

    except ValueError:
        print("Invalid input")
        return

    # Read CSV entries, filter for the specified month and year
    entries = []
    with open("mood_tracking.csv","r",newline='',encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            entry_date = datetime.strptime(row['Date'], '%d %b %Y')
            if entry_date.strftime('%b') == user_month and entry_date.year == user_year:
                entries.append(row)

        # Convert month entered to integer and get number of days in that month
        month_num = datetime.strptime(user_month, "%b").month
        days_in_month = calendar.monthrange(user_year, month_num)[1]

    # If no entries found for the specified month inform user and exit
    if not entries:
        print("No entries found for the date")
        return
    
    # Aggregate entries by day and count frequency of each mood
    entries_by_day = {}
    mood_count = {}
    for entry in entries:
        entry_date = datetime.strptime(entry['Date'], '%d %b %Y')
        day = entry_date.day
        entries_by_day[day] = entry
        mood = entry['Mood']
        mood_count[mood] = mood_count.get(mood,0) + 1
 
    # Determine the most frequently recorded mood of the month
    most_recorded_mood = max(mood_count, key = mood_count.get)

    # Match meaning associated with the most common mood from rasa_dict
    meaning = None
    for info in rasa_dict.values():
        if info['rasa'].lower() == most_recorded_mood.lower():
            meaning = info['meaning'].title()
            break
    
    # Display summary of the most expressed rasa for the selected month and year
    print(f"\nYou most expressed rasa for {user_month} {user_year}: ")
    print(f"{most_recorded_mood}({meaning})")

    # Create canvas to display visualisation
    window = tk.Tk()
    window.title(f"\nThe rasas you expressed in {user_month} {user_year}")

    canvas_width = 500
    canvas_height = 700
    canvas = tk.Canvas(window, width=canvas_width, height=canvas_height)
    canvas.pack()

    # Add title text inside canvas, centered at the top
    canvas.create_text(
    canvas_width / 2, 
    20,
    text=f"The rasas you expressed in {user_month} {user_year}",
    font=("Helvetica", 16, "bold"),
    fill="black")

    # Add title text inside canvas, centered at the top
    canvas.create_text(
    canvas_width / 2, 
    50,
    text=f"Mood of the month: {most_recorded_mood} ({meaning}) ",
    font=("Helvetica", 12, "italic"),
    fill="black")   

    # Draw circles for the moods
    circle_radius = 20
    margin  = 15
    x_start, y_start = 65, 100
    max_per_row = 7

    # Draw a circle for each day of the month
    for day in range(1, days_in_month + 1):
        row = (day - 1) // max_per_row
        col = (day - 1) % max_per_row
        x = x_start + col * (2 * circle_radius + margin)
        y = y_start + row * (2 * circle_radius + margin)

        # Set circle color based on mood for the day, or white if no entry
        if day in entries_by_day:
            mood_name = entries_by_day[day]['Mood'].strip().lower() 
            color = 'white'
            for info in rasa_dict.values():
                rasa_name = info['rasa'].strip().lower()
                if mood_name == rasa_name:
                    color = info['color']
                    break
        else:
            color = 'white'

        # Draw the circle and day number text
        canvas.create_oval( x, 
                            y, 
                            x + 2 * circle_radius, 
                            y + 2 * circle_radius,
                            fill=color, 
                            outline="black")
        canvas.create_text(x + circle_radius, 
                        y + circle_radius,
                        text=str(day), 
                        font=("Helvetica", 10))
        
    # Position for the legend text (below the circles)
    legend_x = 50
    legend_y = y_start + ((days_in_month // max_per_row) + 2) * (2 * circle_radius + margin)

    # Add the title for the legend
    canvas.create_text(
        legend_x, 
        legend_y - 25,  
        text="Color Legend:",
        anchor='w',
        font=("Helvetica", 12, "bold")
        )
        
    # Position for the legend text (below the circles)
    legend_x = 50
    legend_y = y_start + ((days_in_month // max_per_row) + 2) * (2 * circle_radius + margin)

    # Show legend as text lines: "rasa name - color"
    for idx, rasa_info in enumerate(rasa_dict.values()):
        y = legend_y + idx * 20  # 20 px vertical spacing between lines
        legend_text = f"{rasa_info['color'].capitalize()} - {rasa_info['rasa'].title()} ({rasa_info['meaning'].title()})"
        
        canvas.create_text(
            legend_x, y,
            text=legend_text,
            anchor='w',  # align left
            font=("Helvetica", 10)
        )      
    
    window.mainloop()


def view_all_entries():
    """
    Display all journal entries filtered by a chosen rasa (emotion).

    Prompts the user to select one of the nine rasas by number,
    then reads the mood tracking CSV file and prints all entries matching that rasa.
    If no entries exist for the selected rasa or if the file doesn't exist,
    an appropriate message is displayed.
    """

    # Display the list of rasas for user to choose from
    print("\nChoose the rasa:\n")
    for key,value in rasa_dict.items():
        print(f"    {key}.{value['rasa'].title()} - {value['meaning'].title()}")
    
    # Prompt user for input and validate
    try:
        user_choice = int(input("\nEnter the number: "))
        if user_choice not in rasa_dict:
            print("Invalid choice. Try again.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    # Get chosen rasa name
    chosen_rasa = rasa_dict[user_choice]['rasa'].title()
    print(f"\nYour entries for {chosen_rasa}:\n")

    file_path = "mood_tracking.csv"

    # Check if the CSV file exists
    if not os.path.exists(file_path):
        print("No entries found.")
        return

    # Open and read the CSV file, filtering entries by chosen rasa
    with open(file_path,"r",newline='',encoding="utf-8") as file:
        reader = csv.DictReader(file)
        count = 0

        # Loop through each row and print matching entries
        for row in reader:
            if row['Mood'].strip().lower() == chosen_rasa.lower():
                print(f"Date: {row['Date']}")
                print(f"Prompt: {row['Prompt']}")
                print(f"Verse: {row['Verse']}\n")
                count += 1

        # Inform user if no matching entries found
        if count == 0:
            print("No entries found for this rasa.")

    input("\nPress Enter to return to the main menu...")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

    
# =================== Login Menu ===================
def main_menu():
    while True:
        clear_screen()
        print("\nWELCOME TO NAVARASAM MOOD TRACKER!\n")
        # Display menu options and prompt user input
        menu = input(
            '''\nEnter the option number:
            1. Learn about navarasam
            2. Start journaling
            3. View mood summary
            4. View all entries for a rasa
            0. Exit
            Response: ''').strip()

        # Validate that input is a digit
        if not menu.isdigit():
            print("Invalid input. Enter a number.")
            continue        
        
        # Convert input to integer for comparison
        menu = int(menu)

        # Call corresponding function based on user choice
        if menu == 1:
            clear_screen()
            learn_more()

        elif menu == 2:
            clear_screen()
            start_journaling()

        elif menu == 3:
            clear_screen()
            view_stats()

        elif menu == 4:
            clear_screen()
            view_all_entries()

        elif menu == 0:
            print("See you soon!")
            break

        else:
            # Handle invalid numeric input
            print("Invalid choice. Please select a valid menu option.")
            continue

if __name__ == "__main__":
    main_menu()
