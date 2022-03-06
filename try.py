#用于测设和放一些奇奇怪怪的东西
import re,json,datetime,requests,encodings,os,weather,random
from multiprocessing import Process
from flask import Flask
from flask import request
import function,Baidu_Text_transAPI

def send_private_msg(user_id, message, group_id='', auto_escape='False'):
    user_id = str(user_id)
    message = str(message)
    group_id = str(group_id)
    if group_id == '':  # 私聊
        sand_message_user = "http://127.0.0.1:5700/" + "send_private_msg?" + "user_id=" + user_id + "&" + "message=" + message + "&" + "auto_ecscape=" + auto_escape
        return_user = requests.post(sand_message_user)
    else:  # 通过群发
        sand_message_user = "http://127.0.0.1:5700/" + "send_private_msg?" + "user_id=" + user_id + "&" + "group_id=" + group_id + "&" + "message=" + message + "&" + "auto_ecscape=" + auto_escape
        return_user = requests.post(sand_message_user)
    return return_user


# 发送群信息
def send_group_msg(group_id, message, auto_escape=''):
    group_id = str(group_id)
    message = str(message)
    sand_message_user = "http://127.0.0.1:5700/" + "send_group_msg?" + "group_id=" + group_id + "&" + "message=" + message + "&" + "auto_ecscape=" + auto_escape
    return_user = requests.post(sand_message_user)
    return return_user


# 发送合并转发 ( 群 )
def send_group_forward_msg(group_id, messages):
    sand_message_user = "http://127.0.0.1:5700/" + "send_group_forward_msg?" + "group_id=" + group_id + "&" + "message=" + messages


# 发送消息
# TODO 发送信息还在写
def send_msg(message,user_id='', group_id='', message_type='', auto_escape=''):
    #sand_message_user =
    pass



# 撤回消息
def delete_msg(message_id):
    sand_message_user = "http://127.0.0.1:5700/" + "delete_msg?" + "message_id=" + message_id
    return_user = requests.post(sand_message_user)
    return return_user


# 获取消息
def get_msg(message_id):
    sand_message_user = "http://127.0.0.1:5700/" + "set_group_kick?" + "message_id=" + message_id
    return_user = requests.post(sand_message_user)
    return return_user
    # 这里是json信息，需要解析


"""
响应数据
字段	类型	说明
message_id	int32	消息id
real_id	int32	消息真实id
sender	object	发送者
time	int32	发送时间
message	message	消息内容
raw_message	message	原始消息内容
"""


# 获取合并转发内容
def get_forward_msg(message_id):
    sand_message_user = "http://127.0.0.1:5700/" + "get_forward_msg?" + "message_id=" + message_id
    return_user = requests.post(sand_message_user)
    return return_user
    # 此处同上


# 获取图片信息
def get_image(file):
    sand_message_user = "http://127.0.0.1:5700/" + "get_image?" + "file=" + file
    return_user = requests.post(sand_message_user)
    return return_user


# 群组踢人
def set_group_kick(group_id, user_id, reject_add_request='false'):
    sand_message_user = "http://127.0.0.1:5700/" + "set_group_kick?" + "group_if=" + group_id + "&" + "user_id=" + user_id + "&" + "reject_add_request=" + reject_add_request
    return_user = requests.post(sand_message_user)
    return return_user


# 群组单人禁言
def set_group_ban(group_id, user_id, duration='30 * 60'):  # 最后一个参数为禁言时间，单位s，0秒表示取消禁言
    sand_message_user = "http://127.0.0.1:5700/" + "set_group_ban?" + "group_id=" + group_id + "&" + "user_id=" + user_id + "&" + "duration=" + duration
    return_user = requests.post(sand_message_user)
    # 无响应数据

