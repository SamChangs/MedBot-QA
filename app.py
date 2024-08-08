import os
from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
)
from models import Carousel_Msg
from linebot.models import MessageEvent, TextMessage, TemplateSendMessage, CarouselTemplate, CarouselColumn, MessageTemplateAction
app = Flask(__name__)

line_bot_api = LineBotApi(
    "2DgUJGlih3amAF11PlOMA40Ui6vMfKPi82RzNoe8WCbnXDcL1CBRzqC1lPutnTJgN6YFjw/znrBwBV+9Z3PXvTRC+9wATdvEG6gAT7dqtI20246/2Xii0IUJrgPrZQgDMdopOt8rZm6bwnmBe2SJkAdB04t89/1O/w1cDnyilFU="
)
handler = WebhookHandler("45659004fbf43da3501eba3dc1530ffb")

@app.route("/callback", methods=["POST"])
def callback():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print(
            "Invalid signature. Please check your channel access token/channel secret."
        )
        abort(400)

    return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token, TextSendMessage(text=event.message.text)
    )

# --------------------------------- 搜尋衛教園地----------------------------------
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_text = event.message.text.strip()
    if user_text == "衛教查詢":
        template_message = Carousel_Msg.Department_carousel_template()
    # elif user_text in carousel_templates:
    #     carousel_template = carousel_templates[user_text]
    #     template_message = TemplateSendMessage(
    #         alt_text=f'{user_text} 菜单',
    #         template=carousel_template
    #     )
        line_bot_api.reply_message(event.reply_token, template_message)
    # else:
    #     line_bot_api.reply_message(event.reply_token, TextSendMessage(text="抱歉，未找到相关信息。"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    # os.environ["PORT"]
