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
        </tr>
   </thead>
   <tbody>
       <tr>
          <td>1</td>
          <td>program_parametrs.py</td>
          <td>db_path</td>
         
  </tr>
</tbody>
</table>

Путь к базе данных хранится в файле program_parametrs.py   (передедать на yaml файл)
Путь к сервису хранится в самой базе данных в таблице parameters
