import os, re, requests, json, weather, datetime, random, Baidu_Text_transAPI
from turtle import st
from urllib import parse
import os
import urllib.request

# 一些常量,只是为了敲代码快一点
sand_message_user = ""
return_user = ""
all_input = ()
event = ""
message_input = ""
count_number = 0
return_0 = ""  # 一般无用，仅作接受

"""
所有带0的都是main函数的常量，勿动
"""

"""
g代表收到信息执行（被动）
i代表特定时间或事件触发（主动）
"""

"""
# 私聊快捷引用
time = main_into["time"]
self_id = main_into["self_id"]
post_type = main_into["post_type"]
message_type = main_into["message_type"]
sub_type = mian_into["sub_type"]
temp_source = main_into["temp_source"]
message_id = main_into["message_id"]
user_id = main_into["user_id"]
message = main_into["message"]
raw_message = main_into["raw_message"]
font = mian_into["font"]
sender = main_into["sender"]
"""

"""字段名	    数据类型	    可能的值	    说明
time	        int64	    -	        事件发生的时间戳
self_id	        int64	    -	        收到事件的机器人 QQ 号
post_type       string	    message	    上报类型
message_type	string	    private	    消息类型
sub_type	    string	    friend,group消息子类型, 如果是好友则是 friend, 如果是群临时会话则是 group, 如果是在群中自身发送则是 group_self
                            ,group_self
                            ,other	
temp_source	    int	-	                临时会话来源
message_id	    int32	    -	        消息 ID
user_id	        int64	    -	        发送者 QQ 号
message	        message	    -	        消息内容
raw_message	    string	    -	        原始消息内容
font	        int32	    -	        字体
sender	        object	    -	        发送人信息
"""


# main函数
def main(main_into):
    global time_i
    post_type = main_into["post_type"]
    if post_type == "message":
        log_in(str(main_into))
        message_input = main_into["message"]
        message_type = main_into["message_type"]
        #check = str(filter(main_into,message_type))
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
                message_out = "欢迎使用机器人小鸽(目前处于测试开发阶段)\n现有功能:\n1.AI(差不多可以用)\n2.签到(也在开发)\n3.天气预报(输入/天气即可获取)\n4.翻译(格式:/翻译:balabala(目前仅支持中翻英)\n#更多功能测试中，还未上线，有建议可以在空间下留言(格式:/留言:balabala)"
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
        elif "/留言:" in message_input:
            with open('cache/liuyan.txt', 'a') as liuyan:
                if message_type == "private":
                    user_id = main_into["user_id"]
                    write_into = "from:" + str(user_id) + "\n" + "message:" + str(message_input)
                    write_into.replace('/留言:', '')
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
                message_out = "[CQ:at,qq=" + str(user_id) + "]" + "\n" + "翻译:" + ans_msg_src + "\n" + "结果:" + ans_msg_dst
                return_0 = send_group_msg(group_id, message_out)
        elif message_input == "/get_p_0":
            message_out_1 = get_p_p_2()
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
                message_out = ai_msg2(message_input1)
                if str(message_out) == "None":
                    message_out = ai_msg(message_input)
                else:
                    pass
                return_0 = send_group_msg(group_id, message_out)
            else:
                pass
        else:
            if message_type == "private":
                user_id = main_into["user_id"]
                try:
                    message_input1 = message_input.replace("小鸽", "")
                except:
                    pass
                message_out = ai_msg2(message_input)
                if str(message_out) == "None":
                    message_out = ai_msg(message_input)
                else:
                    pass
                return_0 = send_private_msg(user_id, message_out)
            else:
                pass
    else:
        pass


# TODO 将所有字符串加str！！！
# 发送私聊信息
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
    sand_message_user = "http://127.0.0.1:5700/" + "send_group_forward_msg?" + "group_id=" + str(
        group_id) + "&" + "message=" + str(messages)
    return_user = requests.post(sand_message_user)
    return return_user


# 发送消息
# 此模式不常用,请尽量不要引用
def send_msg(message, user_id='', group_id='', message_type='', auto_escape=''):
    if group_id == '':  # 私聊
        sand_message_user = "http://127.0.0.1:5700/" + "send_private_msg?" + "user_id=" + str(user_id) + "&" + "message=" + str(message) + "&" + "auto_ecscape=" + str(auto_escape)
        return_user = requests.post(sand_message_user)
    else:  # 通过群发
        sand_message_user = "http://127.0.0.1:5700/" + "send_private_msg?" + "user_id=" + str(user_id) + "&" + "group_id=" + str(group_id) + "&" + "message=" + str(message) + "&" + "auto_ecscape=" + str(auto_escape)
        return_user = requests.post(sand_message_user)
    return return_user


