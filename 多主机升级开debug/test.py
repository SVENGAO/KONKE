tt1 = 40
tt2 = 17

while tt2 <= tt1:
	print(tt2)
	tt3 = str(tt2)
	SET_ZIGBEE_GROUP1 = "!{\"arg\":{\"id\":\"" + tt3 + "'\",\"name\":\"" + tt3 + "\",\"nodes\":[{\"nodeid\":\"1787\"},{\"nodeid\":\"1788\"}],\"room_id\":\"1\"},\"nodeid\":\"*\",\"opcode\":\"SET_ZIGBEE_GROUP\",\"requester\":\"HJ_Config\"}$"
	print(SET_ZIGBEE_GROUP1)
	tt2 += 1
