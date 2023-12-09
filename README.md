# Downloading the exchange rate from the website of the Central Bank of the Russian Federation and recording them in the Sqlite database:<br><br>Загрузка курса валют с сайта ЦБ РФ и запись их в базу данных Sqlite

## Purpose of the program<br><br>Назначение программы
Программа загружает все курсы валют, предоставляемых сервисом ЦБ РФ и записывает их в базу данных Sqlite
Является методом класса работы с валютами более крупной системы.

## Settings
Таблица настроек
<table>
   <thead>
        <tr>
           <th>N</th>
           <th>sourcer</th>
           <th>parametr</th>
           <th>description</th>
           <th>example</th>
        </tr>
   </thead>
   <tbody>
       <tr>
          <td>1</td>
          <td>program_parametrs.py</td>
          <td>db_path</td>
          <td>the path to the database</td>
          <td>D:\\MY_SCRIPTS\\_CurRate_2023\\DB\\CURRENCY.db</td>
         
  </tr>
   <tr>
          <td>2</td>
          <td>CURRENCY.parameters</td>
          <td>CB_RF_ALL_CUR_RATES_DAILY</td>
          <td>the address for receiving the exchange rates of all currencies on a certain day</td>
          <td>https://cbr.ru/scripts/XML_daily.asp</td>
         
  </tr>
  <tr>
          <td>3</td>
          <td>CURRENCY.parameters</td>
          <td>CB_RF_ONE_CUR_RATE</td>
          <td>The address for receiving the exchange rates of a specific currency for the period</td>
          <td>https://cbr.ru/scripts/XML_dynamic.asp</td>
         
  </tr>
</tbody>
</table>

Путь к базе данных хранится в файле program_parametrs.py   (передедать на yaml файл)<br>
Путь к сервису хранится в самой базе данных в таблице parameters

## Structure

### Layer1 (http)
request_exe.py (получение ответа от сервиса) 

### Layer2 (converting the response to the python type)
xml_parse  преобразование XML, произвольной формы, к типу tuple (кортеж)

### layer3 (SQL)
sql_native.py  (nativ SQL)
ORM_result.py (SQLAlchemy 2.0)






