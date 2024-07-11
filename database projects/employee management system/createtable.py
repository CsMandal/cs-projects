import sqlite3

con = sqlite3.connect("company.db")
cur = con.cursor()
# #cur.execute('''  ''')


class CrateTable:
    def create_register():
        cur.execute('''
                    create table IF NOT EXISTS admin(
                        admin_id varchar(4) primary key,
                        admin_name varchar(25) not null,
                        age int,
                        sex char(1),
                        phone varchar(10) not null unique,
                        email varchar(40) not null unique,
                        adress varchar(50),
                        company_name varchar(50) not null,
                        username varchar(12) not null unique,
                        password varchar(16)
                        )
                    ''')

    # def create_login():
    #     cur.execute('''
    #                 create table IF NOT EXISTS login(
    #                     admin_id varchar(4) primary key,
    #                     username varchar(12),
    #                     password varchar(16),
    #                     foreign key (admin_id) references admin(admin_id) on delete set null
    #                 )

    #                  ''')

    def create_employee():
        cur.execute(''' 
                    create table IF NOT EXISTS employee(
                        admin_id varchar(4),
                        emp_id varchar(4) primary key,
                        name varchar(25) not null ,
                        phone varchar(10) not null unique ,
                        desigination varchar(20) not null,
                        email varchar(40) ,
                        adress varchar(50),
                        income float not null,
                        tax float not null,
                        dept_id varchar(4) not null,
                        foreign key(admin_id) references admin(admin_id) on delete set null,
                        foreign key(dept_id) references department(dept_id) on delete set null
                    )
                    ''')

    def create_department():
        cur.execute('''
                    create table IF NOT EXISTS department(
                        admin_id varchar(4),
                        dept_id varchar(4) ,
                        dept_name varchar(30),
                        dept_info varchar(50),
                        foreign key(admin_id) references admin(admin_id) on delete set null,
                        primary key(admin_id, dept_id)
                    )

                  ''')

    def create_attendance():
        cur.execute(''' 
                    create table IF NOT EXISTS attendance(
                        admin_id varchar(4),
                        emp_id varchar(4),
                        attend_id int primary key,
                        emp_name varchar(20),
                        date date,
                        status tinyint,
                        foreign key(emp_id) references employee(emp_id) on delete cascade,
                        foreign key(admin_id) references register(admin_id)on delete set null
                    )
                    ''')

    def create_addtask_table():
        cur.execute('''
                    CREATE TABLE IF NOT EXISTS to_do_list (
                            admin_id INTEGER,
                            list_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            id TEXT,
                            name TEXT,
                            details TEXT NOT NULL,
                            date TEXT,
                            status bool,
                            FOREIGN KEY (admin_id) REFERENCES admin(admin_id)
                        );

                    ''')


CrateTable.create_attendance()
CrateTable.create_department()
CrateTable.create_employee()
CrateTable.create_register()
CrateTable.create_addtask_table()
