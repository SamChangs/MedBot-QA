import datetime
import json
import os
import re
import pymongo

###############################################################################
#                           LineBot衛教回復機器人mongoDB#                            #
###############################################################################
# 要讀取授權的Authentication Database認證資料庫
myclient = pymongo.MongoClient(
    f"mongodb+srv://khmina834156:As31186752@cluster0.bqth0.mongodb.net/"
)
user_db = myclient["Med-Bot"]
med_db = myclient["Ｍed-Data"]


def find_user(uid):
    # ... (判斷的程式碼)
    # 在判斷的程式碼後加入以下印出語句

    collect = user_db["lineuser"]
    cel = list(collect.find())

    ans = False
    for i in cel:
        if uid == i["uid"]:
            ans = True
    return ans


def write_user(nameid, uid, perm):
    collect = user_db["lineuser"]
    collect.insert_one(
        {
            "nameid": nameid,
            "uid": uid,
            "tr_mode": "N",
            "perm": int(perm),
            "my_medic": [],
            "date_info": datetime.datetime.utcnow(),
        }
    )
# 透過user_Id取得我的藥單陣列
def get_my_medic(uid):
    collect = user_db["lineuser"]
    user_data = collect.find_one({"uid": uid})
    my_medic = user_data.get("my_medic", [])
    medic_name_list = []

    for item in my_medic:
        medic_name = item.get("name")
        if medic_name:
            medic_name_list.append(medic_name)

    return medic_name_list