from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======這裡是呼叫的檔案內容=====
from message import *
#from new import *
#from Function import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('你的Channel AcessToken')
# Channel Secret
handler = WebhookHandler('你的Channel Secret')


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    #[學生改]可以改你要偵測的字詞
    if '協力廠商' in msg: #當使用者在群組輸入[協力廠商]字樣 
        message = imagemap_message()
        line_bot_api.reply_message(event.reply_token, message)
    #[學生改]可以改你要偵測的字詞
    elif '關於本企業' in msg:#當使用者在群組輸入[關於本企業]字樣
        message = buttons_message()
        line_bot_api.reply_message(event.reply_token, message)
    #[學生改]可以改你要偵測的字詞    
    elif '功能列表' in msg:#當使用者在群組輸入[功能列表]字樣
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
    #[學生改]可以改你要偵測的字詞    
    elif '產品資訊' in msg: #當使用者在群組輸入[產品資訊]字樣
        message = image_carousel_message1#test()
        line_bot_api.reply_message(event.reply_token, message)
    else:
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)

@handler.add(PostbackEvent)
def handle_message(event):
    print(event.postback.data)


@handler.add(MemberJoinedEvent)
def welcome(event):
    uid = event.joined.members[0].user_id
    gid = event.source.group_id
    profile = line_bot_api.get_group_member_profile(gid, uid)
    name = profile.display_name
    message = TextSendMessage(text=f'{name}歡迎加入')
    line_bot_api.reply_message(event.reply_token, message)
        
        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
