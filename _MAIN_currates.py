from xml_parse import xml2tuple, currency_rates

from requests_exe import get_answer
from sql_native import currency_rate_merge, clear_temp_table, exchange_rates_transfer as ert

from ORM_result import parameters_str as pps, get_rn_by_code, curs_rate_last_day

from datetime import timedelta
from datetime import datetime


# Загрузка курсов всех валют с сайта ЦБ на заданную дату
# пример запроса  http://www.cbr.ru/scripts/XML_daily.asp?date_req=02/03/2002
# пример всех запросов https://cbr.ru/development/SXML/


def main(s_date: str, cur_type: str):
    """
    Строка s_date Дата в формате dd/mm/yyyy
    """

    if cur_type == 'CBRF':
        s_path = pps('CB_RF_ALL_CUR_RATES_DAILY')
        cur_list = currency_rates(xml2tuple(xml=get_answer(s_path, {'date_req': s_date})))

        # Найдем курс валюты номинала - RUB
        nom_currency = get_rn_by_code('CURNAMES', 'RUB')

    else:
        print(f'Для типа курса {cur_type} загрузка еще не описана!')
        return

    clear_temp_table()

    for i in cur_list:

        # Запишем полученное из сервиса во временную таблицу
        currency_rate_merge(i[0], i[1], i[2], i[3], i[4], i[5], s_date, nom_currency)

    # Перенесем данные в рабочую таблицу

    ert(cur_type)


def main_period(date_beg: str, date_end: str, cur_type: str):

    d1 = datetime.strptime(date_beg, '%d/%m/%Y')
    d2 = datetime.strptime(date_end, '%d/%m/%Y')

    delta = (d2 - d1).days+1

    for i in range(delta):

        main(s_date=(d1 + timedelta(days=i)).strftime("%d/%m/%Y"), cur_type=cur_type)


def main_until_current_date(cur_type: str):

    d1 = curs_rate_last_day(cur_type)
    sd1 = d1[8:10] + '/' + d1[5:7] + '/' + d1[0:4]  # строка последний загруженный курс
    sd2 = datetime.today().strftime('%d/%m/%Y')  # строка сегодняшнее число

    if sd1 == sd2:
        print(f'\033[34mКурсы на дату\033[31m {sd1} \033[34mуже загружены')
    else:
        main_period(sd1, sd2, cur_type)


if __name__ == '__main__':
    # Дату передаем в формате DD.MM.YYYY
    # main_period('01/03/2023', '30/03/2023', 'CBRF')
    # main_period()
    # text = 'Привет мир'
    # print("\033[31m{}".format(text)) # Красный текст только в windows

    main_until_current_date('CBRF')
