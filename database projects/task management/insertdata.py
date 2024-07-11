import sqlite3
import random

con = sqlite3.connect("database.db")
cur = con.cursor()


class InsertData:

    def empty_table(tablename):
        cur.execute(f'''
                    SELECT CASE WHEN EXISTS (SELECT 1 FROM {tablename})
                    THEN 'false' ELSE 'true' END AS is_table_empty;
                    ''')
        res = cur.fetchall()
        return res[0][0]

    def empty_table1(tablename):
        cur.execute('''
                    CREATE PROCEDURE check_table_empty({tablename} TEXT, OUT is_table_empty TEXT)
                            AS
                            BEGIN
                                DECLARE table_count INTEGER;
                                SELECT COUNT(*) INTO table_count FROM sqlite_master WHERE type='table' AND name=tablename;
                                IF table_count > 0 THEN
                                    SET is_table_empty = 'false';
                                ELSE
                                    SET is_table_empty = 'true';
                                END IF;
                            END;

                    ''')

    def insert_admin(data):
        cur.execute("""INSERT INTO admin (name, age, phone, email, college, username, password, goal) 
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", data)
        con.commit()

    def insert_maintask(data):
        cur.execute('''
                    INSERT INTO maintask (admin_id,start_time,end_time,task_name,desc,daycount)
                    VALUES(?,?,?,?,?,?)
                    ''', data)
        con.commit()

    def check_value(tablename, value):
        cur.execute(f'''CREATE TRIGGER IF NOT EXISTS check_value
                    BEFORE INSERT ON {tablename}
                    FOR EACH ROW
                    BEGIN
                        SELECT CASE
                            WHEN EXISTS (SELECT 1 FROM {tablename} WHERE {value} = NEW.value) 
                            THEN RAISE(ABORT, 'false')
                            END;
                    END;''')

        try:
            cur.execute(f"INSERT INTO {tablename} (value) VALUES (?)",
                        (value,))
            con.commit()
            print("Value inserted successfully")
        except sqlite3.Error as e:
            print("Error:", e)

    def update_maintask(data):
        cur.execute("""
                            UPDATE maintask SET start_time=?,end_time=?,task_name=?,desc=?,daycount=?
                            WHERE task_id=?
                            """, data)
        con.commit()

    def insert_subtask(data):
        cur.execute(
            "insert into subtask (admin_id,task_id,task,comment) values(?,?,?,?)", data)
        con.commit()

    def insert_todolist(data):
        cur.execute(
            "insert into to_do_list (admin_id,details,date,status) values (?,?,?,?)", data)
        con.commit()

    def insert_status(data):
        cur.execute(
            "insert into status (admin_id,task_id,date,status) values(?,?,?,?) ", data)
        con.commit()

    def insert_report_manually():
        for i in range(1, 31):
            InsertData.insert_status(
                (1, 2, f"2024-01-{i}", random.choice((0, 1))))
