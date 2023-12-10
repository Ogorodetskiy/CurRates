# Downloading the exchange rate from the website of the Central Bank of the Russian Federation and recording them in the Sqlite database:<br><br>Загрузка курса валют с сайта ЦБ РФ и запись их в базу данных Sqlite

## Purpose of the program<br><br>Назначение программы
Программа загружает все курсы валют, предоставляемых сервисом ЦБ РФ и записывает их в базу данных Sqlite
Является методом класса работы с валютами более крупной системы.

## Settings
ini file encoding="utf-8"
<table>
   <thead>
        <tr>
           <th>N</th>
           <th>section</th>
           <th>code</th>
           <th>description</th>
           <th>example</th>
        </tr>
   </thead>
   <tbody>
       <tr>
          <td>1</td>
          <td>DB</td>
          <td>db_path</td>
          <td>the path to the database</td>
          <td>D:\\MY_SCRIPTS\\_CurRate_2023\\DB\\CURRENCY.db</td>
         
  </tr>
   <tr>
          <td>2</td>
          <td>DB</td>
          <td>engine</td>
          <td>database management system (DBMS)</td>
          <td>sqlite:///</td>
         
  </tr>
  <tr>
          <td>3</td>
          <td>Program</td>
          <td>path</td>
          <td>The path to the database</td>
          <td>D:\MY_SCRIPTS\_CurRate_2023\</td>
         
  </tr>
 <tr>
          <td>4</td>
          <td>Program</td>
          <td>file_currencv_names</td>
          <td>The path to the file from which the currency names are loaded</td>
          <td>Справочник валют.txt</td>
         
  </tr>
  
</tbody>
</table>


## Structure

### Layer1 (http)
request_exe.py (получение ответа от сервиса) 

### Layer2 (converting the response to the python type)
xml_parse.py  преобразование XML, произвольной формы, к типу tuple (кортеж)

### layer3 (SQL)
sql_native.py  (nativ SQL)<br>
ORM_result.py (SQLAlchemy 2.0)






