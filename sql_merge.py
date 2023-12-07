import sqlite3
import program_parameters as pp
from ORM_result import from_date, get_rn_by_code

try:
    db_path = pp.db_path

    conn = sqlite3.connect(db_path)
    print(f"База данных {db_path} успешно подключена к SQLite")

except sqlite3.Error as error:
    print(f"Ошибка при подключении к sqlite базы данных {db_path}", error)

cursor = conn.cursor()


def clear_temp_table():
    
    # Очистим таблицу загрузки

    cursor.execute('delete from imp_cur_rates')


def currency_name_merge(itemid, cur_name, eng_name, nominal, parent_code):

    # формируем список для запроса наличия валюты с заданным кодом
    var_list_s = (itemid, )

    sqlite_select_query = """select 1
                               from imp_cur_names t
                              where t.itemid = ?"""
    sqlite_insert_query = """INSERT into imp_cur_names 
                  (itemid, name, engname, nominal, parentcode)
           VALUES (?, ?, ?, ?, ?)"""
    
    cursor.execute(sqlite_select_query, var_list_s)
    records = cursor.fetchall()

    if not len(records):
        # такой валюты нет, добавляем
        cursor.execute(sqlite_insert_query,
                       (itemid, cur_name, eng_name, nominal,  parent_code))
        print(itemid)

    conn.commit()


def currency_rate_merge(itemid, numcode, charcode, nominal, name, value, date_value, nnom_currency):

    # Записываем полученные данные во временную таблицу tmp_imp_cur_rates
    sqlite_insert_query = """INSERT into imp_cur_rates 
                          (itemid, numcode, charcode, nominal, name, value, date_value, nom_currency )
                   VALUES (?, ?, ?,?, ? ,?, ?, ?)"""

    cursor.execute(sqlite_insert_query,
                   (itemid, numcode, charcode, nominal, name, value.replace(',', '.'), from_date(date_value), nnom_currency ))

    conn.commit()


def exchange_rates_transfer(srate_type: str):

    nrate_type = get_rn_by_code(table_name='exchange_rates_types', scode=srate_type)

    # Перенос данных из временной таблицы imp_cur_rates в рабочую таблицу  exchange_rates
    sql_transfer = """insert into exchange_rates(rate_date, rate_type, currency, nominal, curval)
                       select t.date_value, 1, cn.rn, t.nominal, t.value
                         from imp_cur_rates t
                         join curnames cn on cn.code = t.itemid
                         left join exchange_rates ex on ex.currency = cn.rn 
                                                     and t.date_value = ex.rate_date 
                                                     and ex.rate_type = ?
                       where ex.rn is null"""

    cursor.execute(sql_transfer, (nrate_type,))

    conn.commit()


if __name__ == '__main__':

    exchange_rates_transfer('CBRF')

    if conn:
        conn.close()
        print("Соединение с SQLite закрыто")
