import sqlite3

con = sqlite3.connect("company.db")
cur = con.cursor()


class SelectData:
    def select_last_element(column_return, tablename, column):
        cur.execute(
            f"SELECT {column_return} FROM {tablename} ORDER BY {column} DESC LIMIT 1;")
        res = cur.fetchall()
        return res[0][0]

    def if_value_present(tablename, column, value):
        cur.execute(f'''
        SELECT COUNT(*) FROM {tablename} WHERE {column} = ?;
            ''', (value,))
        res = cur.fetchall()
        return res[0][0]

    def authorize(data):
        cur.execute(
            "select * from admin where username= ? and password = ?;", data)
        res = cur.fetchall()
        return res

    def last_dept_id():
        cur.execute(
            """SELECT dept, MAX(dept_id) AS last_dept_id
            FROM department
            GROUP BY emp_id;
            """)

    def select_all_data(tablename, question, value):
        cur.execute(f'''
                    select * from {tablename} where {question} = ?
                    ''', (value,))
        return cur.fetchall()

    def attendance_status(emp_id, start_date, end_date):
        cur.execute('''
                    SELECT 
                        SUM(CASE WHEN status = 2 THEN 1 ELSE 0 END) AS total_present,
                        SUM(CASE WHEN status = 1 THEN 1 ELSE 0 END) AS total_half_day,
                        SUM(CASE WHEN status = 0 THEN 1 ELSE 0 END) AS total_absent
                    FROM 
                        attendance
                    WHERE 
                        emp_id = ? and
                        date between ? and ?
                        ;

                    ''', (emp_id, start_date, end_date,))
        return (cur.fetchone())

    def select_all_data_2_values(tablename, question, value, question2, value2):
        cur.execute(f'''
                    select * from {tablename} where {question} = ? and {question2}=?
                    ''', (value, value2,))
        return cur.fetchall()

    def if_value_present_date(tablename, column1, value1, column2, value2):
        cur.execute(f'''
        SELECT COUNT(*) FROM {tablename} WHERE {column1} = ? and {column2}=?;
            ''', (value1, value2,))
        res = cur.fetchall()
        return res[0][0]

    def delete_dept(tablename, column, value):
        cur.execute(f'''
                    DELETE FROM {tablename}
                        WHERE {column}=?;
                    ''', (value,))
        con.commit()
        return cur.fetchall()

    def update_todolist(task_id):
        cur.execute(
            "UPDATE to_do_list SET status = 1 WHERE list_id = ?", (task_id,))
        con.commit()

    def delete_task(task_id):
        cur.execute("DELETE FROM to_do_list WHERE list_id = ?", (task_id,))
        con.commit()

    def update_task_list():
        return cur.execute("SELECT list_id,date,name, details FROM to_do_list WHERE status = 0")
