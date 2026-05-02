import sqlite3

def main():
    # Connect to the database.
    conn = sqlite3.connect('phonebook.db')

    # Get a database cursor.
    cur = conn.cursor()
    
    # Add the Entries table.
    add_phonebook_table(cur)
    
    # Add rows to the Entries table.
    add_Entries(cur)
    
    # Commit the changes.
    conn.commit()
    
    # Close the connection.
    conn.close()

# The add_cities_table adds the Cities table to the database.
def add_phonebook_table(cur):
    # If the table already exists, drop it.
    cur.execute('DROP TABLE IF EXISTS Cities')

    # Create the table.
    cur.execute('''CREATE TABLE Entries (Name TEXT,
                                         Number REAL)''')

# The add_cities function adds 20 rows to the Cities table.
def add_Entries(cur):
    Entries    = [('John Smith', 1234567890),
                  ('Me', 5),
                  ('You', 67)]
    
    for row in Entries:
        cur.execute('''INSERT INTO Entries (Name, Number)
                       VALUES (?, ?)''', (row[0], row[1]))

# The display_cities function displays the contents of
# the Cities table.


# Execute the main function.
if __name__ == '__main__':
    main()
