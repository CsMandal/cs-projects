import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()


class SelectData:
    def select_last_element(tablename, column):
        pass

    def login(value):
        cur.execute(
            "SELECT admin_id, name FROM admin WHERE username=? AND password=?", value)
        return cur.fetchall()

    def check_table_is_empty(tablename):
        pass

    def select_all_data(tablename, column, value):
        cur.execute(f"select * from {tablename} where {column} =?", (value,))
        return cur.fetchall()

    def check_done(data):
        cur.execute(
            f"select count(*) from status where admin_id =? and task_id=? and date=?", data)
        return cur.fetchall()

    def select_count_done(user_id, date):
        cur.execute(
            "SELECT COUNT(*) FROM   status WHERE admin_id = ? and status= ? and date=?", (user_id, 1, date,))
        count = cur.fetchone()
        return count

    def select_count_fail(user_id, date):
        cur.execute(
            "SELECT COUNT(*) FROM status WHERE admin_id = ? and status= ? and date=?", (user_id, 0, date,))
        count = cur.fetchone()
        return count

    def check_value_or_not(tablename):
        cur.execute(f"SELECT COUNT(*) FROM {tablename}")

    def update_todolist(task_id):
        cur.execute(
            "UPDATE to_do_list SET status = 1 WHERE list_id = ?", (task_id,))
        con.commit()

    def delete_task(task_id):
        cur.execute("DELETE FROM to_do_list WHERE list_id = ?", (task_id,))
        con.commit()

    def update_task_list():
        return cur.execute("SELECT list_id,date, details FROM to_do_list WHERE status = 0")

    def count_report(data):
        cur.execute(
            "select count(*) from maintask where task_name = ? and admin_id =?", data)
        return cur.fetchone()

    def select_all_report(data):
        cur.execute(
            "select * from status where task_id =? and admin_id=? order by date desc", data)
        return cur.fetchall()

    def select_task_id(data):
        cur.execute(
            "select task_id from maintask where task_name=? and admin_id=?", data)
        return cur.fetchone()

    # def done_report(data):
    #     cur.execute(
    #         "select count(*) from status where task_id=? and status = 1", data)
    #     cur.fetchone()

    def fail_report(data):
        return cur.execute("select count(*) from status where task_id=? and status = 0", data).fetchone()

    def done_report(data):
        return cur.execute("select count(*) from status where task_id=? and status = 1", data).fetchone()

    def select_all_maintask(data):
        return cur.execute("select * from maintask where task_name=? and admin_id=?", data).fetchone()

    def select_note_comment(data):
        return cur.execute("select task, comment from subtask where task_id=? and admin_id=?", data).fetchall()


# value = SelectData.select_task_id(("study", 2))
# print(value[0])
# if value[0]:
#     print("yes")
