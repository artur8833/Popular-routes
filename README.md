# Туристические маршруты


## Сборка репозитория и локальный запуск
Веб проект по агрегации популярных походных маршрутов для самостоятельных путешественников (в текущей версии был выбран кавказкий заповедник). Интересные места, а также места палаточных остановок, обозначаются на карте ввиде маркеров и всплывающих картинок.

#### Выполните в консоли:
~~~
git clone https://github.com/artur8833/Project_tourism.git
~~~

Создайте виртуальное окружение и установите зависимости:

~~~
python3 -m venv env
source env/bin/activate
pip install -r requirments.txt
~~~
#### Работа с базой данных:
~~~
export FLASK_APP=webapp
flask db upgrade
~~~

## Настройка
Создайте файл config.py и задайте в нем базовые переменные:
~~~
SQLALCHEMY_TRACK_MODIFICATIONS = False

WEATHER_DEFAULT_CITY = "Sochi,Russia"

WEATHER_API_KEY = "API ключ который вы получите после регистарации на сайте (https://www.worldweatheronline.com/)  "

WEATHER_URL = "http://api.worldweatheronline.com/premium/v1/weather.ashx"

SECRET_KEY = ""
~~~
## Запуск
Чтобы запустить, выполните в консоли:
~~~
Linux и Mac: (выполнить в консоли команду -
chmod +x run.sh - это сделает файл исполняемым).
После этого ввести в консоли ./run.sh
~~~
~~~
Windows: run.bat
~~~
