import time

import requests

# 新运维平台需要更换token，有效期24H
headers = {
	'content-type': 'application/json',
	'token': 'APPLICATION:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsZWFkZXIiOiIyIiwibmlja25hbWUiOiLpq5jpobrls7AiLCJ0ZW5hbnRJZCI6IjU4OGFjYTE2YzFlZTQzMWM4ZGE1YmZkZGM3MjI5ZDg2IiwidGltZSI6IjE2NTUwODQ3Mjg3NDUiLCJleHAiOjE2NTUxNzExMjgsInVzZXJJZCI6IjhhNWVlZTVhNzczNTRhNDZiNWUxZjg5OTJmZTJmZjYzIiwiaWF0IjoxNjU1MDg0NzI4LCJlbWFpbCI6Imdhby5zaHVuZmVuZ0Bpa29ua2UuY29tIiwib3JnSWQiOiJkMWQ4ZWFhZWU5YTk0NDJmOGI2ZmViNDVhNDRhMmNlNiIsInVzZXJuYW1lIjoiMTg2NTY1MDg4NjAifQ.LZw0-wqIuEvvPVGbtMpRHWXsDvynOa4whljZ2jm_gYk'
}


# env="test"

# 开起LSC
def LSC_SWITCH_ON(CCU, env="nation"):
	"""
	开起LSC
	:param env: 拆入主机环境
	:param CCU: 传入主机号开启LSC
	"""
	# r4 = LSC_TEST.LSC_OPEN(i)
	url = "https://oms.ikonke.com:10000/host-maintenance-server/1.0/ccu/lsc/switch"
	data = {"ccuId": CCU, "env": env, "onOff": "on"}
	# print(data)
	try:
		r = requests.post(url, headers=headers, json=data).json()
		# print(r)
		return r
	except Exception as e:
		print(e)


#  发送报文
def Sent_Sockit(CCU, data):
	"""
	开起LSC
	:param data: 传入主机环境
	:param CCU: 传入主机号开启LSC
	"""
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
	url = "https://oms.ikonke.com:10000/host-maintenance-server/1.0/ccu/opt/" + CCU + "/request"
	try:
		r = requests.post(url, headers=headers, json=OFF).json()
		print(r)
		time.sleep(1)
		r = requests.post(url, headers=headers, json=data).json()
		print(r)
		return r
	except Exception as e:
		print(e)


# 拿端口
def LSC_GET_PORT(CCU, env):
	"""
	拿端口
	:param env: 主机环境
	:param CCU: 通过主机号拿到端口
	"""
	url = "https://oms.ikonke.com:10000/host-maintenance-server/1.0/ccu/ssh/port"
	nation = {
		"ccuId": CCU, "env": "nation"
	}
	test = {
		"ccuId": CCU, "env": "test"
	}
	if env == "test":
		data = test
	else:
		data = nation
	try:
		r = requests.post(url, headers=headers, json=data).json()
		return r
	except Exception as e:
		print(e)


def Login():
	"""
	 运维平台登录，获取login
	"""
	url = 'https://oms.ikonke.com:10000/oauth2-server/login'

	headers = {
		'username': '18656508860',
		'pwd': 'ggg123123',
	}
	try:
		r = requests.post(url, headers=headers).json()
		print(r)
	except Exception as e:
		print(e)


if __name__ == '__main__':
	Login()
