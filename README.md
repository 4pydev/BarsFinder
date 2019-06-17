# Bars Finder
Скрипт поможет Вам найти 5 ближайших московских бара.  
Вы сможете увидеть их на карте в браузере.


Список московских баров в формате JSON взят с сайта [data.mos.ru.](https://data.mos.ru)  
Файл с данными должен быть расположен в корне проекта и называться bars_data.json.

# Как запустить
Скрипт требует для своей работы установленного интерпретатора Python версии 3.5.  
Также потребуется установить необходимые библиотеки:
```bash
$ pip3 install -r requirements.txt
```
Запуск на Linux:
```bash
$ python3 ./bars_finder/main.py

Enter Your current location: Китай-город
```
Вам потребуется ввести свое местоположение, как в примере выше.  
  
Запуск скрипта сгенерирует в корневой директории файл bars.html.  
Чтобы увидеть расположение баров на карте выполните в терминале:
```bash
$ python3 ./bars_finder/flask_server.py
```
и затем откройте любой браузер и перейдите по адресу `0.0.0.0:5000`.

Запуск на Windows происходит аналогично.

# Цели проекта
Код создан в учебных целях. В рамках учебного курса по веб-разработке - DEVMAN.org