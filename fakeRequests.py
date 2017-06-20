#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Developed by Roger Monteiro
#Github: https://github.com/RogerMonteiro124

from fake_useragent import UserAgent
import requests
import os

#Gerando um user agente fake
def geraUserAgente():
	ua=UserAgent()
	ua.update
	user=""
	return str(user)
def urlAlvo():
	os.system("setterm -foreground green")
	url=raw_input('Endereco do site alvo:>_\nhttp://')
	return str(url)
def conectaSite(user,url):
	headers = {'User-Agent': user}
	response = requests.get(url, headers=headers)
	os.system("setterm -foreground blue");
	print(response.content)
def Banner():
	os.system("clear")
	os.system("setterm -foreground red")
	print '''
·▄▄▄ ▄▄▄· ▄ •▄ ▄▄▄ .    ▄▄▄  ▄▄▄ ..▄▄▄  ▄• ▄▌▄▄▄ ..▄▄ · ▄▄▄▄▄.▄▄ · 
▐▄▄·▐█ ▀█ █▌▄▌▪▀▄.▀·    ▀▄ █·▀▄.▀·▐▀•▀█ █▪██▌▀▄.▀·▐█ ▀. •██  ▐█ ▀. 
██▪ ▄█▀▀█ ▐▀▀▄·▐▀▀▪▄    ▐▀▀▄ ▐▀▀▪▄█▌·.█▌█▌▐█▌▐▀▀▪▄▄▀▀▀█▄ ▐█.▪▄▀▀▀█▄
██▌.▐█ ▪▐▌▐█.█▌▐█▄▄▌    ▐█•█▌▐█▄▄▌▐█▪▄█·▐█▄█▌▐█▄▄▌▐█▄▪▐█ ▐█▌·▐█▄▪▐█
▀▀▀  ▀  ▀ ·▀  ▀ ▀▀▀     .▀  ▀ ▀▀▀ ·▀▀█.  ▀▀▀  ▀▀▀  ▀▀▀▀  ▀▀▀  ▀▀▀▀ 
	'''
	Help()
def Help():
	os.system("setterm -foreground white")
	print '''
Uso: python fakeRequestes.py
Endereço da WEB é a pagina que deseja acessar 
com um UserAgent falso.
	'''
def main():
	Banner()
	opt=input('''[1] - Usar um UserAgent especifico\n
[2] - Usar um UserAgent randominco\n''')
	if opt ==1:
		os.system("setterm -foreground red")
		print('[1]-ua.ie')
		os.system("setterm -foreground white")
		print('Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)\n')
		os.system("setterm -foreground red")
		print('[2]-ua.msie')
		os.system("setterm -foreground white")
		print('Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)\n')
		os.system("setterm -foreground red")
		print('''[3]-ua['Internet Explorer']''')
		os.system("setterm -foreground white")
		print('Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.2; SV1; .NET CLR 3.3.69573; WOW64; en-US)\n')
		os.system("setterm -foreground red")
		print('[4]-ua.opera')
		os.system("setterm -foreground white")
		print('Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11\n')
		os.system("setterm -foreground red")
		print('[5]-ua.chrome')
		os.system("setterm -foreground white")
		print('Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2\n')
		os.system("setterm -foreground red")
		print('[6]-ua.google')
		os.system("setterm -foreground white")
		print('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13\n')
		os.system("setterm -foreground red")
		print('''[7]-ua['google chrome']''')
		os.system("setterm -foreground white")
		print('Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11\n')
		os.system("setterm -foreground red")
		print('[8]-ua.firefox')
		os.system("setterm -foreground white")
		print('Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1\n')
		os.system("setterm -foreground red")
		print('[9]-ua.ff')
		os.system("setterm -foreground white")
		print('Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1\n')
		os.system("setterm -foreground red")
		print('[10]-ua.safari')
		os.system("setterm -foreground white")
		print('Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25\n')
		userOpt=input('opcao')
		if userOpt == 1:
			ua=UserAgent()
			ua.update
			user=ua.ie
			url='http://'+urlAlvo()
			conectaSite(user,url)
		elif userOpt == 2:
			ua=UserAgent()
			ua.update
			user=ua.msie
			url='http://'+urlAlvo()
			conectaSite(user,url)
		elif userOpt == 3:
			ua=UserAgent()
			ua.update
			user=ua['Internet Explorer']
			url='http://'+urlAlvo()
			conectaSite(user,url)
		elif userOpt == 4:
			ua=UserAgent()
			ua.update
			user=ua.opera
			url='http://'+urlAlvo()
			conectaSite(user,url)
		elif userOpt == 5:
			ua=UserAgent()
			ua.update
			user=ua.chrome
			url='http://'+urlAlvo()
			conectaSite(user,url)
		elif userOpt == 6:
			ua=UserAgent()
			ua.update
			user=ua.google
			url='http://'+urlAlvo()
			conectaSite(user,url)
		elif userOpt == 7:
			ua=UserAgent()
			ua.update
			user=ua['google chrome']
			url='http://'+urlAlvo()
			conectaSite(user,url)
		elif userOpt == 8:
			ua=UserAgent()
			ua.update
			user=ua.firefox
			url='http://'+urlAlvo()
			conectaSite(user,url)
		elif userOpt == 9:
			ua=UserAgent()
			ua.update
			user=ua.ff
			url='http://'+urlAlvo()
			conectaSite(user,url)
		elif userOpt == 10:
			ua=UserAgent()
			ua.update
			user=ua.safari
			url='http://'+urlAlvo()
			conectaSite(user,url)
		else:
			print "Opcao invalida"
			main()
	elif opt ==2:
		ua=UserAgent()
		ua.update
		user=ua.random
	else:
		print "Opção invalida"
		main()
main()