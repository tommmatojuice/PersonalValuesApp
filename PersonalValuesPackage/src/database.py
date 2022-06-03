import sqlite3
import pandas as pd


class AppDataBase:
    """
    Class describes the database of application
    """

    def __init__(self):
        """
        Initializing a connection to database
        """
        self.connection = sqlite3.connect('app_db.db')
        self.cursor = self.connection.cursor()
        self.create_db()

    def create_db(self):
        """
        Creating tables in database:

        :return: None
        """
        self.cursor.execute('''
          CREATE TABLE IF NOT EXISTS user (
          user_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL)
          ''')

        self.cursor.execute('''
          CREATE TABLE IF NOT EXISTS result (
          result_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
          date TEXT NOT NULL,
          user_id INTEGER NOT NULL,
          card_path TEXT NOT NULL,
          FOREIGN KEY(user_id) REFERENCES user(user_id))
          ''')

        self.connection.commit()

    def insert_user(self, name):
        """
        Inserting new user to table "user":

        :param name: user name

        :return: last added user_id
        """
        self.cursor.execute(f'INSERT INTO user (name) VALUES (\'{name}\')')
        self.connection.commit()
        return self.cursor.lastrowid

    def get_user_id(self, name):
        """
        Getting user id by:

        :param name: user name

        :return:None
        """
        self.cursor.execute(f'SELECT user_id FROM user WHERE name=(\'{name}\')')
        res = self.cursor.fetchall()
        return res[0][0] if len(res) else None

    def insert_result(self, date, user_id, card_path):
        """
        Inserting result of user test in table "result":

        :param date: date of passing test
        :param user_id: user ID
        :param card_path: path to card with value

        :return: None
        """
        self.cursor.execute(f'''INSERT INTO result (date, user_id, card_path) 
VALUES (\'{date}\', {user_id},\'{card_path}\')''')
        self.connection.commit()

    def get_all_saver(self):
        """
        Getting all unique saves:

        :return: DataFrame with result table
        """
        self.cursor.execute('''SELECT DISTINCT user.user_id, name, date FROM result 
JOIN user ON user.user_id = result.user_id
ORDER BY date DESC''')
        df = pd.DataFrame(self.cursor.fetchall(), columns=['user_id', 'name', 'date'])
        return df

    def get_save(self, name, date):
        """
        Getting save of user result by date and name:

        :param name: user name
        :param date: date of test

        :return: DataFrame with result table
        """
        self.cursor.execute(f'''select DISTINCT card_path, name, date from result 
join user on user.user_id = result.user_id where 
name = \'{name}\' and date = \'{date}\'''')
        df = pd.DataFrame(self.cursor.fetchall(), columns=['card_path', 'name', 'date'])
        return df
