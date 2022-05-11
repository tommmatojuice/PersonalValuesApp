import sqlite3


class AppDataBase:

    def __init__(self):
        self.connection = sqlite3.connect('app_db.db')
        self.cursor = self.connection.cursor()
        self.create_db()

    def create_db(self):
        self.cursor.execute('''
          CREATE TABLE IF NOT EXISTS card (
          card_id INTEGER NOT NULL PRIMARY KEY,
          title TEXT NOT NULL)
          ''')

        self.cursor.execute('''
          CREATE TABLE IF NOT EXISTS user (
          user_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL)
          ''')

        self.cursor.execute('''
          CREATE TABLE IF NOT EXISTS result (
          result_id INTEGER NOT NULL PRIMARY KEY,
          date TEXT NOT NULL,
          user_id INTEGER NOT NULL,
          card_id INTEGER NOT NULL,
          FOREIGN KEY(user_id) REFERENCES user(user_id),
          FOREIGN KEY(card_id) REFERENCES card(card_id))
          ''')

        self.connection.commit()

    def inserts_card(self, card_id, title):
        self.cursor.execute(f'INSERT INTO card (card_id, title) VALUES ({card_id}, \'{title}\')')
        self.connection.commit()


if __name__ == '__main__':
    db = AppDataBase()
    db.create_db()
