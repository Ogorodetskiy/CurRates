from sql_merge import currency_name_merge
import program_parameters as pp
from requests_exe import requests_cb_rf
import xml_parse


# Загрузка наименований валют
# данные грузятся в таблицу для импорта imp_cur_names
# данные по адресу https://cbr.ru/scripts/XML_val.asp?d=0
# https://cbr.ru/development/SXML/
def main():
    s_path = pp.parameters_str('CB_RF_ALL_CUR_NAMES')

    cur_list = xml_parse.currency_names(xml_parse.xml2tuple(xml=requests_cb_rf(s_path, {'d': '0'})))

    for i in cur_list:
        # itemID, cur_name, eng_name, nominal, parent_code

        currency_name_merge(i[0], i[1], i[2], i[3], i[4])


if __name__ == '__main__':
    main()
