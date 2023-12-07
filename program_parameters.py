from sqlalchemy import create_engine, column, select, table
db_path = 'D:\\MY_SCRIPTS\\_CurRate_2023\\DB\\CURRENCY.db'
path_main = 'D:\\MY_SCRIPTS\\_CurRate_2023\\'
file_cur_name = 'Справочник валют.txt'

engine = create_engine('sqlite:///'+db_path)
prm = table("parameters", column("val_str"), column("code"))


def parameters_str(s_code: str):
    """
    Функция возвращает значение строкового параметра с заданным кодом из таблицы parameters
    """
    with engine.connect() as con:
        result = con.execute(select(prm.c.val_str).where((prm.c.code == s_code)))

        return result.fetchone()[0]


if __name__ == '__main__':
    print('Модуль хранения пользовательских параметров')
    print(parameters_str('CB_RF_ALL_CUR_NAMES'))
