import json
import logging
import sys
import psycopg2
import requests
import time
import socket
import 新运维平台登录 as Yunweipingtai

GET_CCU_INFO = {"nodeid": "*", "opcode": "GET_CCU_INFO", "requester": "HJ_Server", "timeout": 15, "arg": "*"}

CCU = 'CCU_189870'
data = GET_CCU_INFO

f = open('多个主机循环发送.json', "r")
a = json.load(f)
print(a)
for index in a:  # I 代表主机号
	logging.info('获取到的CCU信息%s', index)
	if index:
		r = Yunweipingtai.Sent_Sockit(index, data)
		logging.info("接受到的主机回复信息:%s", r)
for index in 'Python':  # 第一个实例
	print("当前字母: %s" % index)