#晚间10：00报时加天气预报
def weather_sand(user_id, message, group_id='', auto_escape='False'):
    message = weather.return_main()
    user_id = str(user_id)
    message = str(message)
    group_id = str(group_id)
    if group_id == '':  # 私聊
        sand_message_user = "http://127.0.0.1:5700/" + "send_private_msg?" + "user_id=" + user_id + "&" + "message=" + message + "&" + "auto_ecscape=" + auto_escape
        return_user = requests.post(sand_message_user)
    else:  # 通过群发
        sand_message_user = "http://127.0.0.1:5700/" + "send_private_msg?" + "user_id=" + user_id + "&" + "group_id=" + group_id + "&" + "message=" + message + "&" + "auto_ecscape=" + auto_escape
        return_user = requests.post(sand_message_user)
    return return_user

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello_world():
    global time_i
    main_into = request.json
    post_type = main_into["post_type"]
    if post_type == "message":
        function.log_in(str(main_into))
        message_input = main_into["message"]
        message_type = main_into["message_type"]
        check = str(filter(main_into, message_type))
        with open('json__/main.json', 'r', encoding='utf-8') as main_json:
            main_json_0 = json.load(main_json)
            for key_0 in main_json_0:
                value_0 = main_json_0[key_0]
                if "g" in key_0:
                    mode_0 = value_0["mode"]
                    type_0 = mode_0["type"]
                    get_msg_0 = value_0["get_msg"]
                    from_0 = mode_0["from"]
                    if from_0 == "all":
                        if type_0 == "include":
                            if get_msg_0 in message_input:
                                event_0 = value_0["event"]
                                if event_0 == "g-s":
                                    sand_msg_0 = value_0["return_msg"]
                                    if message_type == "group":
                                        group_id = main_into["group_id"]
                                        return_0 = send_group_msg(group_id, sand_msg_0)
                                    elif message_type == "private":
                                        user_id = main_into["user_id"]
                                        return_0 = send_private_msg(user_id, sand_msg_0)
                                else:
                                    pass
                            else:
                                pass
                        elif type_0 == "exact":
                            if get_msg_0 == message_input:
                                event_0 = value_0["event"]
                                if event_0 == "g-s":
                                    sand_msg_0 = value_0["return_msg"]
                                    if message_type == "group":
                                        group_id = main_into["group_id"]
                                        return_0 = send_group_msg(group_id, sand_msg_0)
                                    elif message_type == "private":
                                        user_id = main_into["user_id"]
                                        return_0 = send_private_msg(user_id, sand_msg_0)
                                else:
                                    pass
                            else:
                                pass
                        else:  # TODO 这里要加其他的mode
                            pass
                    elif from_0 == "private":
                        pass
                    elif from_0 == "group":
                        pass
                    else:
                        print("WRROW")
                else:
                    pass
        if message_input == "/help":
            if message_type == "group":
                group_id = main_into["group_id"]
                message_out = "欢迎使用机器人小鸽(目前处于测试开发阶段)\n现有功能：\n1.AI(差不多可以用)\n2.签到(也在开发)\n3.天气预报(输入/天气即可获取)\n4.翻译(格式：/翻译：balabala(目前仅支持中翻英)\n#更多功能测试中，还未上线，有建议可以在空间下留言(格式：/留言：balabala)"
                return_0 = send_group_msg(group_id, message_out)
            else:
                pass
        elif message_input == "签到123456":
            now_time = datetime.datetime.now().strftime('%R')
            now_time_hour = datetime.datetime.now().strftime('%H')
            now_time_hour_print = int(now_time_hour[-1])
            ran_nub = str(random.randint(1, 9))
            if 0 <= now_time_hour_print < 6:
                time_i = "time1"
            elif 6 <= now_time_hour_print < 12:
                time_i = "time2"
            elif 12 <= now_time_hour_print < 18:
                time_i = "time3"
            elif 18 <= now_time_hour_print <= 24:
                time_i = "time4"
            else:
                print("ERROW:79")
            time_0 = time_i
            with open('json/yuju.json', 'r') as yuju:
                yuju_input = json.load(yuju)
                input_msg1 = yuju_input["qiandao"]
                input_msg2 = input_msg1[time_0]
                input_msg3 = input_msg2[ran_nub]
                if message_type == "group":
                    group_id = main_into["group_id"]
                    message_out = input_msg3
                    return_0 = send_group_msg(group_id, message_out)
                else:
                    pass
        elif message_input == "/天气":
            message_out = weather.main()
            if message_type == "group":
                group_id = main_into["group_id"]
                return_0 = send_group_msg(group_id, message_out)
            else:
                user_id = main_into["user_id"]
                return_0 = send_private_msg(user_id, message_out)
        elif "/留言：" in message_input:
            with open('liuyan.txt', 'a') as liuyan:
                if message_type == "private":
                    user_id = main_into["user_id"]
                    write_into = "from:" + str(user_id) + "\n" + "message:" + str(message_input)
                    write_into.replace('/留言：', '')
                    liuyan.write(write_into)
                    message_out = "留言添加成功"
                    return_0 = send_private_msg(user_id, message_out)
                else:
                    pass
        elif "/fy/" in message_input:
            query_0 = message_input.replace('/fy/', '')
            return_ans = Baidu_Text_transAPI.transport(query_0)
            return_ans2 = json.loads(return_ans)
            ans_msg = return_ans2["trans_result"]
            ans_msg_src = ans_msg[0]["src"]
            ans_msg_dst = ans_msg[0]["dst"]
            if message_type == "private":
                user_id = main_into["user_id"]
                message_out = "翻译:" + ans_msg_src + "\n" + "结果:" + ans_msg_dst
                return_0 = send_private_msg(user_id, message_out)
            else:
                group_id = main_into["group_id"]
                user_id = main_into["user_id"]
                message_out = "[CQ:at,qq=" + str(
                    user_id) + "]" + "\n" + "翻译:" + ans_msg_src + "\n" + "结果:" + ans_msg_dst
                return_0 = send_group_msg(group_id, message_out)
        elif message_input == "/get_p_0":
            message_out_1 = function.get_p_p_2()
            if message_out_1 == "ERROR":
                print("ERROW")
                message_out_0 = "错误"
            else:
                message_out_0 = str(message_out_1)
            message_out = "[CQ:image,file=" + message_out_0 + ",type=show,id=40000]"
            print(message_out)
            if message_type == "group":
                group_id = main_into["group_id"]
                return_0 = send_group_msg(group_id, message_out)
            elif message_type == "private":
                user_id = main_into["user_id"]
                return_0 = send_private_msg(user_id, message_out)
        elif message_input == "":
            pass
        elif message_input == "":
            pass
        elif message_input == "":
            pass
        elif message_input == "":
            pass
        elif message_input == "":
            pass
        elif message_input == "":
            pass
        elif message_input == "":
            pass
        elif "小鸽" in message_input:
            if message_type == "group":
                group_id = main_into["group_id"]
                message_input1 = message_input.replace("小鸽", "")
                message_out = function.ai_msg2(message_input1)
                if str(message_out) == "None":
                    message_out = function.ai_msg(message_input)
                else:
                    pass
                return_0 = send_group_msg(group_id, message_out)
            else:
                pass
        else:
            if message_type == "private":
                user_id = function.main_into["user_id"]
                try:
                    message_input1 = message_input.replace("小鸽", "")
                except:
                    pass
                message_out = function.ai_msg2(message_input)
                if str(message_out) == "None":
                    message_out = function.ai_msg(message_input)
                else:
                    pass
                return_0 = send_private_msg(user_id, message_out)
            else:
                pass
    else:
        pass
    return ''


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5701,debug=False)
