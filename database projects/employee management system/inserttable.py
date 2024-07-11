import sqlite3
import random
from selectdata import SelectData
con = sqlite3.connect("company.db")
cur = con.cursor()

# cur.execute(''' ''')


class Check:
    def empty_table(tablename):
        cur.execute(f'''
                    SELECT CASE WHEN EXISTS (SELECT 1 FROM {tablename})
                    THEN 'false' ELSE 'true' END AS is_table_empty;
                    ''')
        res = cur.fetchall()
        return res[0][0]


class InsertData:

    def insert_register(data):
        cur.execute(''' 
                        INSERT INTO admin (
                        admin_id, admin_name, age, sex, phone, email, adress, company_name, username, password)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        ''', data)
        con.commit()

    # def insert_login(data):
    #     cur.execute('''
    #                 INSERT INTO login (
    #                 admin_id, username, password)
    #                 VALUES (?, ?, ?)
    #         ''', data)
    #     con.commit()

    def insert_employee(data):
        cur.execute('''
                    INSERT INTO employee (
                    admin_id, emp_id, name, phone, desigination, email, adress, income, tax, dept_id)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

                    ''', data)
        con.commit()

    def insert_department(data):
        cur.execute('''
                    INSERT INTO department (
                    admin_id, dept_id, dept_name, dept_info) 
                    VALUES (?, ?, ?, ?)
                    ''', data)
        con.commit()

    def insert_attendance(data):
        cur.execute('''
                    INSERT INTO attendance (
                        admin_id,emp_id,attend_id, emp_name, date, status) 
                        VALUES (?, ?,?, ?,?, ?)
                    ''', data)
        con.commit()

    def update_department(data):
        cur.execute('''
                    UPDATE department
                            SET dept_name = ?, dept_info = ?
                    WHERE 
                        dept_id = ?;

                    ''', data)
        con.commit()

    def update_employee(data):
        cur.execute('''
                    UPDATE employee
                            SET name = ?, phone = ?,desigination=?, email=?, adress=?, income=?, tax=?, dept_id=?
                    WHERE 
                        emp_id = ?;

                    ''', data)
        con.commit()

    def insert_status(data):
        cur.execute(
            "insert into to_do_list (admin_id,id,name,details,date,status) values(?,?,?,?,?,?) ", data)
        con.commit()
# admin id current string emp_id string emp_name all present in table

    def insert_attendance_data(admin_id, emp_id, emp_name):
        status = [0, 1, 2]
        num = SelectData.select_last_element(
            "attend_id", "attendance", "attend_id")

        for i in range(1, 31):
            num += 1
            cur.execute('''
                        INSERT INTO attendance (
                            admin_id,emp_id,attend_id, emp_name, date, status) 
                            VALUES (?, ?,?, ?,?, ?)
                        ''', (admin_id, emp_id, num, emp_name, f"2024-01-{i}", random.choice(status),))
            con.commit()


# cur.execute("drop table attendance")
# InsertData.insert_attendance_data("A102", "E104", "rishika")
