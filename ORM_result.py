from sqlalchemy import create_engine, column, select, table, func

from program_parameters import db_path

engine = create_engine('sqlite:///'+db_path, echo=False)


def from_date(sdate):
    return sdate[6:10] + '-' + sdate[3:5] + '-' + sdate[0:2]


def parameters_str(s_code: str):
    """
    Функция возвращает значение параметра тип строка, с заданным кодом из таблицы parameters
    """

    prm = table("parameters", column("val_str"), column("code"))

    with engine.connect() as con:
        result = con.execute(select(prm.c.val_str).where((prm.c.code == s_code)))
        r = result.fetchone()

        return r[0] if r is not None else None


def parameters_num(s_code: str):
    """
    Функция возвращает значение параметра - Тип число, с заданным кодом из таблицы parameters
    """
    prm = table("parameters", column("val_num"), column("code"))

    with engine.connect() as con:
        result = con.execute(select(prm.c.val_num).where((prm.c.code == s_code)))
        r = result.fetchone()

        return r[0] if r is not None else None


def parameters_date(s_code: str):
    """
    Функция возвращает значение параметра тип - Дата, с заданным кодом из таблицы parameters
    В таблице параметров значения Дат хранятся в формате DD.MM.YYYY,  а вернуть мы должны в формате YYYY.MM.DD
    """
    prm = table("parameters", column("val_str"), column("code"))

    with engine.connect() as con:
        result = con.execute(select(prm.c.val_str).where((prm.c.code == s_code))).fetchone()

        return from_date(result[0]) if result is not None and len(result[0]) == 10 else None


def get_rn_by_code(table_name: str, scode: str):
    """
        Функция возвращает значение поля RN по значению поля code из заданной таблицы
    """

    prm = table(table_name, column("RN"), column("code"))

    with engine.connect() as con:

        result = con.execute(select(prm.c.RN).where((prm.c.code == scode))).fetchone()
        r = result

        return r[0] if r is not None else None


def curs_rate(nrate_types: int, currency: int, sdate: str):
    """
    Функция возвращает:
         курс  nrate_types, - exchange_rates_types.RN,
         валюты  currency,  - curnames.RN
         на дату sdate      - формат DD.MM.YYYY
    """
    ddate = from_date(sdate)

    print(ddate, nrate_types)

    # prm = table("imp_cur_rates", column("rn"), column("itemid"))

    return currency


def curs_rate_last_day(cur_type: str):

    """

    Функция возвращает: последний день когда есть данные о курсе с типом cur_type хотя бы по одной валюте

    """

    ntype = get_rn_by_code('exchange_rates_types', cur_type)

    prm = table('exchange_rates', column("rate_date"), column("rate_type"))

    with engine.connect() as con:

        max_rate_date = con.execute(select(func.max(prm.c.rate_date)).where((prm.c.rate_type == ntype))).fetchone()

        return max_rate_date[0] if max_rate_date is not None else None


if __name__ == '__main__':

    print(db_path)
    # print('Rn типа курса')
    print(get_rn_by_code('CURRENCY', 'RUB'))
    # print('Rn валюты')
    # print(get_rn_by_code('curnames', 'R01235'))

    # print(parameters_date('DATE_TEST'))

    # rate_types = get_rn_by_code('exchange_rates_types', 'CBRF')
    # currency1 = get_rn_by_code('curnames', 'R01235')
    # sdate1 = '17-03-2023'

    # print(curs_rate(rate_types, currency1, sdate1))

    # print(get_currency_rn('RUB'))

    # print(curs_rate_last_day('CBRF'))
