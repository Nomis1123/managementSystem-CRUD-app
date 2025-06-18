# Player Management System - A CRUD Application in Python with Tkinter

This project is a complete desktop application for managing player data, built using Python's native `tkinter` GUI toolkit. It demonstrates the fundamentals of GUI development, event-driven programming, and persistent data storage using a local CSV file.

The application provides a user-friendly interface to perform all essential Create, Read, Update, and Delete (CRUD) operations on a collection of player records.

## Features

*   **Full CRUD Functionality:**
    *   **Create:** Add new player records with a first name, last name, unique player ID, and highest score.
    *   **Read:** Display all player records in an organized, sortable table.
    *   **Update:** Select any player from the table to populate their data into input fields, modify it, and save the changes.
    *   **Delete:** Remove selected player records permanently from the dataset.
*   **Persistent Data Storage:**
    *   All player data is stored locally in a `players.csv` file.
    *   The application automatically creates this file with the correct headers on its first run if it doesn't already exist, making it self-initializing.
*   **Interactive & User-Friendly GUI:**
    *   **Interactive Data Table:** Uses a `ttk.Treeview` widget to present data in a clean, readable format.
    *   **Click-to-Sort Columns:** All table columns can be sorted in ascending or descending order by simply clicking on their headers. The sorting logic correctly handles both alphabetic and numeric data types.
    *   **Easy Record Updating:** Clicking a record in the table automatically populates the input fields, making the update process quick and intuitive.
    *   **Robust Input Validation:**
        *   Ensures all fields are filled before adding or updating a record.
        *   Validates that Player ID and Highest Score are numeric and within specified ranges (0-999 for ID, 0-9999 for Score).
        *   Checks for string length limits on names.
        *   Prevents the creation of duplicate Player IDs.
    *   **User Feedback:** Provides clear success and error messages to the user via `messagebox` pop-ups.
## Usage

To run the application, execute the Python script from your terminal:

```sh
python a2_player_mgmt.py
```

This will launch the "Player Management System" GUI window. From there, you can:
1.  Enter player details in the "Player Info" section and click **Add Record**.
2.  Click on any record in the table to load its data into the input fields.
3.  Modify the data and click **Update Record** to save changes.
4.  Select a record and click **Delete Record** to remove it.
5.  Click on column headers like "Player ID" or "Highest Score" to sort the data.
