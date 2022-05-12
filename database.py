import sqlite3
import pandas as pd


class AppDataBase:

    def __init__(self):
        self.connection = sqlite3.connect('app_db.db')
        self.cursor = self.connection.cursor()
        self.create_db()

    def create_db(self):
        # self.cursor.execute('''
        #   CREATE TABLE IF NOT EXISTS card (
        #   card_id INTEGER NOT NULL PRIMARY KEY,
        #   title TEXT NOT NULL,
        #   path TEXT NOT NULL)
        #   ''')

        self.cursor.execute('''
          CREATE TABLE IF NOT EXISTS user (
          user_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL)
          ''')

        # self.cursor.execute('''
        #   CREATE TABLE IF NOT EXISTS result (
        #   result_id INTEGER NOT NULL PRIMARY KEY,
        #   date TEXT NOT NULL,
        #   user_id INTEGER NOT NULL,
        #   card_id INTEGER NOT NULL,
        #   FOREIGN KEY(user_id) REFERENCES user(user_id),
        #   FOREIGN KEY(card_id) REFERENCES card(card_id))
        #   ''')

        self.cursor.execute('''
          CREATE TABLE IF NOT EXISTS result (
          result_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
          date TEXT NOT NULL,
          user_id INTEGER NOT NULL,
          card_path TEXT NOT NULL,
          FOREIGN KEY(user_id) REFERENCES user(user_id))
          ''')

        self.connection.commit()

    # def inserts_card(self, card_id, title, path):
    #     self.cursor.execute(f'INSERT INTO card (card_id, title, path) VALUES ({card_id}, \'{title}\', \'{path}\')')
    #     self.connection.commit()
    #
    # def select_card(self):
    #     self.cursor.execute('SELECT * FROM card')
    #     df = pd.DataFrame(self.cursor.fetchall(), columns=['card_id', 'title', 'path'])
    #     return df

    def insert_user(self, name):
        self.cursor.execute(f'INSERT INTO user (name) VALUES (\'{name}\')')
        self.connection.commit()
        return self.cursor.lastrowid

    def get_user_id(self, name):
        self.cursor.execute(f'SELECT user_id FROM user WHERE name=(\'{name}\')')
        res = self.cursor.fetchall()
        return res[0][0] if len(res) else None
        # return pd.DataFrame(self.cursor.fetchall(), columns=['user_id']).size == 0

    def insert_result(self, date, user_id, card_path):
        self.cursor.execute(f'''INSERT INTO result (date, user_id, card_path) 
VALUES (\'{date}\', {user_id},\'{card_path}\')''')
        self.connection.commit()

    def get_result(self, date, user):
        pass


