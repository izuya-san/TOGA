# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open('{}/SUMI/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]

class Config(object):
    #dont change
    LOGGER=True
    URL=False
    ALLOW_CHATS=True
    ALLOW_EXCL=False
    TEMP_DOWNLOAD_DIRECTORY=""
    DEL_CMDS=False
    BAN_STICKER="kans"
    CERT_PATH=""
    PORT=8443
    WORKERS=8
    LOAD=""
    NO_LOAD="translation"
    MONGO_DB="YourPervertSenpai"
    WEBHOOK=False
    BOT_API_URL="https://api.telegram.org/bot"
    
    #change
    WOLVES=[]
    BOT_ID="5493514510" 
    SQLALCHEMY_DATABASE_URI="postgres://togasql:Toga12345@togamain.ca0im984bj3g.us-east-1.rds.amazonaws.com:5432/togalol" 
    JOIN_LOGGER="-1001548936254" 
    API_HASH="7c160052c4c6af647e5cc17e5b89a22e" 
    ARQ_API_URL="arq.hamker.dev"
    GENIUS_API_TOKEN="agjwjspa" 
    INFOPIC=True
    TIGERS=[5121126855, 1852772237]
    API_ID="17750703"
    BL_CHATS=[1]
    DB_URL2="xiyivexr" 
    TOKEN="5493514510:AAG6KZ74d3gf6nfuxP5HPv4YyOO1Qo7G3c8"
    DEV_USERS=[5214808179, 5589385763]
    DRAGONS=[1486727193, 1762600440, 1122860241, 2093473332]
    SPAMWATCH_API="J968E_20LgxrKj0sIDBG~YqN2NRTbU"
    WALL_API="2455acab48f3a935a8e703e54e26d121" #gift from meow
    DEMONS=[5587802538, 5395870942, 1005344893, 5591566214, 2025995896, 5205602399, 5266361550, 2039336161, 5555455171, 5435686540, 5500575469, 1160126059, 1642721989, 5738696210, 1843037755, 1295698776]
    SUPPORT_CHAT="TogaSupport"
    OWNER_USERNAME="izuya"
    DONATION_LINK="https://www.paypal.me/PaulSonOfLars"
    EVENT_LOGS="-1001548936254" 
    OWNER_ID="5163444566" 
    TIME_API_KEY="" #gift from meow
    ERROR_LOGS="-1001417928763" 
    BOT_NAME="toga_robot"
    STRICT_GBAN=True
    REDIS_URL="redis://YourPervertSenpai:Hrituzee123+@redis-14816.c15.us-east-1-2.ec2.cloud.redislabs.com:14816/Kac-free-db"
    ARQ_API_KEY="CZGPYC-SCMRAI-EKQNGY-ZRFYGZ-ARQ"
    UPDATE_CHANNEL="AnicadeUpdates"
    MONGO_DB_URI="mongodb+srv://YourPervertSenpai:Hrituzee123@kacchan.ikpgw.mongodb.net/?retryWrites=true&w=majority"
    BOT_USERNAME="Toga_Robot"
    REM_BG_API_KEY="K2Rc"
    CASH_API_KEY=""
    AI_API_KEY=""
    SPAMWATCH_SUPPORT_CHAT="SpamWatchSupport"
    OPENWEATHERMAP_ID=""
    LOG_GROUP_ID="-1001417928763"
    STRICT_GMUTE=False
    NETWORK_USERNAME="Anicademia"
    NETWORK_NAME="Anicade"
    AFKVID=""
    GROUP_ALIVE_PIC=""
    SUMI_STATS_PIC=""
    SUMI_WELCOME=""
    SUMI_OWNER_WEL_IMG=""
    SUMI_DISPACHER_PIC=""
    SUMI_HELP_PIC=""
    PM_IMAGE=""
    GROUPSTART_VID=""
    SUMI_DIS_WEL=""
    SPAMWATCH_API="9x__eKEBWQFj~t~zgUWkSk8BWSsWYaAcDWFEITQX1eKNd3CswakpUVYGt5hcH06n"
    HEROKU_APP_NAME = ""
    HEROKU_API_KEY = ""
    OWNER_NAME = "izuya"
    COTB = "izuya"
    BANCODES = ""
    REPOSITORY = "GitHub.com/izuya-san/suguha"
    RED7_TOKEN = "RED7-z0pc44m5mf8v8bjdwq8g2"

class Production(Config):
    LOGGER=True


class Development(Config):
    LOGGER=True
