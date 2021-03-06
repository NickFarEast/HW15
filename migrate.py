import sqlite3
from os.path import join, isfile

DATABASE_PATH = 'animal.db'
SQL_DIR_PAS = 'sql'
INIT_MIGRATION_FILE_PATH = 'init.sql'


def get_sql_from_file(file_name):
    """

    :param file_name:
    :return:
    """
    content = ''
    if isfile(file_name):
        with open(file_name) as file:
            content = file.read()
    return content


def main():
    """

    :return:
    """
    con = sqlite3.connect(DATABASE_PATH)
    cur = con.cursor()

    sql = get_sql_from_file(join(SQL_DIR_PAS, INIT_MIGRATION_FILE_PATH))

    cur.executescript(sql)

    cur.close()
    con.close()


if __name__ == '__main__':
    main()
