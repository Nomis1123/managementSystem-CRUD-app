import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os

# File name
FILE_NAME = 'players.csv'

# Ensure CSV file exists, create one when it is not there
if not os.path.isfile(FILE_NAME):
    # create CSV file if file is not exist
    with open(FILE_NAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['first_name', 'last_name', 'player_id', 'highest_score'])

# Read data from CSV file
def read_data():
    with open(FILE_NAME, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

# Write data to CSV file
def write_data(data):
    with open(FILE_NAME, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['first_name', 'last_name', 'player_id', 'highest_score'])
        writer.writeheader()
        writer.writerows(data)

# Add a new record
def add_record():
    first_name = entry_first_name.get().strip()
    last_name = entry_last_name.get().strip()
    player_id = entry_player_id.get().strip()
    highest_score = entry_highest_score.get().strip()

    # Empty field is not allowed
    if not first_name or not last_name or not player_id or not highest_score:
        messagebox.showerror('Input Error', 'All fields are required.')
        return

    # Validate that inputted data
    if not player_id.isdigit() or int(player_id) < 0 or int(player_id) > 999 :
        messagebox.showerror('Input Error', 'Player ID must be numeric(1-999).')
        return

    if not highest_score.isdigit() or int(highest_score) < 0 or int(highest_score) > 9999 :
        messagebox.showerror('Input Error', 'Highest Score must be numeric(1-9999).')
        return

    if len(first_name) > 20 or len(last_name) > 20:
        messagebox.showerror('Input Error', 'length of first_name and last_name can not exceed 20')
        return

    # Retrieve existed player
    data = read_data()
    for row in data:
        # Duplicated player_id is not allowed
        if row['player_id'] == player_id:
            messagebox.showerror('Duplicate Error', f'Player ID {player_id} already exists.')
            return

    # Update CSV file, display
    data.append({'first_name': first_name, 'last_name': last_name, 'player_id': player_id, 'highest_score': highest_score})
    write_data(data)
    refresh_treeview()
    clear_inputs()
    messagebox.showinfo('Success', 'Record added successfully!')

# Refresh Treeview
def refresh_treeview():
    for row in tree.get_children():
        tree.delete(row)
    for row in read_data():
        tree.insert('', 'end', values=(row['first_name'], row['last_name'], row['player_id'], row['highest_score']))

# Clear input fields
def clear_inputs():
    entry_first_name.delete(0, tk.END)
    entry_last_name.delete(0, tk.END)
    entry_player_id.delete(0, tk.END)
    entry_highest_score.delete(0, tk.END)

# Delete selected record
def delete_record():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Selection Error', 'No record selected.')
        return

    # Use player_id as key field to sort out record
    item = tree.item(selected_item)
    player_id = item['values'][2]

    # Remove record through player_id
    data = read_data()
    data = [row for row in data if int(row['player_id']) != player_id]
    write_data(data)
    refresh_treeview()
    messagebox.showinfo('Success', 'Record deleted successfully!')

# Update selected record
def update_record():
    # Determine there is selected record
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Selection Error', 'No record selected.')
        return

    # Read input
    first_name = entry_first_name.get().strip()
    last_name = entry_last_name.get().strip()
    player_id = entry_player_id.get().strip()
    highest_score = entry_highest_score.get().strip()

    # Empty field is not allowed
    if not first_name or not last_name or not player_id or not highest_score:
        messagebox.showerror('Input Error', 'All fields are required.')
        return

    # Validate that inputted data
    if not player_id.isdigit() or int(player_id) < 0 or int(player_id) > 999 :
        messagebox.showerror('Input Error', 'Player ID must be numeric(1-999).')
        return

    if not highest_score.isdigit() or int(highest_score) < 0 or int(highest_score) > 9999 :
        messagebox.showerror('Input Error', 'Highest Score must be numeric(1-9999).')
        return

    if len(first_name) > 20 or len(last_name) > 20:
        messagebox.showerror('Input Error', 'length of first_name and last_name can not exceed 20')
        return

    # Read information of selected player
    item = tree.item(selected_item)
    original_player_id = item['values'][2]

    # Read all player information
    data = read_data()
    # Duplicated player_id is not allowed
    for row in data:
        if row['player_id'] == player_id and int(player_id) != original_player_id:
            messagebox.showerror('Duplicate Error', f'Player ID {player_id} already exists.')
            return

    # Update record with input data
    for row in data:
        if int(row['player_id']) == original_player_id:
            row.update({'first_name': first_name, 'last_name': last_name, 'player_id': player_id, 'highest_score': highest_score})
            break

    write_data(data)
    refresh_treeview()
    clear_inputs()
    messagebox.showinfo('Success', 'Record updated successfully!')

# Populate input fields from selected record
def populate_inputs(event):
    selected_item = tree.selection()
    if not selected_item:
        return

    item = tree.item(selected_item)
    values = item['values']

    entry_first_name.delete(0, tk.END)
    entry_first_name.insert(0, values[0])
    entry_last_name.delete(0, tk.END)
    entry_last_name.insert(0, values[1])
    entry_player_id.delete(0, tk.END)
    entry_player_id.insert(0, values[2])
    entry_highest_score.delete(0, tk.END)
    entry_highest_score.insert(0, values[3])

# Display players' information sorted by any column
def sort_treeview(col, reverse):
    # Retrieve all data from the TreeView
    data = [(tree.set(child, col), child) for child in tree.get_children('')]

    # Sort by the column value (convert to int for numeric sorting)
    if col in ('player_id', 'highest_score'):
        data.sort(key=lambda t: int(t[0]), reverse=reverse)
    else:
        data.sort(reverse=reverse)

    # Rearrange items in the Treeview based on sorted data
    for index, (val, child) in enumerate(data):
        tree.move(child, '', index)

    # Reverse the sorting order for the next click
    tree.heading(col, command=lambda: sort_treeview(col, not reverse))

# GUI setup
window = tk.Tk()
window.title('Player Management System')
window.geometry('820x450')

# Frame for input player's information
frame_input = tk.LabelFrame(window, text="Player Info")
frame_input.pack(pady=10)

tk.Label(frame_input, text='First Name').grid(row=0, column=0, padx=5, pady=5)
entry_first_name = tk.Entry(frame_input)
entry_first_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text='Last Name').grid(row=1, column=0, padx=5, pady=5)
entry_last_name = tk.Entry(frame_input)
entry_last_name.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_input, text='Player ID').grid(row=2, column=0, padx=5, pady=5)
entry_player_id = tk.Entry(frame_input)
entry_player_id.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_input, text='Highest Score').grid(row=3, column=0, padx=5, pady=5)
entry_highest_score = tk.Entry(frame_input)
entry_highest_score.grid(row=3, column=1, padx=5, pady=5)

