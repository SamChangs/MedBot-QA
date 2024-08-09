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
from linebot.models import (
    MessageEvent,
    TextMessage,
    TemplateSendMessage,
    CarouselTemplate,
    CarouselColumn,
    MessageTemplateAction,
)

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
    topic_name_list = ["一般照護", "心臟血管疾病", "手術相關", "牙科", "出院準備", "外科", "外語護理指導", "皮膚疾病", "耳鼻喉疾病", "血液腫瘤", "肝膽疾病", "兒科疾病", "泌尿疾病", "肺部、胸腔疾病", "侵入性檢查相關","急診相關", "重症加護", "骨科疾病", "健康保健", "產科、婦科疾病","腎臟疾病", "感染疾病", "腸胃疾病", "腦神經系統疾病", "精神科疾病","糖尿病疾病", "營養衛教單張", "癌症相關", "醫療美容"]
    topic_name_list_en = ["General Care", "Cardiovascular", "Surgery", "Dentistry", "Discharge Prep", "Surgery Info", "Nursing Guides", "Skin Diseases", "ENT Issues", "Blood Cancer", "Liver Disorders", "Pediatric Care", "Urology", "Lung/Chest Issues", "Invasive Exams","Emergency Care", "ICU Care", "Orthopedics", "Health Care", "OB/GYN Care","Kidney Issues", "Infectious Diseases", "GI Disorders", "Neurological", "Mental Health","Diabetes", "Nutrition Info", "Cancer Info", "Cosmetic Care"]
    
    
    user_text = event.message.text.strip()
    if user_text == "衛教查詢":
        template_message = Carousel_Msg.information_carousel_template()
    elif user_text in topic_name_list:
        template_message = Carousel_Msg.info_topic_carousel_template(user_text)
    elif user_text == "Health Inquiry":
        template_message = Carousel_Msg.information_carousel_template_en()
    elif user_text == "Tanya Kesehatan":
        template_message = Carousel_Msg.information_carousel_template_idn()
    elif user_text == "Tư vấn Y tế":
        template_message = Carousel_Msg.information_carousel_template_vn()
    elif user_text == "สอบถามสุขภาพ":
        template_message = Carousel_Msg.information_carousel_template_th()
    

    line_bot_api.reply_message(event.reply_token, template_message)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    # os.environ["PORT"]
