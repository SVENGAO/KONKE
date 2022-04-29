import json
import logging
import SSH命令发送 as SSHUpgrade
import 新运维平台登录 as Yunweipingtai

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
# """
# 使用前去json文件中更改主机号，主机类型，主机服务器环境
# """
P12_6730 = 'wget -O /tmp/kk-9531-ap86-key.bin http://web.nj-ikonke.site:20001/ccu_package/kkfirmware/ap86-key-p12/2.67.30/20220428205403/kk-9531-ap86-key.bin;sleep 3;sysupgrade /tmp/kk-9531-ap86-key.bin'
P8_6725 = 'wget -O /tmp/kk-9531-dtgw.bin http://web.nj-ikonke.site:20001/ccu_package/kkfirmware/ap86-dt-p8/2.67.25/20220329160806/kk-9531-dtgw.bin;sleep 3;sysupgrade /tmp/kk-9531-dtgw.bin'
P8_6730 = 'wget -O /tmp/kk-9531-dtgw.bin http://web.nj-ikonke.site:20001/ccu_package/kkfirmware/ap86-dt-p8/2.67.30/20220428204134/kk-9531-dtgw.bin;sleep 3;sysupgrade /tmp/kk-9531-dtgw.bin'

repairDb_updateCcu = 'cd /tmp/;wget http://file.nj-ikonke.site:8096/index.php/s/ggKJxmyynerP8EA/download/repairDb_updateCcu.sh;sleep 2;sh repairDb_updateCcu.sh'
#  自定义查询命令

P15_6730 = 'wget -O /tmp/KK-CC-J86.bin http://web.nj-ikonke.site:20001/ccu_package/kkfirmware/KK-CC-J86-p15/2.67.30/20220428204509/KK-CC-J86.bin;sleep 3;sysupgrade /tmp/KK-CC-J86.bin'

P14_6725 = 'wget -O /tmp/KK-CC-E86.bin http://web.nj-ikonke.site:20001/ccu_package/kkfirmware/KK-CC-E86-p14/2.67.25/20220329161326/KK-CC-E86.bin;sleep 3;sysupgrade /tmp/KK-CC-E86.bin'
P14_6008 = 'wget -O /tmp/KK-CC-E86.bin http://web.nj-ikonke.site:20001/ccu_package/kkfirmware/KK-CC-E86-p14/2.60.8/20210622194552/KK-CC-E86.bin;sleep 3;sysupgrade /tmp/KK-CC-E86.bin'
P14_5617 = 'wget -O /tmp/KK-CC-E86.bin http://web.nj-ikonke.site:20001/ccu_package/kkfirmware/KK-CC-E86-p14/2.56.17/20210115142416/KK-CC-E86.bin;sleep 3;sysupgrade /tmp/KK-CC-E86.bin'
P14_6730 = 'wget -O /tmp/KK-CC-E86.bin http://web.nj-ikonke.site:20001/ccu_package/kkfirmware/KK-CC-E86-p14/2.67.30/20220428204750/KK-CC-E86.bin;sleep 3;sysupgrade /tmp/KK-CC-E86.bin'
ssh_cmd = P8_6730


def get_CCU():
	"""
	通过文件获取到主机号
	"""
	f = open('远程获取端口SSH发送升级命令主机号.json', "r")
	a = json.load(f)

	for i in a:  # I 代表主机号
		logging.info('获取到的CCU信息%s', i)
		if i != '':
			# print(i)
			zj_type = a[i][0]
			env = a[i][1]
			# print(zj_type)
			get_Port(i, zj_type, env)


def get_Port(CCU, zj_type, env):
	"""
	通过主机号，获取主机远程端口
	"""
	try:
		r = Yunweipingtai.LSC_GET_PORT(CCU, env)
		if 'status' in r:
			if r['status'] == 'success':
				ssh_port = r['arg']['tunnel_remote_port']
				logging.info("获取端口成功：%s", ssh_port)

				r2 = SSHUpgrade.SSHUPGRADE(ssh_port, ssh_cmd, zj_type)
				if r2 == "0":
					logging.info("命令发送完成，稍后检查主机")
			elif r['status'] == 'timeout':
				logging.info("获取端口失败原因:ccu opt timeout,主机可能不在线，或者在测试服务器。错误码：%s", r['status'])
			elif r['status'] == 500:
				logging.info("获取端口失败原因:Internal Server Error,错误码：%s", r['status'])
			elif r['status'] == 401:
				logging.info("Token失效，需要更换新的Token,错误码：%s", r['status'])
			else:
				logging.info("请求端口失败,错误码%s", r['status'])
		else:
			logging.info('请求接口失败')
	except Exception as e:
		print(e)


if __name__ == '__main__':
	get_CCU()
