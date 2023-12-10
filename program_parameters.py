from configparser import ConfigParser

from sqlalchemy import create_engine, column, table
import configparser


db_path = 'D:\\MY_SCRIPTS\\_CurRate_2023\\DB\\CURRENCY.db'
path_main = 'D:\\MY_SCRIPTS\\_CurRate_2023\\'
file_cur_name = 'Справочник валют.txt'

engine = create_engine('sqlite:///'+db_path)
prm = table("parameters", column("val_str"), column("code"))


def read_config():
    my_config = configparser.ConfigParser()
    my_config.read('currate_settings.ini', encoding="utf-8")
    return my_config


def create_config():
    print('Создание модуля хранения пользовательских параметров')
    # https://www.c-sharpcorner.com/article/configuration-files-in-python/

    # CREATE OBJECT
    config_file = configparser.ConfigParser()

    # ADD SECTION
    config_file.add_section("DB")
    config_file.add_section("Program")
    # ADD SETTINGS TO SECTION
    config_file.set("DB", "db_path", "D:\\MY_SCRIPTS\\_CurRate_2023\\DB\\CURRENCY.db")
    config_file.set("DB", "engine", "sqlite:///")

    config_file.set("Program", "path", "D:\\MY_SCRIPTS\\_CurRate_2023\\")
    config_file.set("Program", "file_currencv_names", "'Справочник валют.txt'")

    # SAVE CONFIG FILE
    with open(r"currate_settings.ini", 'w', encoding="utf-8") as configfileObj:
        config_file.write(configfileObj)
        configfileObj.flush()
        configfileObj.close()

    print("Config file 'configurations.ini' created")

def load_config_one_prm(section, code):
    return config[section][code]


if __name__ == '__main__':
    # Создаем первоначальный ini файл
    create_config()

    config = read_config()

    db_path1 = config["DB"]["db_path"]
    file_name = config["Program"]["file_currencv_names"]

    print(load_config_one_prm('DB', 'db_path'), file_name)
