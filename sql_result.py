import sqlite3
import program_parameters as pp

try:
    db_path = pp.db_path

    conn = sqlite3.connect(db_path)
    print(f"База данных {db_path} успешно подключена к SQLite")

except sqlite3.Error as error:
    print(f"Ошибка при подключении к sqlite базы данных {db_path}", error)

cursor = conn.cursor()


def currency_rn(itemid):
    # Найдем RN валюты
    var_list_s = (itemid,)

    sqlite_sel_type = """SELECT t.rn from curnames t
           where t.code = ?"""

    cursor.execute(sqlite_sel_type, var_list_s)

    rn = cursor.fetchone()

    return rn[0] if rn is not None else None


if __name__ == '__main__':

    print(currency_rn('CBRF'))
    if conn:
        conn.close()
        print("Соединение с SQLite закрыто")
