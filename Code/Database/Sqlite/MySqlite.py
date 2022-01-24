import sqlite3
import datetime


class MySqlite:
    conn = None
    day_titles = [
        "Monday 1",
        "Tuesday 1",
        "Wednesday 1",
        "Thursday 1",
        "Friday 1",
        "Saturday 1",
        "Sunday 1",
        "Monday 2",
        "Tuesday 2",
        "Wednesday 2",
        "Thursday 2",
        "Friday 2",
        "Saturday 2",
        "Sunday 2",
    ]
    __create_constructions = {
        "create_departments_table":
            """
            CREATE TABLE IF NOT EXISTS Department(
            Department_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Title TEXT,
            DESCRIPTION TEXT);
            """
        ,
        "create_actions_table":
            """
            CREATE TABLE IF NOT EXISTS Action(
            Action_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Title TEXT,
            DESCRIPTION TEXT,
            Department_ID INTEGER,
            FOREIGN KEY (Department_ID) REFERENCES Department (Department_ID) ON DELETE CASCADE);
            """,
        "create_days_table":
            """
            CREATE TABLE IF NOT EXISTS Day(
            Day_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Title TEXT,
            Days_date TEXT);
            """,
        "create_days_configurations_table":
            """
            CREATE TABLE IF NOT EXISTS Day_configuration(
            Days_configuration_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Day_ID INTEGER,
            Start TEXT,
            Finish TEXT,
            Department_ID INTEGER,
            Type TEXT,
            FOREIGN KEY (Department_ID) REFERENCES Department (Department_ID) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY (Day_ID) REFERENCES Day (Day_ID) ON DELETE CASCADE ON UPDATE CASCADE);
            """
    }

    def __connection(self):
        self.conn = sqlite3.connect('llk.db')

    def get_days_data_by_title(self, title):
        self.__connection()
        cursor = self.conn.cursor()
        cursor.execute(
            f"SELECT Days_date FROM Day WHERE Title =\"{title}\""
        )
        results = cursor.fetchall()
        cursor.close()
        self.conn.close()
        return results[0][0] if len(results) > 0 else None

    def update_days_date_by_title_on_value(self, title, value):
        self.__connection()
        cursor = self.conn.cursor()
        cursor.execute(
            f"UPDATE Day SET Days_date = \"{value}\" WHERE Title =\"{title}\""
        )
        self.conn.commit()
        cursor.close()
        self.conn.close()

    def go_forward_with_data(self):
        today = datetime.datetime.today().date()
        for item in self.day_titles:
            that_date = self.get_days_data_by_title(item)
            date_time_obj = datetime.datetime.strptime(that_date, '%Y-%m-%d').date()
            delta_days = (today - date_time_obj).days
            if delta_days > 0:
                differance = (delta_days / 14).__ceil__() * 14
                new_date = date_time_obj + datetime.timedelta(days=differance)
                self.update_days_date_by_title_on_value(item, new_date)

    def create_tables(self):
        """
        Table 'Department':
            1. Department_ID: int (PK)
            2. Title: str
            3. DESCRIPTION: str

        Table 'Action':
            1. Department_ID: int (FK)
            2. Action_ID: int (PK)
            3. Title: str
            4. DESCRIPTION: str

        Table 'Day':
            1. Day_ID: int (PK)
            2. Title: str
            3. Days_date: str //points on current week

        Table 'Day_configuration':
            1. Days_configuration_ID: int (PK)
            2. Day_ID: int (FK)
            3. Start: str
            4. Finish: str
            5. Department_ID: int (FK)
            6. Type: str
        :return: None
        """
        self.__connection()
        cursor = self.conn.cursor()
        for item in self.__create_constructions.keys():
            cursor.execute(self.__create_constructions[item])
            self.conn.commit()
        cursor.close()
        self.conn.close()

    @staticmethod
    def get_next_weeks_days_data_by_title(title):
        return MySqlite.get_this_weeks_days_data_by_title(title) + datetime.timedelta(days=7)

    def get_days_title_by_date(self, date):
        self.__connection()
        cursor = self.conn.cursor()
        cursor.execute(
            f"SELECT Title FROM Day WHERE Days_date =\"{date}\""
        )
        results = cursor.fetchall()
        cursor.close()
        self.conn.close()
        return results[0][0] if len(results) > 0 else None

    @staticmethod
    def get_this_weeks_days_data_by_title(title):
        translator = {
            "Monday": 1,
            "Tuesday": 2,
            "Wednesday": 3,
            "Thursday": 4,
            "Friday": 5,
            "Saturday": 6,
            "Sunday": 7
        }
        current = datetime.datetime.today().date().isoweekday()
        finding = translator[title]
        return datetime.datetime.today().date() + datetime.timedelta(days=finding - current)

    def add_days(self):
        if self.get_days_id_by_title('Monday 1') is None:
            print('Days adding')
            self.__connection()
            cursor = self.conn.cursor()
            for title in self.day_titles:
                cursor.execute(
                    f"""
                    INSERT INTO Day(Title, Days_date) VALUES(\"{title}\",
                    \"{str(MySqlite.get_this_weeks_days_data_by_title(title.split(' ')[0])) if title.split(' ')[-1] == '1' else str(MySqlite.get_next_weeks_days_data_by_title(title.split(' ')[0]))}\");
                    """
                )
                self.conn.commit()
            cursor.close()
            self.conn.close()

    def insert_days_item(self, start, finish, department_title, type_, day_title):
        department_id = self.get_department_id_by_title(department_title)
        day_id = self.get_days_id_by_title(day_title)
        if department_id is not None and day_id is not None:
            self.__connection()
            cursor = self.conn.cursor()
            cursor.execute(
                f"""INSERT INTO Day_configuration(Day_ID, Start, Finish, Department_ID, Type) VALUES({day_id}, \"{str(start)}\", \"{str(finish)}\", {department_id}, \"{type_}\");"""
            )
            self.conn.commit()
            cursor.close()
            self.conn.close()

    def insert_department(self, title, description):
        self.__connection()
        cursor = self.conn.cursor()
        cursor.execute(
            f"INSERT INTO Department(Title, DESCRIPTION) VALUES(\"{title}\", \"{description}\");"
        )
        self.conn.commit()
        cursor.close()
        self.conn.close()

    def remove_department(self, title):
        self.__connection()
        cursor = self.conn.cursor()
        cursor.execute(
            f"DELETE FROM Department WHERE Title=\"{title}\";"
        )
        self.conn.commit()
        cursor.close()
        self.conn.close()

    def insert_action(self, department_title, title, description):
        department_id = self.get_department_id_by_title(department_title)
        self.__connection()
        cursor = self.conn.cursor()
        cursor.execute(
            f"INSERT INTO Action(Department_ID, Title, DESCRIPTION) VALUES ({department_id}, '{title}', '{description}');"
        )
        self.conn.commit()
        cursor.close()
        self.conn.close()

    def remove_action(self, title):
        self.__connection()
        cursor = self.conn.cursor()
        cursor.execute(
            f"DELETE FROM Action WHERE Title=\"{title}\";"
        )
        self.conn.commit()
        cursor.close()
        self.conn.close()

    def remove_day_item(self, day, start):
        day_id = self.get_days_id_by_title(day)
        if day_id is not None:
            self.__connection()
            cursor = self.conn.cursor()
            cursor.execute(
                f"DELETE FROM Day_configuration WHERE Day_ID= {day_id} AND Start=\"{start}\";"
            )
            self.conn.commit()
            cursor.close()
            self.conn.close()

    def get_department_id_by_title(self, title):
        self.__connection()
        cursor = self.conn.cursor()
        cursor.execute(
            f"SELECT Department_ID FROM Department WHERE Title =\"{title}\""
        )
        results = cursor.fetchall()
        cursor.close()
        self.conn.close()
        return results[0][0] if len(results) > 0 else None

    def get_department_title_by_id(self, id):
        self.__connection()
        cursor = self.conn.cursor()
        cursor.execute(
            f"SELECT Title FROM Department WHERE Department_ID ={id}"
        )
        results = cursor.fetchall()
        cursor.close()
        self.conn.close()
        return results[0][0] if len(results) > 0 else None

    def get_days_id_by_title(self, title):
        self.__connection()
        cursor = self.conn.cursor()
        cursor.execute(
            f"SELECT Day_ID FROM Day WHERE Title =\"{title}\""
        )
        results = cursor.fetchall()
        cursor.close()
        self.conn.close()
        return results[0][0] if len(results) > 0 else None

    def get_departments(self):
        self.__connection()
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT Title, DESCRIPTION FROM Department ORDER BY Title"
        )
        results = cursor.fetchall()
        cursor.close()
        self.conn.close()
        return results

    def get_days_configs_by_days_title(self, title):
        days_id = self.get_days_id_by_title(title)
        if days_id is not None:
            self.__connection()
            cursor = self.conn.cursor()
            cursor.execute(
                f"SELECT Start, Finish, Department_ID, Type FROM Day_configuration WHERE Day_ID = {days_id}"
            )
            results = cursor.fetchall()
            cursor.close()
            self.conn.close()
            return results

    def get_actions(self, departments_title):
        self.__connection()
        cursor = self.conn.cursor()
        cursor.execute(
            f"""
            SELECT Action.Title, Action.DESCRIPTION 
            FROM 
            Department JOIN Action 
            ON 
            Department.Department_ID = Action.Department_ID 
            WHERE Department.Title = \"{departments_title}\"
            ORDER BY Action.Title"""
        )
        results = cursor.fetchall()
        cursor.close()
        self.conn.close()
        return results


if __name__ == '__main__':
    MySqlite().add_days()
