import configparser

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

    if __name__ == '__main__':
        create_config()