#!/usr/bin/env python3.6
#coding=utf8
import requests
import itchat

KEY = '输入图灵机器人密钥'

flag = False
stop_reply=False
default_text="你好，本人不在。联系我请直接拨打电话。或者等本人上线后回复。\n电话号码：110" \
             "\n如果想继续聊天请回复12138进入聊天机器人系统。回复666退出聊天。\n" \
             "祝你愉快！  ————来自otote"
def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    global flag
    global stop_reply
    oldflag=flag
    # defaultReply = 'I received: ' + msg.text
    global default_text
    reply = get_response(msg.text)
    # return reply or defaultReply
    if msg.text=="12138":
        flag=True
    elif msg.text=="666":
        flag=False
    elif msg.text == "启动机器人":
        stop_reply = False
    elif msg.text == "停止机器人":
        stop_reply = True

    if not stop_reply:
        if flag :
            if not oldflag:
                return "我们可以开始聊天了。"
            else:
                return reply+"\n\t\t————来自机器人\n退出机器人请回复666"
        else:
            return default_text
        # return reply or test

@itchat.msg_register(itchat.content.RECORDING)#语音消息
def voice_reply(msg):
    return tuling_reply(msg)

itchat.auto_login(enableCmdQR=2,hotReload=True)
#itchat.auto_login(hotReload=True)


itchat.run()

# nohup python run.py    #linux后台自动运行