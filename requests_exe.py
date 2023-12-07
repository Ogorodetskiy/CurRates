import requests


def requests_cb_rf(s_path, params_dict):

    """
        Возвращает XML с сайта s_path, параметрами   params_dict
    """

    try:

        r = requests.get(s_path, params_dict)

        if r.status_code != 200:
            print(f'Не удалось получить данные по адресу . Код ошибки: {r.status_code}')
            r.text = 'error'

        return r.text

    except Exception as ex:

        print("Error from response: ", f"{ex}")


if __name__ == '__main__':
    from program_parameters import parameters_str

    print(requests_cb_rf(parameters_str('CB_RF_ALL_CUR_RATES_DAILY'), {'date_req': '20/02/2023'}))
