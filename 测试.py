# -*- coding: utf-8 -*-
import json

#import lxml,requests,re,random
#from bs4 import BeautifulSoup
#from lxml import etree
#import bs4,function
#import requests,os
#from urllib import parse
#from TFH import function

#path_0 = r"C:\Users\13957\Desktop\游戏"
#files_0 = os.listdir(path_0)
#type = type(files_0)
#for files in files_0:
#    print(files.encode().decode(encoding='utf-8'))
#print(type)
#print(str(files_0))

def 打印消息(msg):
    print(msg)
def 接受消息(msg):
    msg_in = input(msg)
    return msg_in
消息 = 接受消息("请输入消息内容")
打印消息(消息)