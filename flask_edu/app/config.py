SECRET_KEY='dev'

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'root'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'yang'

SQLALCHEMY_DATABASE_URI="{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)

MQTT_BROKER_URL = '127.0.0.1'
MQTT_BROKER_PORT = 1883
MQTT_USERNAME = 'yang'
MQTT_PASSWORD = 'yang'
MQTT_KEEPALIVE = 5
MQTT_TLS_ENABLED = False
MQTT_CLEAN_SESSION = True

SECRET_KEY = 'super-secret'