import sqlite3

def main():
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()
    while(True):
        command = input("Would you like to read an entry (type: read), delete an entry (type: delete), or edit an entry (type: edit)? \nTo end this program, enter \"end\" ")
        if (command == 'read'):
            name = input("What is the name you want to find? ")
            results = cur.execute('SELECT Name, Number FROM Entries WHERE Name = ?', (name,))
            for row in results:
                print(f'{row[0]:2} {row[1]:20}')

        elif (command == 'delete'):
            name = input("What name would you like to delete? ")
            cur.execute('DELETE FROM Entries WHERE Name = ?', (name,))

        elif(command == 'edit'):
            name = input("What name would you like to edit? ")
            number = input(f"What would you like to update {name}'s number to? ")
            cur.execute("UPDATE Entries SET Number = ? WHERE Name = ?", (number, name))
        
        elif(command == 'end'):
            break

        else:
            print("Invalid command, please try again")




if __name__ == '__main__':
    main()