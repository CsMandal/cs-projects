import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS your_table (
                    id INTEGER PRIMARY KEY,
                    value TEXT)''')

# Create a trigger to check if a value exists in the table before inserting
cursor.execute('''CREATE TRIGGER IF NOT EXISTS check_value
                    BEFORE INSERT ON your_table
                    FOR EACH ROW
                    BEGIN
                        SELECT CASE
                            WHEN EXISTS (SELECT 1 FROM your_table WHERE value = NEW.value) 
                            THEN RAISE(ABORT, 'Value already exists in the table')
                            END;
                    END;''')

# Example: Inserting a value
try:
    cursor.execute("INSERT INTO your_table (value) VALUES (?)", ('example_value',))
    conn.commit()
    print("Value inserted successfully")
except sqlite3.Error as e:
    print("Error:", e)

# Example: Trying to insert a duplicate value
try:
    cursor.execute("INSERT INTO your_table (value) VALUES (?)", ('example_value',))
    conn.commit()
    print("Value inserted successfully")
except sqlite3.Error as e:
    print("Error:", e)

# Close the connection
conn.close()
