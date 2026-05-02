import sqlite3

def main():
    conn = sqlite3.connect("cities.db")
    cur = conn.cursor()
    cur.execute('SELECT CityID, CityName, Population FROM Cities')
    results = cur.fetchall()

    for row in results:
        print(f'{row[0]:30}  {row[1]:30} {row[2]:5}')
    
    conn.close()

if __name__ == '__main__':
    main()