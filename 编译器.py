#用于直接输入并完成编译
import sys,os,requests




print("欢迎使用鸽牌机器人（编译器）")
print("途中输入q即为退出")
while True:
    mode = input("请输入选择的模式：全局/私聊/群聊")
    if mode == "全局":
        mode_input = "all"
        break
    elif mode == "私聊":
        mode_input = "private"
        break
    elif mode == "群聊":
        mode_input = "group"
        break
    elif mode == "q":
        sys.exit()
    else:
        print("输入错误，请重新输入q")


#while True:
#    print("http://www.baidu.com")


print("请输入触发事件：")
print("事件对应表：私聊消息\n群消息\n群文件.上传\n群管理员变动\n群成员减少\n群成员增加\n群禁言\n好友添加\n群消息撤回\n好友消息撤回\n好友戳一戳\n群内戳一戳\n群红包运气王提示\n群成员荣誉变更提示\n群成员名片更新\n接收到离线文件\n加好友请求\n加群请求/邀请\n其他客户端在线状态变更\n精华消息")
print(r"表格详情请见：https://docs.go-cqhttp.org/event/")
print("并自己对照输入数字\n如：1对应私聊消息")
print("目前只能使用前两个功能，其余还在开发中")
event = input("")


event_input = ""


while True:
    if event == "1":
        pass
    elif event == "2":
        pass
    elif event == "3":
        pass
    elif event == "4":
        pass
    elif event == "5":
        pass
    elif event == "6":
        pass
    elif event == "7":
        pass
    elif event == "8":
        pass
    elif event == "9":
        pass
    elif event == "10":
        pass
    elif event == "11":
        pass
    elif event == "12":
        pass
    elif event == "13":
        pass
    elif event == "14":
        pass
    elif event == "15":
        pass
    elif event == "16":
        pass
    elif event == "17":
        pass
    elif event == "18":
        pass
    elif event == "19":
        pass
    elif event == "20":
        pass
    elif event == "q":
        sys.exit()
    else:
        pass