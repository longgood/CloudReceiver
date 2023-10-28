# -*- encoding: utf-8 -*-
"""
"""

from apps.receiver import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound
import json
import requests
import os
@blueprint.route('/receiver')
@login_required
def index():

    return render_template('receiver/index.html', segment='index')

@blueprint.route('/get_gait',methods=['POST'])
def get_gait():
    json_data = request.get_json()
    token="Ac69b674cCxj/6ej3j;6DCc623e2A"
    return process_data(json_data,token)
def process_data(json_data,token):
    # 解析 JSON 資料
    
    try:如果他就是一個dict
        token=data["Token"]
        print("真Dict:",token)
    except:
        print("no dict")
        pass
    try:
        data    =json.dumps(json_data)
        print("dumps, type:",type(data))
        print("content:",data)
        data = json.loads(data)
        print("type:",type(data))
    except:
        print("--failt to dump")
        pass
    try:
        data    =json.loads(json_data)
        print("loads, type:",type(data))
    except:
        print("--fail to load")
        pass
    # 檢查 Token 是否正確
    response = {"success":"false", "message":"Invalid token"}
    if "Token" in data:
        if data["Token"] != token:
            response = {"success":"false", "message":"Invalid token"}
        else:
            # 在這裡添加要處理 JSON 資料的程式碼
            data_processing(data)
            response = {"success":"true", "message":"上傳成功"}
        # 回傳處理結果
    
    return json.dumps(response)
from datetime import datetime
from apps.authentication.models import TEvent
def data_processing(data):
    fname_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    print("格式化時間:",fname_time)
    
    #---user---
    if "User" in data:
        print("使用者:",data["User"])
    #---activity---
    if "Activity" in data:
        print("活動:",data["Activity"])
    #---download data---
    score=0
    json_url=""
    raw_url=""
    if "Custom" in data:
        custom_data=data["Custom"]
        if "ExecutionLevel" in custom_data:
            score=custom_data["ExecutionLevel"]
        if "JsonFile" in custom_data:        
            json_url=custom_data["JsonFile"]
            download_files(json_url,fname_time,".json")
        if "RawFile" in custom_data:
            raw_url =custom_data["RawFile"]
            download_files(raw_url,fname_time,".csv.lzma")
    print("---需要紀錄到資料庫")
    event=TEvent()
    eventdic={"score":score,"json_file":fname_time+".json","raw_file":fname_time+".csv.lzma","startTime":fname_time}
    event.add_new(eventdic)

def download_files(url,fname,subname):
    filename = os.path.join("download_files",fname+subname)
    response = requests.get(url)
    if response.status_code == 200:  # 確認回應是否成功
        with open(filename, "wb") as f:
            f.write(response.content)
        print("下載完成！",url)
    else:
        print("下載失敗！",url)
        