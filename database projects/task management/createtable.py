import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()


class CreateTable:
    def create_table_admin():
        cur.execute('''
                    CREATE TABLE IF NOT EXISTS admin  (
                            admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            age INTEGER,
                            phone TEXT,
                            email TEXT UNIQUE NOT NULL,
                            college TEXT,
                            username TEXT UNIQUE NOT NULL,
                            password TEXT NOT NULL,
                            goal TEXT
                                        );
                    ''')

    def create_maintask_table():
        cur.execute('''
                    CREATE TABLE IF NOT EXISTS maintask (
                            admin_id INTEGER,
                            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            start_time TIME,
                            end_time TIME,
                            task_name TEXT NOT NULL,
                            desc TEXT,
                            daycount INTEGER,
                            FOREIGN KEY (admin_id) REFERENCES admin(admin_id)
                        );
                    ''')

    def create_subtask_table():
        cur.execute('''
                    CREATE TABLE  IF NOT EXISTS subtask (
                            admin_id INTEGER,
                            task_id INTEGER,
                            subtask_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            task TEXT NOT NULL,
                            comment TEXT,
                            FOREIGN KEY (admin_id) REFERENCES admin(admin_id),
                            FOREIGN KEY (task_id) REFERENCES maintask(task_id)
                        );

                    ''')

    def create_todolist_table():
        cur.execute('''
                    CREATE TABLE IF NOT EXISTS to_do_list (
                            admin_id INTEGER,
                            list_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            details TEXT NOT NULL,
                            date TEXT,
                            status bool,
                            FOREIGN KEY (admin_id) REFERENCES admin(admin_id)
                        );

                    ''')

    def create_report_table():
        cur.execute('''
                    CREATE TABLE IF NOT EXISTS  status (
                            admin_id INTEGER,
                            task_id INTEGER,
                            status_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            date date,
                            status bool,
                            FOREIGN KEY (admin_id) REFERENCES admin(admin_id),
                            FOREIGN KEY (task_id) REFERENCES maintask(task_id)
                        );

                    ''')

    def check_the_table_empty(tablename):
        cur.execute(f'''CREATE TABLE IF NOT EXISTS {tablename}_insert_flag (
                flag INTEGER DEFAULT 0
             )''')

        cur.execute(
            f'''INSERT INTO {tablename}_insert_flag (flag) VALUES (0)''')

        cur.execute(f'''CREATE TRIGGER IF NOT EXISTS set_{tablename}_insert_flag
             AFTER INSERT ON {tablename}
             BEGIN
                UPDATE {tablename}_insert_flag SET flag = 1 WHERE flag = 0;
             END;''')

    def droptable(tablename):
        cur.execute(f"drop table {tablename}")


CreateTable.create_table_admin()
CreateTable.create_maintask_table()
CreateTable.create_report_table()
CreateTable.create_subtask_table()
CreateTable.create_todolist_table()