# 撤回消息
def delete_msg(message_id):
    message_id = str(message_id)
    sand_message_user = "http://127.0.0.1:5700/" + "delete_msg?" + "message_id=" + message_id
    return_user = requests.post(sand_message_user)
    return return_user


# 获取消息
def get_msg(message_id):
    message_id = str(message_id)
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
    message_id = str(message_id)
    sand_message_user = "http://127.0.0.1:5700/" + "get_forward_msg?" + "message_id=" + message_id
    return_user = requests.post(sand_message_user)
    return return_user
    # 此处同上


# 获取图片信息
def get_image(file):
    file = str(file)
    sand_message_user = "http://127.0.0.1:5700/" + "get_image?" + "file=" + file
    return_user = requests.post(sand_message_user)
    return return_user


# 群组踢人
def set_group_kick(group_id, user_id, reject_add_request='false'):
    group_id = str(group_id)
    user_id = str(user_id)
    reject_add_request = str(reject_add_request)
    sand_message_user = "http://127.0.0.1:5700/" + "set_group_kick?" + "group_if=" + group_id + "&" + "user_id=" + user_id + "&" + "reject_add_request=" + reject_add_request
    return_user = requests.post(sand_message_user)
    return return_user


# 群组单人禁言
def set_group_ban(group_id, user_id, duration='30 * 60'):  # 最后一个参数为禁言时间，单位s，0秒表示取消禁言
    group_id = str(group_id)
    user_id = str(user_id)
    duration = str(duration)
    sand_message_user = "http://127.0.0.1:5700/" + "set_group_ban?" + "group_id=" + group_id + "&" + "user_id=" + user_id + "&" + "duration=" + duration
    return_user = requests.post(sand_message_user)
    return return_user
    # 无响应数据


# 群组匿名用户禁言    
def set_group_anonymous_ban(group_id,duration='',anonymous='30 * 60',flag='',anonymous_flag=''):#anonymous，anonymous_flag或flag效果相同，只需择其一即可,若都传入,则使用 anonymous,推荐使用anonymous,禁言时长单位秒
    group_id = str(group_id)
    try:
        duration = str(duration)
    except:
        pass
    try:
        duration = str(flag)
    except:
        pass
    try:
        duration = str(anonymous_flag)
    except:
        pass
    sand_message_user = "http://127.0.0.1:5700/" + "set_group_anonymous_ban?" + "group_id=" + group_id +"&" + "anonymous=" + anonymous + "&" + "duration=" + duration
    return_user = requests.post(sand_message_user)
    return return_user
    # 无响应数据


# 群组全员禁言
def set_group_whole_ban(group_id,enable='true'):
    group_id = str(group_id)
    sand_message_user = "http://127.0.0.1:5700/" + "set_group_whole_ban?" + "group_id=" + group_id +"&" + "enable=" + enable
    return_user = requests.post(sand_message_user)
    return return_user
    # 无响应数据


# 群组设置管理员
def set_group_admin(group_id,user_id,enable='true'):
    group_id = str(group_id)
    user_id = str(user_id)
    sand_message_user = "http://127.0.0.1:5700/" + "set_group_admin?" + "group_id=" + group_id +"&" + "user_id=" + user_id + "&" + "enable=" + enable
    return_user = requests.post(sand_message_user)
    return return_user
    # 无响应数据


# 群组匿名
"""暂不支持"""
def set_group_anonymous(group_id,enable='true'):
    group_id = str(group_id)
    sand_message_user = "http://127.0.0.1:5700/" + "set_group_anonymous?" + "group_id=" + group_id +"&" + "enable=" + enable
    return_user = requests.post(sand_message_user)
    return return_user
    # 无响应数据


# 设置群名片 ( 群备注 )
def set_group_card(group_id,user_id,card=''):#card群名片内容, 不填或空字符串表示删除群名片
    group_id = str(group_id)
    user_id = str(user_id)
    sand_message_user = "http://127.0.0.1:5700/" + "set_group_card?" + "group_id=" + group_id +"&" + "user_id=" + user_id + "&" + "card=" + card
    return_user = requests.post(sand_message_user)
    return return_user
    # 无响应数据


# 设置群名
def set_group_name(group_id,group_name):
    group_id = str(group_id)
    group_name = str(group_name)
    sand_message_user = "http://127.0.0.1:5700/" + "set_group_name?" +"group_id=" + group_id + "&" + "group_name=" + group_name
    return return_user
    # 无响应数据


