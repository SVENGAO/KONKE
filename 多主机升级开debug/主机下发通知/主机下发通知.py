import requests
import logging
import json

logging.basicConfig(level=logging.INFO, format='%(message)s')


def Notion_CCU():
	"""
	通知大主机有新版本升级提示
	"""

	f = open('123.txt', "r")
	a = json.load(f)

	for i in a:  # I 代表主机号
		if i != '':
			if a[i] == 'test':
				logging.info("测试环境主机%s", i)
				url = "http://ops-test.nj-ikonke.site:1080/api/info/ccu" + i + "/notifyCcuUpgrade"
			else:
				logging.info("正式环境主机%s", i)
				url = "https://iot-ops.ikonke.com/api/info/ccu/" + i + "/notifyCcuUpgrade"
			r = requests.get(url).json()
			if 'code' in r:
				if r['code'] == 200:
					logging.info('%s下发升级通知成功', i)


def Getversion_CCU():
	"""
		获取到主机版本号
	"""

	f = open('本地发送socket报文主机号.json', "r")
	a = json.load(f)

	for i in a:  # I 代表主机号
		if i != '':
			if a[i] == 'test':
				logging.info("测试环境主机%s", i)
				url1 = "http://ops-test.nj-ikonke.site:1080/api/info/ccu/ccuInfo"
			else:
				logging.info("正式环境主机%s", i)
				url1 = "https://iot-ops.ikonke.com/api/info/ccu/ccuInfo"
			data = {"projectId": "1", "ccuId": i}
			r2 = requests.post(url1, json=data).json()
			if 'code' in r2:
				if r2['code'] == 200:
					if 'data' in r2:
						if 'installVersion' in r2['data']['baseInfo']:
							version = r2['data']['baseInfo']['installVersion']
							logging.info("%s主机已安装的版本为%s" % (i, version))
						else:
							logging.info("未获取到主机版本")
			else:
				logging.info("查询接口返回失败")


def Getversion_CCU_BY_CCU():
	"""
		获取到主机版本号
	"""
	with open('123.txt', "r") as f:
		text = f.read().splitlines()

	# 先读取一行
	# a1 = text
	# print(len(a1))

	for index in range(len(text)):
		if text[index] != "":
			# print(text[index])
			url1 = "https://iot-ops.ikonke.com/api/info/ccu/ccuInfo"
			data = {"projectId": "1", "ccuId": text[index]}
			r2 = requests.post(url1, json=data).json()
			# print(r2)
			if 'code' in r2:
				if r2['code'] == 200:
					# print(r2)
					if 'data' in r2:
						if 'installVersion' in r2['data']['baseInfo']:
							# print(r2['data']['baseInfo']['installVersion'])
							if r2['data']['baseInfo']['installVersion'] is not None:
								version = r2['data']['baseInfo']['installVersion'][0:4]
							else:
								version = 'None'
							pid = r2['data']['businessInfo']['pId']
							logging.info("主机号：%s, 主机类型：%s,已安装的版本为：%s" % (text[index], pid, version))
						else:
							logging.info("未获取到主机版本")
			else:
				logging.info("查询接口返回失败")


if __name__ == '__main__':
	# 通知大主机有新版本升级提示
	# Notion_CCU()
	# 获取到主机版本号
	# Getversion_CCU()
	# 获取到主机版本号
	Getversion_CCU_BY_CCU()
