from sqlalchemy import create_engine, column, select, table
db_path = 'D:\\MY_SCRIPTS\\_CurRate_2023\\DB\\CURRENCY.db'
path_main = 'D:\\MY_SCRIPTS\\_CurRate_2023\\'
file_cur_name = 'Справочник валют.txt'

engine = create_engine('sqlite:///'+db_path)
prm = table("parameters", column("val_str"), column("code"))




if __name__ == '__main__':
    print('Модуль хранения пользовательских параметров')
    #print(parameters_str('CB_RF_ALL_CUR_NAMES'))
