from configparser import ConfigParser

"""
db_path = 'D:\\MY_SCRIPTS\\_CurRate_2023\\DB\\CURRENCY.db'
path_main = 'D:\\MY_SCRIPTS\\_CurRate_2023\\'
file_cur_name = 'Справочник валют.txt'

engine = create_engine('sqlite:///'+db_path)
prm = table("parameters", column("val_str"), column("code"))
"""


def read_config():
    my_config = ConfigParser()
    my_config.read('currate_settings.ini', encoding="utf-8")
    return my_config


def load_config_one_prm(section, code):
    config = read_config()
    return config[section][code]


if __name__ == '__main__':
    # Создаем первоначальный ini файл
    """
    create_config()

    config = read_config()

    db_path1 = config["DB"]["db_path"]
    file_name = config["Program"]["file_currencv_names"]
"""
    print(load_config_one_prm('DB', 'db_path'))
