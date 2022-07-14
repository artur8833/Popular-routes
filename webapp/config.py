import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'db.sqlite3')
SQLALCHEMY_TRACK_MODIFICATIONS = False
WEATHER_DEFAULT_CITY = "Sochi,Russia"
WEATHER_API_KEY = "55d82c1a6ba2440eb58133738220506"
WEATHER_URL = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
SECRET_KEY = "AWHDPDAIJWDIOJDsmakmksmcikejdfwejfunas_^##^@^5^35862135"