# 退出群组
def set_group_leave(group_id,is_dismiss='false'):
    group_id = str(group_id)
    sand_message_user = "http://127.0.0.1:5700/" + "set_group_name?" + "group_id=" + group_id + "&" + "is_dismiss=" + is_dismiss
    return return_user
    # 无响应数据


# 
# def 



# 晚间10：00报时加天气预报
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


def get_picture():
    url_0 = 'https://www.duitang.com/blogs/tag/?name=Pixiv%E7%AB%99'
    html_0 = requests.get(url_0).content.decode()
    print(html_0)  # TODO


def ai_msg(msg):
    url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg={}'.format(parse.quote(msg))
    html = requests.get(url)
    return_msg = html.json()["content"]
    return return_msg


def ai_msg_p(msg_0):
    try:
        msg = str(msg_0)
        cq_code_0 = re.search("{(.*)}", msg)
        msg_r = msg.replace('{', '').replace('}', '').replace(str(cq_code_0), '')
        cq_code = "[CQ:face,id=" + str(cq_code_0) + "]"
        return_msg = cq_code + msg_r
        return return_msg
    except:
        pass


def get_p_p_1(message_input):
    # 默认随机模式：/get_p
    # 默认消息格式：/get_p#此处加上标签#
    url_post = "https://api.lolicon.app/setu/v2"
    r18 = ""  # 默认0
    num = ""  # 默认1
    uid = "1"
    keyword = ""  # 默认不用
    tag = ""
    size = ""  # 默认["original"]
    proxy = ""  # 默认i.pixiv.cat
    dateAfter = ""
    dateBefore = ""
    dsc = ""  # 默认false
    data = ""
    if message_input == "/get_p":
        url_return = requests.get(url_post).json()
        data = url_return["data"]
        data_1 = data[0]
        urls = data_1["urls"]
        original = urls["original"]
        image_url = original
        file_path = 'C:/python-pro/mall_splier'
        try:
            if not os.path.exists(file_path):
                os.makedirs(file_path)  # 如果没有这个path则直接创建
            file_suffix = os.path.splitext(image_url)[1]
            print(file_suffix)
            filename = '{}{}'.format(file_path, file_suffix)
            print(filename)
            urllib.request.urlretrieve(image_url, filename=filename)
            print(11111)

        except IOError as e:
            print(1, e)

        except Exception as e:
            print(2, e)
    else:
        message_get = re.search('#(.*?)#', message_input).group(0)
        tag = message_get


def get_p_p_2():
    url = "https://www.dmoe.cc/random.php?return=json"
    headers = {"authority": "www.dmoe.cc",
               "method": "GET",
               "path": "/random.php?233335556958",
               "scheme": "https",
               "accept": "image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
               "accept-encoding": "gzip, deflate, br",
               "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
               "referer": '"https://www.dmoe.cc/","sec-ch-ua":"Microsoft Edge";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
               "sec-ch-ua-mobile": "?0",
               "sec-ch-ua-platform": '"Windows"',
               "sec-fetch-dest": "image",
               "sec-fetch-mode": "no-cors",
               "sec-fetch-site": "same-origin",
               "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53"
               }
    return_url = requests.get(url, headers=headers).json()
    if str(return_url["code"]) == str("200"):
        url_return = return_url["imgurl"]
        return url_return
    else:
        return "ERROR"


def ai_msg2(msg):
    with open('D:\myQQrobot\myQQrobot\程序\语料库\AnimeThesaurus-main\data.json',encoding='UTF-8') as f:
        lines = json.load(f)
        for keys in lines:
            if keys in msg:
                return_msg = random.choice(lines[keys])
                return return_msg
            else:
                pass


def test_1():
    print("ok")


def log_in(into):
    with open(mode='a' , file='D:\myQQrobot\myQQrobot\程序\python2\log\log.txt' , encoding='UTF-8') as f:
        f.write(into + '\n')


def filter(main_into,user_type):
    with open(r'D:\myQQrobot\myQQrobot\程序\python2\json__\filter.json__') as f:
        lines = json.load(f)
        for keys in lines:
            if user_type == "group":
                for keys2 in lines[keys]:
                    if main_into["group_id"] == keys[keys2]:
                        print("no")
                        return 'no'
                    else:
                        print("yes")
                        return 'yes'
            else:
                for keys2 in keys:
                    if main_into["user_id"] == keys[keys2]:
                        print("no")
                        return 'no'
                    else:
                        print("yes")
                        return 'yes'
        else:
            pass


def pan():
    pass


