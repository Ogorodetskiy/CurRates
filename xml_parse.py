import xml.etree.ElementTree as Et


def xml2tuple(xml='', s_path=''):
    """
    Преобразование XML словарь
    Либо передаем непосредственно XML файл, если ранее получили его сами, например из интернета
    либо путь по которому лежит XML файл вместе с его именем
    """
    dict_all = {}

    if xml == '':

        tree = Et.parse(s_path)  # Берем из файла
        root = tree.getroot()
        print("Взято из файла")
    else:
        root = Et.fromstring(xml)  # Передали сам XML

    for child in root:

        dict_one = {}
        for ev in child:

            dict_one[ev.tag] = ev.text

        ind = child.attrib.popitem()[1]

        dict_all[ind] = dict_one

    return dict_all.items()


def currency_names(dict_cn):
    lis_cn = list()
    for j in dict_cn:
        lis_cn.append([j[0],
                       j[1]['Name'],
                       j[1]['EngName'],
                       j[1]['Nominal'],
                       j[1]['ParentCode'].strip() if j[0].strip() != j[1]['ParentCode'].strip() else ''])
    return lis_cn


def currency_rates(dict_cn):
    lis_cn = list()
    for j in dict_cn:
        lis_cn.append([j[0],
                       j[1]['NumCode'],
                       j[1]['CharCode'],
                       j[1]['Nominal'],
                       j[1]['Name'],
                       j[1]['Value']
                       ])
    return lis_cn


if __name__ == '__main__':

    s_path_tmp = 'D:\\MY_SCRIPTS\\_CurRate\\Справочник валют.txt'
    print('_______________ Печать из модуля  ____________________')

    for i in xml2tuple('', s_path_tmp):
        print(i[0], i[1]['Name'], i[1]['EngName'], i[1]['Nominal'],
              i[1]['ParentCode'].strip() if i[0].strip() != i[1]['ParentCode'].strip() else '', sep=",")

    """
    s_path_tmp = 'D:\\MY_SCRIPTS\\_CurRate\\Курс на день.txt'
    print('_______________ Печать из модуля  ____________________')
    # R01820 {'NumCode': '392', 'CharCode': 'JPY', 'Nominal': '100', 'Name': 'Японских иен', 'Value': '55,3049'}
    for i in xml2tuple(s_path_tmp):
        print(i[0], i[1]['NumCode'], i[1]['CharCode'], i[1]['Nominal'], i[1]['Name'],  i[1]['Value'])
    """