import os, time
import json
import requests
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from pathlib import Path


def dd_robot(msg):
    msg += "\n当前时间为：" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(msg)
    HEADERS = {"Content-Type": "application/json;charset=utf-8"}
    url = 换成自己的钉钉bot的url
    data_info = {
        "msgtype": "text",
        "text": {
        "content": "炉石" + msg
        },
        "isAtAll": False
    }

    value = json.dumps(data_info)
    requests.post(url,data=value,headers=HEADERS)

def read_json():
    f_dir = 自己的Battle.net.config路径
    contents = Path(f_dir).read_text()
    data = json.loads(contents)
    return data

def get_now_account():
    data = read_json()
    SavedAccountNames = str(data['Client']['SavedAccountNames']).split(',')
    return SavedAccountNames[0]

def main():
    command = r'.\lua53.exe "BNetSwitcher.lua"'
    os.system(command)
    os.system('taskkill /f /t /im "Battle.net.exe"')
    os.system('taskkill /f /t /im "Hearthstone.exe"')
    msg = "切换账号成功，当前账号为" + get_now_account()
    dd_robot(msg)


def test_main():
    msg = '测试'
    dd_robot(msg)
    main()

def test():
    dd_robot("")
    pass

if __name__ == '__main__':
    
    # test_main()
    dd_robot("脚本开启成功")
    
    scheduler = BlockingScheduler()
    scheduler.add_job(main, 'cron', hour=0)
    scheduler.add_job(main, 'cron', hour=12)
    scheduler.add_job(test, 'interval', hours=1)
    scheduler.start()
