import 新运维平台登录 as Yunweipingtai

GET_CCU_INFO = {"nodeid": "*", "opcode": "GET_CCU_INFO", "requester": "HJ_Server", "timeout": 15, "arg": "*"}
# 智睿主机升级协调器
OTA_COORD_UPGRADE = {
	"arg": {
		"url": "https://test-kkhz-smarthome.oss-cn-hangzhou.aliyuncs.com/ota/test/ctr/flat/0.4.1/Z3SOCGW_flat_mg21a020_sv0.4.1.gbl",
		"firmware_version": "0.4.1"},
	"nodeid": "203",
	"opcode": "OTA_COORD_UPGRADE",
	"requester": "HJ_Server"
}

CCU = 'CCU_21312'
data = GET_CCU_INFO
r = Yunweipingtai.Sent_Sockit(CCU, data)
print(r)