frame_buttons = tk.Frame(window)
frame_buttons.pack(pady=10)

# Frame to host buttons
# Add button
btn_add = tk.Button(frame_buttons, text='Add Record', command=add_record)
btn_add.grid(row=0, column=0, padx=5)

# Update button
btn_update = tk.Button(frame_buttons, text='Update Record', command=update_record)
btn_update.grid(row=0, column=1, padx=5)

# Delete button
btn_delete = tk.Button(frame_buttons, text='Delete Record', command=delete_record)
btn_delete.grid(row=0, column=2, padx=5)

# Button to clean input
btn_clear = tk.Button(frame_buttons, text='Clear Inputs', command=clear_inputs)
btn_clear.grid(row=0, column=3, padx=5)

# Frame to display players
frame_tree = tk.Frame(window)
frame_tree.pack(pady=10)

columns = ('first_name', 'last_name', 'player_id', 'highest_score')
tree = ttk.Treeview(frame_tree, columns=columns, show='headings', height=8)
tree.heading('first_name', text='First Name')
tree.heading('last_name', text='Last Name')
tree.heading('player_id', text='Player ID')
tree.heading('highest_score', text='Highest Score')
tree.pack()

tree.bind('<<TreeviewSelect>>', populate_inputs)

# Bind sorting function to Treeview headers
for col in columns:
    tree.heading(col, text=col.replace('_', ' ').title(),
                 command=lambda _col=col: sort_treeview(_col, False))

refresh_treeview()

window.mainloop()
