import json
import logging
import sys
import psycopg2
import requests
import time
import 新运维平台登录 as Yunweipingtai

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
GET_CCU_INFO = {"nodeid": "*", "opcode": "GET_CCU_INFO", "requester": "HJ_Server", "timeout": 15, "arg": "*"}
SET_LOG_CONFIG = {"arg": {"log_leave": "-A"}, "nodeid": "*", "opcode": "SET_LOG_CONFIG", "requester": "HJ_Server"}
CCU = 'CCU_21312'
# data = SET_LOG_CONFIG
ON = {
		"nodeid": "293",
		"opcode": "SWITCH",
		"requester": "HJ_Server",
		"timeout": 6,
		"arg": "ON"
	}
OFF = {
	"nodeid": "293",
	"opcode": "SWITCH",
	"requester": "HJ_Server",
	"timeout": 6,
	"arg": "OFF"
}
data = ON
f = open('多个主机循环发送.json', "r")
a = json.load(f)
for CCU in a:  # I 代表主机号
	logging.info('获取到的CCU信息%s', CCU)
	if CCU:
		count = 51  # count 代表循环次数
		for i in range(1, count):
			print(i)
			time.sleep(180)
			r = Yunweipingtai.Sent_Sockit(CCU, data)
			if 'status' in r:
				if r['status'] == 'success':
					logging.info("接受到的主机%s回复opcode%s信息:%s" % (CCU, data['opcode'], r['arg']))
				elif r['status'] == 'timeout':
					logging.error("接受到的主机%s回复opcode%s信息超时，主机可能不在线,错误信息%s" % (CCU, data['opcode'], r['errorinfo']))
				elif r['status'] == 500:
					logging.error("接受到的主机%s回复opcode%s信息:%s" % (CCU, data['opcode'], r['error']))
			else:
				logging.error("接受到的主机%s回复opcode%s信息:%s" % (CCU, data['opcode'], r))
			logging.info("%s主机第%s次获取消息" % (CCU, i))
