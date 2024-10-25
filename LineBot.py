from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import configparser
import WeatherData

LineBot = Flask(__name__)

# LineBot info
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

# callback
@LineBot.route("/callback", methods = ['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text = True)
    LineBot.logger.info("Request body: " + body)
    
    try:
        print(body, signature)
        handler.handle(body, signature)
        
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# send weather data
@handler.add(MessageEvent, message = TextMessage)
def sendWeather(event):
    if(event.message.text == "天氣"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text = "_____及時天氣_____"  + WeatherData.mergeData())
        )

if __name__ == "__main__":
    LineBot.run()





    